#!/usr/bin/env python3
"""验证三个项目文档 Skill 的显式调用和轻量包装边界。"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_NAMES = (
    "project-doc-skeleton",
    "project-doc-consistency",
    "project-doc-contraction",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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
                self.assertFalse((skill_root / "assets").exists())
                self.assertFalse((skill_root / "references").exists())

    def test_no_shared_runtime_package(self) -> None:
        self.assertFalse((ROOT / "project-doc-shared").exists())


if __name__ == "__main__":
    unittest.main()
