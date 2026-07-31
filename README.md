# kache_skills

本仓库用于开发和验证个人 Skill。仓库中的 Skill 在完成结构校验、脚本测试和真实项目正向验证前，
不应安装到个人 Skills 目录或用于批量修改项目。

- [项目文档](docs/README.md)
- [软件测试](SoftwareTesting/README.md)

## 构建与交付

本项目无独立构建步骤。

交付产物为仓库中的两个 Skill 源码目录：

- [`project-doc-skeleton`](project-doc-skeleton/)
- [`project-doc-consistency`](project-doc-consistency/)

## project-doc-skeleton

[`project-doc-skeleton`](project-doc-skeleton/SKILL.md) 的中文显示名为“项目文档骨架管理”。

它只负责单一上下文项目的：

- 固定与条件目录；
- 文档入口和实际链接可达性；
- 已确认的路径职责与承接位置；
- 待办、方案和归档生命周期；
- 测试治理结构及机械门禁；
- 已确认的结构迁移与机械修复。

它不判断文档内容是否符合代码或产品行为。`CONTEXT.md` 是条件文件，由用户另行选择的语义裁决流程
维护；环境中存在 `$grill-with-docs` 时可显式选择它，不存在时直接向用户交接待决问题。

该 Skill 只能显式调用。显式调用只开始只读调查和必要确认；互不依赖的未知项集中确认，存在冲突或依赖
时再逐个澄清。它不自动授权修改、Git 操作、构建、测试或其他 Skill。

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

## project-doc-consistency

[`project-doc-consistency`](project-doc-consistency/SKILL.md) 的中文显示名为“项目文档一致性”。

它在同一套证据规则下提供两种显式模式：

- `check` 默认只读检查标准或非标准文档中的当前事实，先区分当前事实、决定、历史结果、状态和非穷举
  摘要，再发现过期、缺失、重复或冲突声明；
- `sync` 先执行相同检查，再按文档职责最小同步可直接证明的事实正文；单独选择模式时先确认集中清单，
  明确要求“审计并修复”等直接实施动作时不重复请求文件修改确认；
- 两种模式都区分一致、不一致、无法验证、需要决策和未覆盖；
- 两种模式都不实施结构变化，也不裁决术语、`CONTEXT.md`、ADR 或语义取舍。

该 Skill 只能显式调用，未指定模式且没有修订意图时默认 `check`。“检查并修复”“审计后同步”等组合表达
直接进入 `sync`；命令执行仍须与文件修改分开授权。它不安装脚本、模板或持久化报告。

目录保持最小：

```text
project-doc-consistency/
├── SKILL.md
└── agents/openai.yaml
```

## 当前状态

**两个 Skill 已完成首轮隔离前向测试，可用于受控的单项目试用；暂不建议批量改造或无监督运行。**

当前本地普通验证：

- 两个 Skill 均通过 `skill-creator` 结构校验；
- 文档机械门禁的 23 个隔离夹具通过；
- 当前项目的 `T-DOC` 通过，结果为 0 warning；
- 使用独立新鲜上下文回归了骨架静态结论、全量 `check` 的范围与状态分类，以及 `sync` 的最小修订边界。

未完成的验证事项统一登记在[已知问题与待做需求](docs/已知问题与待做需求.md)。

安装 Skill、commit、push 和 PR 均须分别获得用户明确授权，不由文档或验证流程自动执行。
