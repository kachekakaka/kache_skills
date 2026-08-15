#!/usr/bin/env python3
"""机械检查一致性反证扫描、评审证据和来源身份合同。"""

from __future__ import annotations

import unittest
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = Path("project-doc-consistency/SKILL.md")
REFERENCE_PATH = Path(
    "project-doc-consistency/references/counterevidence-audit.md"
)
SHARED_PATH = Path("project-doc-shared/references/long-audit-protocol.md")
AGENT_PATH = Path("project-doc-consistency/agents/openai.yaml")

R1_REQUIRED_FIELDS = (
    "path",
    "claim",
    "initial_evidence",
    "counter_evidence",
    "result",
    "reason",
)
R2_REQUIRED_FIELDS = (
    "action",
    "product_semantics",
    "permission_or_security",
    "test_selection",
    "runtime_behavior",
    "historical_decision",
    "direct_consumer",
    "result",
)


def read_text(relative: Path) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"缺少文件: {relative.as_posix()}")
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return "".join(text.split())


def validate_r1(
    expected_paths: Iterable[str],
    records: list[dict[str, str]],
) -> list[str]:
    issues: list[str] = []
    expected = tuple(expected_paths)
    actual = tuple(record.get("path", "") for record in records)
    if set(actual) != set(expected) or len(actual) != len(expected):
        issues.append("第一轮没有逐份覆盖固定文档集合")
    for record in records:
        path = record.get("path", "<unknown>")
        for field in R1_REQUIRED_FIELDS:
            if not record.get(field, "").strip():
                issues.append(f"{path}: 缺少 R001 字段 {field}")
        if record.get("initial_evidence") == record.get("counter_evidence"):
            issues.append(f"{path}: 相反证据不得复用初审正向证据")
        if record.get("result") not in {"改变", "未改变"}:
            issues.append(f"{path}: result 必须是改变或未改变")
    return issues


def validate_r2(
    expected_actions: Iterable[str],
    records: list[dict[str, str]],
) -> list[str]:
    issues: list[str] = []
    expected = tuple(expected_actions)
    actual = tuple(record.get("action", "") for record in records)
    if set(actual) != set(expected) or len(actual) != len(expected):
        issues.append("第二轮没有逐项覆盖固定动作集合")
    for record in records:
        action = record.get("action", "<unknown>")
        for field in R2_REQUIRED_FIELDS:
            if not record.get(field, "").strip():
                issues.append(f"{action}: 缺少 R002 字段 {field}")
        if record.get("result") not in {"通过", "修改", "撤销"}:
            issues.append(f"{action}: result 必须是通过、修改或撤销")
    return issues


class ProjectDocConsistencyCounterevidenceTest(unittest.TestCase):
    def test_repository_contracts_pass(self) -> None:
        skill = compact(read_text(SKILL_PATH))
        reference = compact(read_text(REFERENCE_PATH))
        shared = compact(read_text(SHARED_PATH))
        agent = compact(read_text(AGENT_PATH))

        required_skill = (
            "SOURCE-PROVENANCE.json",
            "verified",
            "missing",
            "mismatch",
            "references/counterevidence-audit.md",
            "四类跨载体扫描",
            "可证伪主张",
            "初审正向证据",
            "不同角色的相反证据或邻接消费者",
            "仓库外正式轨迹",
            "不得询问保存",
        )
        required_reference = (
            "初始状态与运行时转换",
            "允许、禁止、退役合同与夹具",
            "聚合入口与成员闭包",
            "身份与操作粒度",
            "数量相同不能代替成员闭包",
            "同一source／lease／snapshot",
            "N/N不变",
            "失败关闭",
        )
        required_shared = (
            "用户明确授权",
            "仓库外正式轨迹",
            "逐字追加",
            "不得事后补造",
        )
        required_agent = (
            "四类跨载体反证扫描",
            "逐文档反证式Rxxx",
            "SOURCE-PROVENANCE.json",
        )
        for token in required_skill:
            self.assertIn(compact(token), skill, token)
        for token in required_reference:
            self.assertIn(compact(token), reference, token)
        for token in required_shared:
            self.assertIn(compact(token), shared, token)
        for token in required_agent:
            self.assertIn(compact(token), agent, token)

    def test_grouped_or_self_confirming_r1_is_rejected(self) -> None:
        issues = validate_r1(
            ("S001", "S002"),
            [
                {
                    "path": "S001-S002",
                    "claim": "全部一致",
                    "initial_evidence": "README",
                    "counter_evidence": "README",
                    "result": "未改变",
                    "reason": "2/2 不变",
                }
            ],
        )
        self.assertTrue(
            any("逐份覆盖" in issue for issue in issues),
            issues,
        )
        self.assertTrue(
            any("不得复用" in issue for issue in issues),
            issues,
        )

    def test_per_document_adversarial_r1_is_accepted(self) -> None:
        issues = validate_r1(
            ("S001", "S002"),
            [
                {
                    "path": "S001",
                    "claim": "启动时选择后运行期不可切换",
                    "initial_evidence": "需求表",
                    "counter_evidence": "运行时切换 API",
                    "result": "改变",
                    "reason": "直接消费者允许双向热切换",
                },
                {
                    "path": "S002",
                    "claim": "run-all 调度全部声明成员",
                    "initial_evidence": "命令表",
                    "counter_evidence": "实际调度函数",
                    "result": "未改变",
                    "reason": "声明成员与实际调用闭包一致",
                },
            ],
        )
        self.assertEqual([], issues)

    def test_r2_requires_each_safety_axis(self) -> None:
        issues = validate_r2(
            ("F001",),
            [
                {
                    "action": "F001",
                    "product_semantics": "不变",
                    "permission_or_security": "",
                    "test_selection": "不变",
                    "runtime_behavior": "不变",
                    "historical_decision": "不变",
                    "direct_consumer": "README",
                    "result": "通过",
                }
            ],
        )
        self.assertTrue(
            any("permission_or_security" in issue for issue in issues),
            issues,
        )


if __name__ == "__main__":
    unittest.main()
