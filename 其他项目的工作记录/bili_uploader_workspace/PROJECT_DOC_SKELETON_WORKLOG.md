# `project-doc-skeleton` 工作记录

- 记录日期：2026-07-31
- 执行场景：非空既有项目首次迁移
- 项目基线：`0b56000`（D6 fake-adapter Docker E2E 完成）
- 结构实施提交：`2e56c93`
- 交付分支：`agent/docs-skeleton-consistency`
- 交付 PR：Draft PR #22
- 记录性质：事后复盘；不作为当前项目事实或测试结果真源

本记录用于优化 `project-doc-skeleton`。它描述该 Skill 在本次调用中的要求、实际动作、有效做法、
摩擦点和改进建议。本文件由用户在原调用完成后另行明确要求创建，不表示该 Skill 在常规调用中会生成
持久化报告。

## 1. 用户目标与授权

用户要求先用 `project-doc-skeleton` 初始化骨架，再用 `project-doc-consistency` 审计并修复；除非遇到
必须由用户决定的问题，否则持续执行。调查完成后，用户一次性确认了：

- 使用简体中文维护文档和用户交流；标识符、API 与协议字段使用英文；
- 保留既有英文 Conventional Commit 风格；
- 不移动、归档或删除现有批次文档；
- 采用标准长期文档、测试治理、仓库外测试现场和机械门禁；
- 授权本轮文件修改、普通验证、分支、commit、push 和 Draft PR；
- 不授权真实账号、真实上传、Docker E2E、Rust 构建或合并 `main`。

一次集中确认覆盖了互不冲突的结构决定，没有逐项打断执行。

## 2. 调查与场景判断

调查范围包括适用的 `AGENTS.md`、根 README、全部活动 Markdown、测试和归档目录、Git 状态及已有
构建和交付入口。结论如下：

- 项目是单一上下文，没有 `CONTEXT-MAP.md` 或多个领域 `CONTEXT.md`；
- 已有完整代码、Docker 交付和大量批次文档，但缺少标准长期文档主干；
- 不存在 `SoftwareTesting/`、标准 Registry、归档索引或文档机械门禁；
- 现有工作树干净，历史内容可由 Git 恢复；
- 因此归类为“非空既有项目首次迁移”，不是新项目，也不是日常结构审查。

现有文档无法安全一对一迁移到全部标准职责，因此采用“保留原文档、新建承接路径、建立导航”的
方案，不移动、不合并、不删除历史批次文档。

## 3. 实际执行顺序

| 阶段 | 实际动作 | 结果 |
| --- | --- | --- |
| 规则读取 | 完整读取 Skill、骨架规则、测试基线和两份通用资产 | 明确结构边界、授权边界和逐字节资产要求 |
| 结构盘点 | 枚举活动 Markdown、测试入口、归档、语言与 Git 状态 | 确认首次迁移且无不可恢复旧文件 |
| 集中确认 | 汇总语言、职责映射、条件目录、测试层级、测试根和 Git 操作 | 用户一次确认，未遗留结构待决项 |
| 建立入口 | 更新 `AGENTS.md`、根 README、`docs/README.md` | 构建、文档和测试入口形成两跳可达导航 |
| 建立主干 | 新建需求、设计、待办、软件测试和归档索引 | 固定主干齐全，未创建空的方案、ADR 或测试归档目录 |
| 条件升格 | 新建字段契约和运维入口 | 项目已有 Schema、SQLite、跨进程协议、部署和恢复证据 |
| 测试治理 | 新建 Protocol、Safety、Registry 和五个 suite README | 测试类别、触发条件、命令、失败语义和安全边界有唯一入口 |
| 安装资产 | 从 Skill 资产目录原样复制两份 Python 门禁源码 | 目标 SHA-256 与源资产完全一致 |
| 行尾治理 | 新增 `.gitattributes`，把活动 Markdown 统一为 LF | 首次 T-DOC 的 CRLF 错误全部消除 |
| 机械验证 | 运行规则夹具、目标 T-DOC、链接与残留检查 | 23 项夹具通过，目标检查 0 warning |

## 4. 结构输出

### 4.1 固定主干

- `AGENTS.md`：增加构建、文档、测试入口及语言/Git 授权规则；
- `README.md#构建与交付`：声明 Docker/Compose 交付与测试入口；
- `docs/README.md`：活动文档入口、职责分流、生命周期和归档入口；
- `docs/需求文档.md`、`docs/设计文档.md`、`docs/已知问题与待做需求.md`、
  `docs/软件测试.md`；
- `SoftwareTesting/README.md`、`PROTOCOL.md`、`SAFETY.md`；
- `archive/docs/README.md`。

### 4.2 有证据支持的条件结构

- `docs/字段契约.md`：项目存在 JSON Schema、SQLite、配置、事件和多进程字段边界；
- `docs/运维/README.md`：项目存在 Docker、存储、权限、扫码、恢复和人工验证；
- `SoftwareTesting/doc_consistency/`、`python/`、`biliup_patch/`、`docker/`、`manual/`：
  都有实际测试或人工验证入口。

没有创建 `CONTEXT.md`、ADR、活动方案或 `archive/SoftwareTesting/`。D7 待办状态为“待实施”，
不满足建立活动方案的条件。

## 5. 通用资产与可复现性

安装后的资产与 Skill 源文件逐字节一致：

| 文件 | SHA-256 |
| --- | --- |
| `test_doc_consistency.py` | `2c87e82dc6e8729e84342ccd8dfa11ed6fdad09a2d0e565bebdab9337f4c884e` |
| `test_doc_consistency_rules.py` | `f898e8b9a791ae1389dab10c8c6490589ea3423dd0fe7450590cc4e457309aae` |

复制后没有在项目中修改通用源码。行尾规范只作用于目标路径，资产 hash 比较在所有格式化动作后再次执行。

## 6. 验证记录

| 验证项 | 结果 |
| --- | --- |
| 规则夹具 | `23 tests`，通过 |
| 目标项目 T-DOC | 通过，`0 warning(s)` |
| 两份资产逐字节比较 | 通过 |
| 活动 Markdown UTF-8/LF | 通过 |
| 必需入口、相对链接、标题锚点、两跳可达性 | 通过 |
| 待办状态、方案数量、Registry、归档关系 | 通过 |
| 绝对本地路径和旧名称残留 | 目标门禁未报告 warning |
| 产品代码、`CONTEXT.md`、ADR | 未修改 |

## 7. 有效做法

1. **职责边界清楚。** 骨架只创建承接位置和机械规则，具体产品事实留给后续 consistency sync，
   避免在结构阶段凭代码推导正文。
2. **集中确认有效。** 语言、测试层级、条件目录、Git 授权和不移动旧文档可以一次确认，减少了无意义停顿。
3. **历史文档原位保留。** 项目已有 D1-D6 文档，建立“已完成批次记录”入口比强行移动或归档风险低。
4. **资产禁止项目内分叉。** 逐字节复制和 hash 复核能明确区分通用门禁缺陷与项目配置问题。
5. **机械门禁覆盖面合适。** 首次运行立即发现全库 Markdown 行尾不符合 LF，而没有越界判断产品事实。

## 8. 摩擦点与边界案例

### 8.1 Windows 行尾需要显式迁移流程

首次 T-DOC 将所有既有 Markdown 报为 CRLF。仅新增 `*.md text eol=lf` 不会自动修正当前工作树；
仍需一次安全的批量规范化。随后 `verify_source.py` 又发现 pinned patch 在 Windows checkout 中被转为
CRLF，实际 hash 与锁值不符，而 LF 规范化后的 hash 完全匹配。

最终 `.gitattributes` 还需覆盖自身和 `*.patch`：

```gitattributes
.gitattributes text eol=lf
*.md text eol=lf
*.patch text eol=lf
SoftwareTesting/doc_consistency/*.py text eol=lf
```

当前 Skill 明确要求 Markdown LF，但没有给出首次迁移时的跨平台预检、规范化顺序或
`.gitattributes` 自身规则。

### 8.2 测试根规则缺少可执行的所有权引导

Safety 要求仓库外测试根、`.project-owner.json`、run containment 和失败关闭，同时明确骨架不提供
创建、检查或清理工具。既有 D6 文档原本提供可复制执行的一键命令；迁移后只能把目标改成“已经验证过的
绝对 run 路径”占位符，否则文档会暗示可以绕过所有权核验。

规则本身安全，但在首次迁移时会形成“治理要求完整、执行入口不可自助”的落差。

### 8.3 结构与内容 Skill 的交接只存在于对话

骨架先创建空职责文件，consistency 随后填充事实，顺序正确；但两者之间的职责映射、条件目录理由、
不修改项和待决项只存在于会话上下文。若两个 Skill 分别在不同任务运行，后一个 Skill 需要重新推导大部分
范围。

### 8.4 `AGENTS.md` 的最小性需要更明确的机械判据

骨架要求 `AGENTS.md` 保存长期入口、语言和授权规则，但项目原文件已经包含大量产品现状、专项文档清单和
命令。此次只增补必要入口，没有重构旧内容。Skill 对“迁移时是否需要报告已有 AGENTS 职责越界”缺少
明确的输出格式和严重度。

## 9. Skill 优化建议

| 优先级 | 建议 | 原因 | 可验收结果 |
| --- | --- | --- | --- |
| 高 | 增加跨平台 EOL preflight 与迁移步骤 | 首次迁移常见 CRLF；只写属性不足以修复工作树 | 在写入前报告 `git ls-files --eol` 摘要，给出不会触碰通用资产 hash 的规范化顺序 |
| 高 | 提供推荐 `.gitattributes` 最小片段并覆盖其自身 | 本次先后补了 Markdown、patch 和 `.gitattributes` 三类规则 | 新 checkout 上 T-DOC 与 pinned 文本 artifact hash 均稳定 |
| 高 | 定义 skeleton→consistency 的结构化交接摘要 | 当前交接只存在对话，跨任务容易丢失 | 输出路径职责、条件目录理由、旧文档处置、待决项和禁止修改项的短表，不写入项目也可 |
| 中 | 为测试根提供可选、显式授权的 owner-marker bootstrap/check 规范 | 仅有约束会迫使 runbook 使用不可执行占位符 | helper 能创建/校验 marker、规范化路径、拒绝 reparse point，且不提供自动清理 |
| 中 | 内置通用资产 hash 比较命令的 Windows/POSIX 两种写法 | 手工组合命令容易漏掉格式化后的二次比较 | 安装后自动输出源/目标 hash 与 exact-copy 布尔值 |
| 中 | 明确既有 `AGENTS.md` 职责越界只报告还是需要迁移 | 当前规则描述职责，但未规定非空项目的处置级别 | 最终清单单列“既有规则越界但本轮不改” |
| 低 | 可选输出本轮结构清单的机器可读临时结果 | 便于后续 Skill 和人工审查，避免持久状态 | 结果只在会话或授权的仓库外 run 中，默认不写项目 |

## 10. 最终边界

- 未移动、归档或删除任何既有文档；
- 未创建空条件目录；
- 未改产品代码、Schema、Docker 配置、`CONTEXT.md` 或 ADR；
- 未创建或清理仓库外测试 run；
- 结构阶段没有宣称文档事实已与实现一致；
- commit、push 和 Draft PR 均在用户分别确认后执行。
