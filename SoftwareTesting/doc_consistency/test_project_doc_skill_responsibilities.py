#!/usr/bin/env python3
"""验证三个项目文档 Skill 的显式调用和轻量包装边界。"""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SKILL_NAMES = (
    "project-doc-skeleton",
    "project-doc-consistency",
    "project-doc-contraction",
)
LINK_RE = re.compile(r"\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^)\s]+)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def local_link_paths(text: str) -> list[str]:
    result: list[str] = []
    for match in LINK_RE.finditer(text):
        destination = match.group(1).strip()
        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1]
        parsed = urlsplit(destination)
        if not parsed.scheme and not parsed.netloc and parsed.path:
            result.append(unquote(parsed.path))
    return result


class ProjectDocSkillPackagingTest(unittest.TestCase):
    def test_packages_are_explicit_and_self_contained(self) -> None:
        for name in SKILL_NAMES:
            with self.subTest(skill=name):
                skill_root = ROOT / name
                skill_text = read(skill_root / "SKILL.md")
                agent_text = read(skill_root / "agents/openai.yaml")

                self.assertRegex(skill_text, rf"(?m)^name:\s*{re.escape(name)}\s*$")
                self.assertIn(f"${name}", skill_text.split("---", 2)[1])
                self.assertIn(f"${name}", agent_text)
                self.assertRegex(
                    agent_text,
                    r"(?m)^\s*allow_implicit_invocation:\s*false\s*$",
                )
                for relative in local_link_paths(skill_text):
                    target = (skill_root / relative).resolve()
                    self.assertTrue(
                        target.is_relative_to(skill_root.resolve()),
                        f"{name} 运行入口引用包外路径: {relative}",
                    )
                    self.assertTrue(target.exists(), f"{name} 缺少本地依赖: {relative}")


if __name__ == "__main__":
    unittest.main()
