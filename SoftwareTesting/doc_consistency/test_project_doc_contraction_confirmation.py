#!/usr/bin/env python3
"""机械检查内容收缩 Skill 的单次前置确认和骨架 Skill 独立分流。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACTION_SKILL = Path("project-doc-contraction/SKILL.md")
CONTRACTION_AGENT = Path("project-doc-contraction/agents/openai.yaml")
SKELETON_SKILL = Path("project-doc-skeleton/SKILL.md")
SKELETON_AGENT = Path("project-doc-skeleton/agents/openai.yaml")

CONTRACTION_REQUIRED = (
    "用只读 Git 取得当前 `HEAD` 的完整 SHA",
    "默认使用 `full` 与只读报告",
    "随后只问一次",
    "回复“确认”即可",
    "不要求用户粘贴验证日志",
    "缺少验证日志本身不是阻断理由",
    "不得再单独追问基线、范围或交付路线",
    "默认“两轮、不生成”",
)

CONTRACTION_AGENT_REQUIRED = (
    "当前 HEAD",
    "只问一句",
    "回复“确认”即可",
    "不索要验证证据",
    "默认两轮、不生成反哺",
)

OBSOLETE_BURDENS = (
    "明确列出仍为 `not_run` 但不影响内容真值的边界",
    "未明确基线／交付路线时，先询问缺失项",
)

SKELETON_REQUIRED = (
    "这次只要检查报告，还是检查后形成方案",
    "一个白话问题",
    "不要调用、依赖或假定其他 Skill 已安装",
)


def read_text(root: Path, relative: Path) -> str:
    path = root / relative
    if not path.is_file():
        raise AssertionError(f"缺少文件: {relative.as_posix()}")
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return "".join(text.split())


def collect_issues(root: Path) -> list[str]:
    contraction = read_text(root, CONTRACTION_SKILL)
    contraction_agent = read_text(root, CONTRACTION_AGENT)
    skeleton = read_text(root, SKELETON_SKILL)
    skeleton_agent = read_text(root, SKELETON_AGENT)

    contraction_compact = compact(contraction)
    contraction_agent_compact = compact(contraction_agent)
    skeleton_compact = compact(skeleton)

    issues: list[str] = []
    for token in CONTRACTION_REQUIRED:
        if compact(token) not in contraction_compact:
            issues.append(f"{CONTRACTION_SKILL.as_posix()}: 缺少 {token!r}")
    for token in CONTRACTION_AGENT_REQUIRED:
        if compact(token) not in contraction_agent_compact:
            issues.append(f"{CONTRACTION_AGENT.as_posix()}: 缺少 {token!r}")
    for token in OBSOLETE_BURDENS:
        if compact(token) in contraction_compact:
            issues.append(f"{CONTRACTION_SKILL.as_posix()}: 仍保留旧多字段负担 {token!r}")
    for token in SKELETON_REQUIRED:
        if compact(token) not in skeleton_compact:
            issues.append(f"{SKELETON_SKILL.as_posix()}: 缺少既有独立分流合同 {token!r}")

    if "allow_implicit_invocation: false" not in contraction_agent:
        issues.append(f"{CONTRACTION_AGENT.as_posix()}: 必须禁止隐式调用")
    if "allow_implicit_invocation: false" not in skeleton_agent:
        issues.append(f"{SKELETON_AGENT.as_posix()}: 必须禁止隐式调用")
    if "不索要验证证据" in skeleton or "当前 HEAD" in skeleton_agent:
        issues.append("project-doc-skeleton: 不得继承 contraction 的一致性前置交互")

    return issues


class ProjectDocContractionConfirmationTest(unittest.TestCase):
    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], collect_issues(ROOT))

    def test_old_five_field_prompt_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for relative in (
                CONTRACTION_SKILL,
                CONTRACTION_AGENT,
                SKELETON_SKILL,
                SKELETON_AGENT,
            ):
                source = ROOT / relative
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    source.read_text(encoding="utf-8"),
                    encoding="utf-8",
                    newline="\n",
                )

            path = root / CONTRACTION_SKILL
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                "不要求用户粘贴验证日志、命令输出、审阅包或 `not_run` 清单",
                "要求用户明确列出仍为 `not_run` 但不影响内容真值的边界",
                1,
            )
            path.write_text(text, encoding="utf-8", newline="\n")

            issues = collect_issues(root)
            self.assertTrue(
                any("旧多字段负担" in issue for issue in issues),
                issues,
            )

    def test_skeleton_keeps_its_existing_route_question(self) -> None:
        skeleton = read_text(ROOT, SKELETON_SKILL)
        self.assertIn("这次只要检查报告，还是检查后形成方案", skeleton)
        self.assertNotIn("不索要验证证据", skeleton)


if __name__ == "__main__":
    unittest.main()
