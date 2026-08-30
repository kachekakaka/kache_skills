#!/usr/bin/env python3
"""只读检查本仓库非历史 Markdown 中的本地链接和标题锚点。"""

from __future__ import annotations

import re
import tempfile
import unicodedata
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^)\s]+)(?:\s+[^)]*)?\)"
)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")


def strip_fenced_code(text: str) -> str:
    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        marker = "```" if stripped.startswith("```") else "~~~" if stripped.startswith("~~~") else None
        if marker:
            fence = None if fence == marker else marker if fence is None else fence
            output.append("\n" if line.endswith(("\n", "\r")) else "")
        elif fence is None:
            output.append(line)
        else:
            output.append("\n" if line.endswith(("\n", "\r")) else "")
    return "".join(output)


def heading_slug(heading: str) -> str:
    value = re.sub(r"<[^>]+>", "", heading)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").lower()
    kept: list[str] = []
    for char in value:
        category = unicodedata.category(char)
        if char in (" ", "-") or category[0] in ("L", "N", "M"):
            kept.append(char)
    return re.sub(r"\s+", "-", "".join(kept))


def heading_slugs(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    result: set[str] = set()
    text = strip_fenced_code(path.read_text(encoding="utf-8"))
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = heading_slug(match.group(1))
        index = seen.get(base, 0)
        result.add(base if index == 0 else f"{base}-{index}")
        seen[base] = index + 1
    return result


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] == "archive":
            continue
        if any(part in {".git", "__pycache__"} for part in relative.parts):
            continue
        files.append(path)
    return sorted(files)


def check_repository(root: Path) -> list[str]:
    root = root.resolve()
    issues: list[str] = []
    for source in markdown_files(root):
        relative_source = source.relative_to(root).as_posix()
        try:
            text = strip_fenced_code(source.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            issues.append(f"{relative_source}: 无法读取 UTF-8 Markdown: {exc}")
            continue

        for match in LINK_RE.finditer(text):
            destination = match.group(1).strip()
            if destination.startswith("<") and destination.endswith(">"):
                destination = destination[1:-1]
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue

            path_text = unquote(parsed.path)
            target = source if not path_text else (source.parent / path_text).resolve()
            if not target.is_relative_to(root):
                issues.append(f"{relative_source}: 本地链接越出仓库: {destination}")
                continue
            if not target.exists():
                issues.append(f"{relative_source}: 链接目标不存在: {destination}")
                continue

            fragment = unquote(parsed.fragment).lower()
            if fragment and target.is_file() and target.suffix.lower() == ".md":
                try:
                    slugs = heading_slugs(target)
                except (OSError, UnicodeError) as exc:
                    issues.append(
                        f"{relative_source}: 无法读取链接目标 {destination}: {exc}"
                    )
                    continue
                if fragment not in slugs:
                    issues.append(f"{relative_source}: 标题锚点不存在: {destination}")
    return issues


class MarkdownLinkCheckerTest(unittest.TestCase):
    def test_valid_local_link_and_external_link(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "README.md").write_text(
                "# 入口\n\n[说明](docs/guide.md#章节)\n[外链](https://example.invalid)\n",
                encoding="utf-8",
                newline="\n",
            )
            (root / "docs/guide.md").write_text(
                "# 说明\n\n## 章节\n",
                encoding="utf-8",
                newline="\n",
            )
            self.assertEqual([], check_repository(root))

    def test_missing_target_and_anchor_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "# 入口\n\n[缺文件](missing.md)\n[缺标题](#absent)\n",
                encoding="utf-8",
                newline="\n",
            )
            issues = check_repository(root)
            self.assertTrue(any("链接目标不存在" in issue for issue in issues), issues)
            self.assertTrue(any("标题锚点不存在" in issue for issue in issues), issues)


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(MarkdownLinkCheckerTest)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        return 1

    issues = check_repository(ROOT)
    if issues:
        for issue in issues:
            print(issue)
        return 1
    print("本仓库非历史 Markdown 本地链接检查通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
