#!/usr/bin/env python3
"""验证项目文档 Skill 独立镜像安装和来源清单。"""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INSTALLER_PATH = ROOT / "SoftwareTesting/doc_consistency/install_project_doc_skills.py"

SPEC = importlib.util.spec_from_file_location("project_doc_skill_installer", INSTALLER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"无法加载安装器: {INSTALLER_PATH}")
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)

SUPPORTED_SKILLS = (
    "project-doc-consistency",
    "project-doc-contraction",
    "project-doc-skeleton",
)


def make_skill(source: Path, name: str) -> None:
    (source / name / "agents").mkdir(parents=True)
    (source / name / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: test\n---\n",
        encoding="utf-8",
        newline="\n",
    )
    (source / name / "agents/openai.yaml").write_text(
        "policy:\n  allow_implicit_invocation: false\n",
        encoding="utf-8",
        newline="\n",
    )


METADATA = {
    "source_repository": "https://example.invalid/repo.git",
    "source_branch": "main",
    "source_commit": "a" * 40,
}


class ProjectDocSkillInstallerTest(unittest.TestCase):
    def test_exact_independent_mirror_and_provenance(self) -> None:
        for skill_name in SUPPORTED_SKILLS:
            with self.subTest(skill=skill_name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                source = root / "source"
                target = root / "target"
                make_skill(source, skill_name)
                (target / skill_name).mkdir(parents=True)
                (target / skill_name / "stale.txt").write_text(
                    "stale\n", encoding="utf-8"
                )

                results = INSTALLER.install(source, target, (skill_name,), METADATA)

                self.assertEqual("verified", results[0]["state"])
                self.assertFalse((target / skill_name / "stale.txt").exists())
                self.assertEqual(
                    [skill_name],
                    sorted(path.name for path in target.iterdir() if path.is_dir()),
                )
                manifest_path = target / skill_name / "SOURCE-PROVENANCE.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual([skill_name], manifest["roots"])

    def test_modified_installed_file_is_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            target = root / "target"
            skill_name = "project-doc-consistency"
            make_skill(source, skill_name)
            INSTALLER.install(source, target, (skill_name,), METADATA)
            (target / skill_name / "SKILL.md").write_text(
                "changed\n", encoding="utf-8", newline="\n"
            )

            result = INSTALLER.verify_manifest(target, skill_name)

            self.assertEqual("mismatch", result["state"])
            self.assertTrue(
                any("SHA-256 不匹配" in issue for issue in result["issues"]),
                result,
            )

    def test_missing_manifest_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = INSTALLER.verify_manifest(
                Path(temporary), "project-doc-consistency"
            )
            self.assertEqual("missing", result["state"])


if __name__ == "__main__":
    unittest.main()
