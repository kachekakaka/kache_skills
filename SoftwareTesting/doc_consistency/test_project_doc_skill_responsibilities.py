#!/usr/bin/env python3
"""机械检查项目文档 Skill 的职责隔离和方案不混合合同。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKELETON_PATH = Path("project-doc-skeleton/SKILL.md")
SKELETON_AGENT_PATH = Path("project-doc-skeleton/agents/openai.yaml")
CONSISTENCY_PATH = Path("project-doc-consistency/SKILL.md")
CONSISTENCY_AGENT_PATH = Path("project-doc-consistency/agents/openai.yaml")
TEST_CONTRACT_PATH = Path(
    "project-doc-consistency/references/test-design-audit.md"
)
CONTRACTION_PATH = Path("project-doc-contraction/SKILL.md")
CONTRACTION_AGENT_PATH = Path("project-doc-contraction/agents/openai.yaml")
SHARED_PROTOCOL_PATH = Path(
    "project-doc-shared/references/long-audit-protocol.md"
)
SHARED_VALIDATION_PATH = Path(
    "project-doc-shared/references/validation-planning.md"
)
SPLIT_ADR_PATH = Path(
    "docs/adr/0012-separate-content-consistency-and-contraction-skills.md"
)
OBSOLETE_CONSISTENCY_REFERENCES = (
    Path("project-doc-consistency/references/content-contraction.md"),
    Path("project-doc-consistency/references/validation-planning.md"),
)

SHARED_PROTOCOL_LINK = (
    "../project-doc-shared/references/long-audit-protocol.md"
)
SHARED_VALIDATION_LINK = (
    "../project-doc-shared/references/validation-planning.md"
)

CONTRACTION_ACTION_MARKERS = (
    "删除重复正文",
    "迁移内容",
    "摘要加链接",
    "合并段落",
    "简化表达",
)
CONSISTENCY_ACTION_MARKERS = (
    "修正事实",
    "校准状态",
    "同步 Registry",
    "澄清直接消费者",
)


def read_required(root: Path, relative: Path, issues: list[str]) -> str:
    path = root / relative
    if not path.is_file():
        issues.append(f"{relative.as_posix()}: 缺少必需文件")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeError:
        issues.append(f"{relative.as_posix()}: 必须是有效 UTF-8")
        return ""


def extract_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    next_heading = text.find("\n## ", start)
    return text[start:] if next_heading < 0 else text[start:next_heading]


def require_tokens(
    issues: list[str],
    label: str,
    text: str,
    tokens: tuple[str, ...],
) -> None:
    compact = " ".join(text.split())
    for token in tokens:
        if " ".join(token.split()) not in compact:
            issues.append(f"{label}: 缺少职责合同 {token!r}")


def validate_plan_scope(role: str, plan_text: str) -> list[str]:
    has_contraction = any(
        marker in plan_text for marker in CONTRACTION_ACTION_MARKERS
    )
    has_consistency = any(
        marker in plan_text for marker in CONSISTENCY_ACTION_MARKERS
    )
    issues: list[str] = []
    if has_contraction and has_consistency:
        issues.append("同一方案混合一致性修正和内容收缩动作")
    if role == "consistency" and has_contraction:
        issues.append("一致性方案包含删除、迁移、链接、合并或简化动作")
    if role == "contraction" and has_consistency:
        issues.append("收缩方案包含事实、状态、Registry 或消费者修正")
    return issues


def collect_contract_issues(root: Path) -> list[str]:
    issues: list[str] = []
    skeleton = ""
    skeleton_agent = ""
    if (root / SKELETON_PATH).is_file() or (root / SKELETON_AGENT_PATH).is_file():
        skeleton = read_required(root, SKELETON_PATH, issues)
        skeleton_agent = read_required(root, SKELETON_AGENT_PATH, issues)
    consistency = read_required(root, CONSISTENCY_PATH, issues)
    consistency_agent = read_required(
        root, CONSISTENCY_AGENT_PATH, issues
    )
    test_contract = read_required(root, TEST_CONTRACT_PATH, issues)
    contraction = read_required(root, CONTRACTION_PATH, issues)
    contraction_agent = read_required(
        root, CONTRACTION_AGENT_PATH, issues
    )
    shared = read_required(root, SHARED_PROTOCOL_PATH, issues)
    shared_validation = read_required(
        root, SHARED_VALIDATION_PATH, issues
    )
    split_adr = read_required(root, SPLIT_ADR_PATH, issues)
    if issues:
        return issues

    if skeleton:
        require_tokens(
            issues,
            SKELETON_PATH.as_posix(),
            skeleton,
            (
                "name: project-doc-skeleton",
                "仅在用户显式调用 $project-doc-skeleton",
                "不要调用、依赖或假定其他 Skill 已安装",
            ),
        )
    require_tokens(
        issues,
        CONSISTENCY_PATH.as_posix(),
        consistency,
        (
            "name: project-doc-consistency",
            "仅在用户显式调用 $project-doc-consistency",
            "本 Skill **不负责内容收缩**",
            "`后续收缩候选`",
            SHARED_PROTOCOL_LINK,
            SHARED_VALIDATION_LINK,
            "一致性方案只能包含事实、契约、状态、所有权",
            "不得形成删除重复正文、迁移内容、摘要加链接、合并、简化",
            "所有文档级 `一致` 结论",
            "防语义误改轮",
            "不得自动调用 `project-doc-contraction`",
        ),
    )
    require_tokens(
        issues,
        TEST_CONTRACT_PATH.as_posix(),
        test_contract,
        (
            "测试契约一致性参考",
            "不评价测试数量是否足够",
            "不做覆盖率、重复测试经济性或测试资产内容收缩",
            "不能以",
            "删除测试",
            "`后续收缩候选`",
        ),
    )
    require_tokens(
        issues,
        CONTRACTION_PATH.as_posix(),
        contraction,
        (
            "name: project-doc-contraction",
            "仅在用户显式调用 $project-doc-contraction",
            "必要前置：一致性基线",
            "不可变提交 SHA",
            "`consistency_blocked`",
            "不得自行决定哪一方正确",
            SHARED_PROTOCOL_LINK,
            SHARED_VALIDATION_LINK,
            "收缩方案只能包含内容删除、迁移、摘要加链接、合并或简化",
            "不得包含当前事实、",
            "全部 `无需收缩` 文档",
            "防误伤轮",
            "不得自动调用",
        ),
    )
    require_tokens(
        issues,
        SHARED_PROTOCOL_PATH.as_posix(),
        shared,
        (
            "`S000`",
            "`Axxx`",
            "`Cnnn`",
            "累计可恢复尾部",
            "不能只依赖不可见内部记忆",
            "最终索引",
            "不允许一个 Skill 自动调用另一个 Skill",
        ),
    )
    require_tokens(
        issues,
        SPLIT_ADR_PATH.as_posix(),
        split_adr,
        (
            "将内容一致性与内容收缩拆为两个显式 Skill",
            "部分替代 ADR-0008",
            "一致性方案与收缩方案不得混合",
        ),
    )
    require_tokens(
        issues,
        SHARED_VALIDATION_PATH.as_posix(),
        shared_validation,
        (
            "`project-doc-consistency` 与 `project-doc-contraction`",
            "原范围消费者漂移",
            "临时环境阻断",
            "新的范围问题",
            "`not_run`",
        ),
    )

    if "文档级 `无需收缩`" in consistency or "形成 `需要收缩`" in consistency:
        issues.append(
            f"{CONSISTENCY_PATH.as_posix()}: 不得恢复内容收缩文档处置"
        )
    if "content-contraction.md" in consistency:
        issues.append(
            f"{CONSISTENCY_PATH.as_posix()}: 不得加载内容收缩 reference"
        )
    for marker in ("冗余候选", "过度候选", "判断覆盖、重叠与成本"):
        if marker in test_contract:
            issues.append(
                f"{TEST_CONTRACT_PATH.as_posix()}: 不得恢复测试经济性或删除候选 {marker!r}"
            )
    if "事实／契约遍" in contraction or "测试设计" in contraction:
        issues.append(
            f"{CONTRACTION_PATH.as_posix()}: 不得恢复一致性或测试设计审计"
        )
    if any(
        token in shared
        for token in (
            "需要收缩",
            "无需收缩",
            "需要修正",
            "事实／契约遍",
        )
    ):
        issues.append(
            f"{SHARED_PROTOCOL_PATH.as_posix()}: 共享协议不得拥有业务处置"
        )

    consistency_plan = extract_section(consistency, "方案隔离")
    contraction_plan = extract_section(contraction, "方案隔离")
    if not consistency_plan:
        issues.append(
            f"{CONSISTENCY_PATH.as_posix()}: 缺少“方案隔离”章节"
        )
    if not contraction_plan:
        issues.append(
            f"{CONTRACTION_PATH.as_posix()}: 缺少“方案隔离”章节"
        )

    if skeleton_agent and "allow_implicit_invocation: false" not in skeleton_agent:
        issues.append(
            f"{SKELETON_AGENT_PATH.as_posix()}: 必须禁止隐式调用"
        )
    if "allow_implicit_invocation: false" not in consistency_agent:
        issues.append(
            f"{CONSISTENCY_AGENT_PATH.as_posix()}: 必须禁止隐式调用"
        )
    if "allow_implicit_invocation: false" not in contraction_agent:
        issues.append(
            f"{CONTRACTION_AGENT_PATH.as_posix()}: 必须禁止隐式调用"
        )
    if "不要做内容收缩" not in consistency_agent:
        issues.append(
            f"{CONSISTENCY_AGENT_PATH.as_posix()}: 默认提示必须隔离收缩"
        )
    if "已经完成一致性整改与验证的基线提交" not in contraction_agent:
        issues.append(
            f"{CONTRACTION_AGENT_PATH.as_posix()}: 默认提示必须要求一致性基线"
        )

    for relative in OBSOLETE_CONSISTENCY_REFERENCES:
        if (root / relative).exists():
            issues.append(
                f"{relative.as_posix()}: 旧收缩／验证 reference 必须退出 consistency"
            )
    if (root / "project-doc-shared/SKILL.md").exists():
        issues.append("project-doc-shared/: 共享支持目录不得成为可调用 Skill")

    return issues


class ProjectDocSkillResponsibilityTest(unittest.TestCase):
    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], collect_contract_issues(ROOT))

    def test_consistency_must_not_generate_contraction_actions(self) -> None:
        issues = validate_plan_scope(
            "consistency",
            "修正事实并删除重复正文，再简化表达。",
        )
        self.assertIn(
            "一致性方案包含删除、迁移、链接、合并或简化动作",
            issues,
        )
        self.assertIn(
            "同一方案混合一致性修正和内容收缩动作",
            issues,
        )

    def test_contraction_must_not_decide_fact_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary)
            for relative in (
                SKELETON_PATH,
                SKELETON_AGENT_PATH,
                CONSISTENCY_PATH,
                CONSISTENCY_AGENT_PATH,
                TEST_CONTRACT_PATH,
                CONTRACTION_PATH,
                CONTRACTION_AGENT_PATH,
                SHARED_PROTOCOL_PATH,
                SHARED_VALIDATION_PATH,
                SPLIT_ADR_PATH,
            ):
                source = ROOT / relative
                if not source.is_file():
                    continue
                target = fixture / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    source.read_text(encoding="utf-8"),
                    encoding="utf-8",
                    newline="\n",
                )
            path = fixture / CONTRACTION_PATH
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                "不得自行决定哪一方正确",
                "选择看起来更新的一方作为正确结果",
                1,
            )
            path.write_text(text, encoding="utf-8", newline="\n")

            issues = collect_contract_issues(fixture)
            self.assertTrue(
                any("不得自行决定哪一方正确" in issue for issue in issues),
                issues,
            )

    def test_mixed_contraction_plan_is_rejected(self) -> None:
        issues = validate_plan_scope(
            "contraction",
            "迁移内容，并同步 Registry 与校准状态。",
        )
        self.assertIn(
            "收缩方案包含事实、状态、Registry 或消费者修正",
            issues,
        )
        self.assertIn(
            "同一方案混合一致性修正和内容收缩动作",
            issues,
        )


if __name__ == "__main__":
    unittest.main()
