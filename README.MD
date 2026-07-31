# kache_skills

本仓库用于开发和验证个人 Skill。仓库中的 Skill 在完成结构校验、脚本测试和真实项目正向验证前，
不应安装到个人 Skills 目录或用于批量修改项目。

## project-doc-skeleton

[`project-doc-skeleton`](project-doc-skeleton/SKILL.md) 的中文显示名为“项目文档骨架管理”。

它只负责单一上下文项目的：

- 固定与条件目录；
- 文档入口和实际链接可达性；
- 已确认的路径职责与承接位置；
- 待办、方案和归档生命周期；
- 测试治理结构及机械门禁；
- 已确认的结构迁移与机械修复。

它不判断文档内容是否符合代码或产品行为。`CONTEXT.md` 是条件文件，并始终由
`$grill-with-docs` 维护。

该 Skill 只能显式调用。显式调用只开始只读调查和逐项确认，不自动授权修改、Git 操作、构建、测试或
其他 Skill。

### 通用资产

```text
project-doc-skeleton/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── skeleton-rules.md
│   └── testing-baseline.md
└── assets/SoftwareTesting/
    └── doc_consistency/
        ├── test_doc_consistency.py
        └── test_doc_consistency_rules.py
```

文档机械门禁默认从 Skill 资产逐字节安装，不允许在目标项目中手工转录或制作分叉。骨架只把测试根、
所有权、containment 和清理授权边界写入治理文档，不提供创建、复用、检查或清理测试现场的运行工具。

其中 `test_doc_consistency.py` 是复制到目标项目后运行的只读机械门禁，只检查文件、入口、链接、
生命周期、Registry 和归档结构；`test_doc_consistency_rules.py` 用隔离正反夹具验证门禁自身，
不判断文档内容是否符合代码。

## audit-project-docs

[`audit-project-docs`](audit-project-docs/SKILL.md) 的中文显示名为“项目文档内容审计”。

它用于：

- 对照代码、配置、构建、测试和可观察行为审计文档事实；
- 在标准或非标准文档结构中审计事实；
- 发现过期、缺失、重复或互相冲突的声明；
- 区分一致、不一致、无法验证、需要决策和未覆盖；
- 在单独授权后只修正现有活动文档中的事实正文，不实施结构变化；
- 将术语、`CONTEXT.md`、ADR 和语义取舍交给显式调用的 `$grill-with-docs`。

该 Skill 只能显式调用，默认只读。它不安装脚本、模板或持久化报告；修改文档和运行命令都需要独立确认。

目录保持最小：

```text
audit-project-docs/
├── SKILL.md
└── agents/openai.yaml
```

## 当前状态

**两个 Skill 已完成首轮隔离前向测试，可用于受控的单项目试用；暂不建议批量改造或无监督运行。**

当前本地开发验证：

- 两个 Skill 均通过 `skill-creator` 结构校验；
- 文档机械门禁的 23 个隔离夹具通过。
- 使用独立新鲜上下文验证了非空新项目首次迁移、逐项确认、精确清单、原文件保护和通用资产逐字节安装；
- 验证了多上下文项目会停止，不会被压平成单一骨架；
- 验证了非标准合成项目的内容审计、只修正已授权事实正文及拒绝越权结构修改；
- 以多个既有项目做了严格只读审计或骨架复核，未修改这些仓库；
- 验证了 `$audit-project-docs → $grill-with-docs → $project-doc-skeleton` 只能逐次显式调用，
  且修改、机械复制、验证命令和 Git 授权不会继承；
- 用负向确认包验证了依赖、工作目录和结果语义冲突会被逐项拦截。

仍需扩大验证的范围：

1. 不修改现有仓库这一前提下，尚未对大型非标准项目实施完整写入迁移；
2. 当前仅在 Windows 与本机 Python 环境验证，尚未做 Linux/macOS 可移植性回归；
3. 批量项目改造、无人监督运行和正式认证流程仍未验证。

当前不会安装 Skill，也不会执行 commit、push 或 PR。
