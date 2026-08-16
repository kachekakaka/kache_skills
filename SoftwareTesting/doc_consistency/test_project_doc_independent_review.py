#!/usr/bin/env python3
"""机械检查独立方案审阅、双向候选和失效证据合同。"""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def compact(text: str) -> str:
    return "".join(text.split())


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"缺少文件: {relative}")
    return path.read_text(encoding="utf-8")


def assess(
    *,
    audit_complete: bool,
    independent_context: bool,
    unresolved_candidates: int = 0,
    invalidated_evidence_reused: bool = False,
    stale_fact_action: bool = False,
) -> str:
    if not audit_complete:
        return "blocked"
    if not independent_context:
        return "needs_revision"
    if unresolved_candidates or invalidated_evidence_reused or stale_fact_action:
        return "needs_revision"
    return "implementation_ready"


class ProjectDocIndependentReviewTest(unittest.TestCase):
    def test_repository_contracts_pass(self) -> None:
        consistency = compact(read("project-doc-consistency/SKILL.md"))
        contraction = compact(read("project-doc-contraction/SKILL.md"))
        counter = compact(
            read("project-doc-consistency/references/counterevidence-audit.md")
        )
        content = compact(
            read("project-doc-contraction/references/content-contraction.md")
        )
        long_protocol = compact(
            read("project-doc-shared/references/long-audit-protocol.md")
        )
        review = compact(
            read("project-doc-shared/references/independent-plan-review.md")
        )
        shared_readme = compact(read("project-doc-shared/README.md"))
        consistency_agent = compact(
            read("project-doc-consistency/agents/openai.yaml")
        )
        contraction_agent = compact(
            read("project-doc-contraction/agents/openai.yaml")
        )
        requirements = compact(read("docs/需求文档.md"))
        design = compact(read("docs/设计文档.md"))
        testing = compact(read("SoftwareTesting/doc_consistency/README.md"))

        for token in (
            "独立审阅一份已经保存的一致性方案",
            "implementation_ready",
            "needs_revision",
            "independent-plan-review.md",
        ):
            self.assertIn(compact(token), consistency)
        for token in (
            "独立审阅一份已经保存的收缩方案",
            "implementation_ready",
            "independent-plan-review.md",
        ):
            self.assertIn(compact(token), contraction)
        for token in (
            "双向清单",
            "候选编号与闭环",
            "不得用“扫描完成、无新发现”",
        ):
            self.assertIn(compact(token), counter)
        for token in (
            "过时事实删除门",
            "已经过时",
            "默认`consistency_blocked`",
        ):
            self.assertIn(compact(token), content)
        for token in (
            "audit_complete",
            "implementation_ready",
            "原审计任务不得自行",
            "失效的证据",
            "静默引用",
        ):
            self.assertIn(compact(token), long_protocol)
        for token in (
            "不继承原任务的完整性或防误伤结论",
            "四类双向清单",
            "过时事实删除门",
            "失效证据",
        ):
            self.assertIn(compact(token), review)
        self.assertIn("independent-plan-review.md", shared_readme)
        self.assertIn("implementation_ready", consistency_agent)
        self.assertIn("过时事实删除", contraction_agent)
        self.assertIn("audit_complete", requirements)
        self.assertIn("independent-plan-review.md", design)
        self.assertIn("test_project_doc_independent_review.py", testing)

    def test_original_task_cannot_self_approve(self) -> None:
        self.assertEqual(
            "needs_revision",
            assess(audit_complete=True, independent_context=False),
        )

    def test_unclosed_candidate_is_rejected(self) -> None:
        self.assertEqual(
            "needs_revision",
            assess(
                audit_complete=True,
                independent_context=True,
                unresolved_candidates=1,
            ),
        )

    def test_stale_fact_delete_and_invalid_evidence_are_rejected(self) -> None:
        self.assertEqual(
            "needs_revision",
            assess(
                audit_complete=True,
                independent_context=True,
                stale_fact_action=True,
            ),
        )
        self.assertEqual(
            "needs_revision",
            assess(
                audit_complete=True,
                independent_context=True,
                invalidated_evidence_reused=True,
            ),
        )

    def test_corrected_plan_can_be_ready(self) -> None:
        self.assertEqual(
            "implementation_ready",
            assess(audit_complete=True, independent_context=True),
        )


if __name__ == "__main__":
    unittest.main()
