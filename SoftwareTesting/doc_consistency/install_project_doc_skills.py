#!/usr/bin/env python3
"""精确镜像安装项目文档 Skill，并生成可验证来源清单。"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
PROVENANCE_NAME = "SOURCE-PROVENANCE.json"
CALLABLE_DEPENDENCIES = {
    "project-doc-consistency": ("project-doc-consistency", "project-doc-shared"),
    "project-doc-contraction": ("project-doc-contraction", "project-doc-shared"),
    "project-doc-skeleton": ("project-doc-skeleton",),
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_files(root: Path, roots: Iterable[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for root_name in roots:
        base = root / root_name
        if not base.is_dir():
            raise FileNotFoundError(f"缺少目录: {base}")
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.name == PROVENANCE_NAME:
                continue
            relative = path.relative_to(root).as_posix()
            result[relative] = sha256_file(path)
    return result


def mirror_directory(source: Path, target: Path) -> None:
    if target.exists():
        if not target.is_dir():
            raise RuntimeError(f"安装目标不是目录: {target}")
        shutil.rmtree(target)
    shutil.copytree(source, target)


def git_output(source_root: Path, *args: str) -> str:
    result = subprocess.run(
        ("git", "-C", str(source_root), *args),
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Git 命令失败: git {' '.join(args)}\n{result.stdout}{result.stderr}"
        )
    return result.stdout.strip()


def git_metadata(source_root: Path) -> dict[str, str]:
    status = git_output(source_root, "status", "--porcelain")
    if status:
        raise RuntimeError("源仓库工作树或索引不干净，拒绝生成可追溯安装")
    branch = git_output(source_root, "branch", "--show-current")
    if not branch:
        raise RuntimeError("源仓库处于 detached HEAD，拒绝安装")
    return {
        "source_repository": git_output(source_root, "remote", "get-url", "origin"),
        "source_branch": branch,
        "source_commit": git_output(source_root, "rev-parse", "HEAD"),
    }


def build_manifest(
    target_root: Path,
    skill_name: str,
    metadata: dict[str, str],
) -> dict[str, object]:
    roots = CALLABLE_DEPENDENCIES[skill_name]
    return {
        "schema_version": 1,
        "skill_name": skill_name,
        **metadata,
        "installed_at_utc": datetime.now(timezone.utc).isoformat(),
        "roots": list(roots),
        "files": iter_files(target_root, roots),
    }


def write_manifest(
    target_root: Path,
    skill_name: str,
    metadata: dict[str, str],
) -> Path:
    manifest_path = target_root / skill_name / PROVENANCE_NAME
    manifest = build_manifest(target_root, skill_name, metadata)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest_path


def verify_manifest(target_root: Path, skill_name: str) -> dict[str, object]:
    manifest_path = target_root / skill_name / PROVENANCE_NAME
    if not manifest_path.is_file():
        return {"state": "missing", "skill_name": skill_name, "issues": ["缺少来源清单"]}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {
            "state": "mismatch",
            "skill_name": skill_name,
            "issues": [f"来源清单不可读: {exc}"],
        }

    issues: list[str] = []
    if manifest.get("schema_version") != 1:
        issues.append("schema_version 必须为 1")
    if manifest.get("skill_name") != skill_name:
        issues.append("skill_name 不匹配")
    roots = manifest.get("roots")
    files = manifest.get("files")
    if not isinstance(roots, list) or not all(isinstance(item, str) for item in roots):
        issues.append("roots 必须是字符串列表")
        roots = []
    if not isinstance(files, dict) or not all(
        isinstance(path, str) and isinstance(value, str)
        for path, value in (files.items() if isinstance(files, dict) else ())
    ):
        issues.append("files 必须是路径到 SHA-256 的映射")
        files = {}

    actual: dict[str, str] = {}
    if roots:
        try:
            actual = iter_files(target_root, roots)
        except (OSError, RuntimeError) as exc:
            issues.append(str(exc))

    expected_paths = set(files)
    actual_paths = set(actual)
    for missing in sorted(expected_paths - actual_paths):
        issues.append(f"缺少安装文件: {missing}")
    for extra in sorted(actual_paths - expected_paths):
        issues.append(f"存在清单外文件: {extra}")
    for path in sorted(expected_paths & actual_paths):
        if files[path] != actual[path]:
            issues.append(f"SHA-256 不匹配: {path}")

    required_metadata = ("source_repository", "source_branch", "source_commit")
    for field in required_metadata:
        value = manifest.get(field)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"缺少来源字段: {field}")

    return {
        "state": "verified" if not issues else "mismatch",
        "skill_name": skill_name,
        "source_repository": manifest.get("source_repository"),
        "source_branch": manifest.get("source_branch"),
        "source_commit": manifest.get("source_commit"),
        "file_count": len(files),
        "issues": issues,
    }


def install(
    source_root: Path,
    target_root: Path,
    skills: Iterable[str],
    metadata: dict[str, str],
) -> list[dict[str, object]]:
    selected = tuple(dict.fromkeys(skills))
    unknown = [name for name in selected if name not in CALLABLE_DEPENDENCIES]
    if unknown:
        raise ValueError(f"未知 Skill: {', '.join(unknown)}")

    roots: list[str] = []
    for skill_name in selected:
        for root_name in CALLABLE_DEPENDENCIES[skill_name]:
            if root_name not in roots:
                roots.append(root_name)

    target_root.mkdir(parents=True, exist_ok=True)
    for root_name in roots:
        mirror_directory(source_root / root_name, target_root / root_name)

    for skill_name in selected:
        write_manifest(target_root, skill_name, metadata)

    results = [verify_manifest(target_root, name) for name in selected]
    failed = [item for item in results if item["state"] != "verified"]
    if failed:
        raise RuntimeError(json.dumps(failed, ensure_ascii=False, indent=2))
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=REPO_ROOT)
    parser.add_argument(
        "--target-root",
        type=Path,
        default=Path.home() / ".codex" / "skills",
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        choices=sorted(CALLABLE_DEPENDENCIES),
        default=sorted(CALLABLE_DEPENDENCIES),
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    target_root = args.target_root.resolve()

    if args.verify_only:
        results = [verify_manifest(target_root, name) for name in args.skills]
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0 if all(item["state"] == "verified" for item in results) else 1

    if not args.apply:
        print("未指定 --apply；未修改安装目录。", file=sys.stderr)
        return 2

    metadata = git_metadata(source_root)
    results = install(source_root, target_root, args.skills, metadata)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
