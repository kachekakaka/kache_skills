# project-doc-skeleton 工作记录：HG Workspace 首次迁移

## 记录说明

本文件是在任务完成后应用户明确要求形成的历史工作记录，不是 `project-doc-skeleton` 的默认持久化输出。记录用于后续优化 Skill，当前规则仍以 [project-doc-skeleton](../../project-doc-skeleton/SKILL.md) 及其 references 为准。

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 执行日期 | 2026-07-31 |
| 目标项目 | `hg_workspace` |
| 场景判断 | 单一上下文、已有代码和非标准文档，属于首次迁移 |
| 目标项目基线 | `d9f1d35def916e729ef17c2f5cb4d977c963ce51` |
| 目标项目结果提交 | `d3b2889db6e01d3c61a132264f2b6cf01bf3848c` |
| Skill 仓库基线 | `1fa37ac9bd3540584c021639146dda7f3e693b2d` |
| 验证层级 | 普通验证；未执行全量后端或 Android 测试 |

## 用户目标与授权

- 用户明确要求先用 `project-doc-skeleton` 初始化骨架，再用 `project-doc-consistency` 审计并修复。
- 用户要求除非出现必须由其决定的真实取舍，否则持续执行。
- 用户确认了迁移清单、文件移动、通用门禁安装和三类普通验证。
- 文件修改、验证命令和最终 commit 分别取得授权；未授权 push、PR 或发布。
- 目标项目已有 `scripts/build-apk.bat`、`scripts/install-apk.bat` 工作区修改，整个过程中均未覆盖，也未纳入提交。

## 调查结论

1. 项目没有 `CONTEXT-MAP.md`、多个领域 `CONTEXT.md` 或明显独立业务上下文，适用单一上下文骨架。
2. 根 README、构建脚本、CI、Compose、后端和 Android 代码已经存在，但缺少标准文档入口、测试治理入口和文档门禁。
3. `docs/decisions/` 中有 11 份 ADR；另有 Android 开发说明和 4 份历史交接或重构资料。
4. 旧文档均由 Git 可靠保存，移动前没有不可恢复的文档修改，因此没有建立外部备份。
5. 项目存在 API、数据库、配置和 Android/后端序列化边界，满足创建 `docs/字段契约.md` 的条件。
6. 项目不存在需要单独维护的项目专属术语集，因此没有创建 `CONTEXT.md`。

## Skill 直接完成的动作

### 固定骨架

- 创建根 `AGENTS.md`，只保存语言、授权、安全和长期入口。
- 创建 `docs/README.md`、`docs/需求文档.md`、`docs/设计文档.md`、`docs/已知问题与待做需求.md`、`docs/软件测试.md`。
- 创建 `SoftwareTesting/README.md`、`SoftwareTesting/PROTOCOL.md`、`SoftwareTesting/SAFETY.md`。
- 创建 `archive/docs/README.md` 并登记历史文档。
- 在根 README 增加项目文档、测试入口和唯一“构建与交付”入口。

### 条件结构

- 创建 `docs/字段契约.md`，承接数据库、API、配置和跨层映射。
- 创建 `docs/adr/`，承接已有 ADR。
- 创建 `docs/运维/Android开发.md`，承接现有 Android 开发与安装说明。
- 创建 `SoftwareTesting/doc_consistency/`、`backend/`、`android/`；后续根据 CI 审计结果增加 `repository/`。

### 机械迁移

- 11 份 ADR 从 `docs/decisions/` 移至 `docs/adr/`，正文保持不变。
- 4 份历史资料移至 `archive/docs/`，正文保持不变并在归档索引登记。
- `docs/ANDROID_DEVELOPMENT.md` 移至 `docs/运维/Android开发.md`；结构迁移时保持原文，随后由一致性 Skill 同步事实。
- 创建 6 个稳定待办 ID：`HG-001` 至 `HG-006`，状态均为 `待实施`，没有创建不满足条件的活动方案。

### 通用门禁

- 从 Skill 资产原样安装 `test_doc_consistency.py` 和 `test_doc_consistency_rules.py`。
- 规则资产出现修改需求时，先修改并验证 Skill 源资产，再重新复制到目标项目和 Skill 仓库自身的已安装门禁。
- 最终比较源资产、Skill 仓库自检副本和目标项目副本的 SHA-256，确认逐字节一致。

## 跨边界交接与后续回流

| 发现 | Skill 边界 | 实际处理 |
| --- | --- | --- |
| 核心文档缺少当前产品事实 | 骨架不得从代码推导事实 | 交给随后显式调用的 `project-doc-consistency sync` |
| Registry 未覆盖仓库卫生、Python 编译和 Compose 校验 | 属于测试治理结构 | 一致性审计给出证据后，回流骨架范围新增 `T-REPOSITORY` |
| CI 未执行 `T-DOC` | 属于机械门禁接入 | 在测试治理回流中补入 CI |
| 门禁夹具含连续的假 GitHub Token | 属于通用资产缺陷 | 先修 Skill 资产并运行 23 项自测，再重新安装 |
| 仓库卫生脚本无法处理未暂存重命名 | 属于目标项目测试工具 | 修复为扫描现存已跟踪文件和未忽略新文件，不修改真实 Git 索引 |

## 验证记录

| 验证项 | 结果 |
| --- | --- |
| 门禁规则夹具 | 23 项全部通过 |
| 目标项目 `T-DOC` | 通过，`0 warning(s)` |
| 门禁资产一致性 | 源资产、Skill 仓库自检副本和目标项目副本 SHA-256 一致 |
| 仓库卫生 | 通过 |
| 明显密钥模式补充扫描 | 0 命中 |
| `git diff --check` | 目标项目和 Skill 仓库均无空白错误 |
| 产品测试 | 后端与 Android 未运行，不在本次普通验证范围 |

最终资产哈希：

- `test_doc_consistency.py`：`2C87E82DC6E8729E84342CCD8DFA11ED6FDAD09A2D0E565BEBDAB9337F4C884E`
- `test_doc_consistency_rules.py`：`F92CF24CB14642C21AF644A85B4B7A8C4CB68C2DFDAE379FE6571C63B150C671`

## 实战中暴露的问题

### 1. 技术性说明不够易懂

在解释“假 Token 误报”和“Registry 与 CI 不一致”时，用户直接反馈“看不懂”。说明当前流程虽然边界严谨，但面向用户的第一层说明仍过于技术化。

建议：所有阻塞或剩余问题先给一段不超过三句的白话结论，再提供路径、规则和命令细节。可固定为“发生了什么、会造成什么、准备怎么处理”三句结构。

### 2. 通用夹具与仓库秘密扫描器冲突

规则夹具使用了形似真实 GitHub Token 的连续字符串。夹具自身测试通过，但目标项目的仓库卫生检查会把它当成明显 secret，导致未来 CI 失败。

当前修复：改为运行时字符串拼接，测试语义不变，静态扫描不再看到完整 Token 形状。

建议：Skill 资产发布前增加常见 secret 模式静态扫描；测试凭据样例默认使用分段拼接或明显不满足真实格式的字符集。

### 3. 未暂存迁移与 `git ls-files` 的交互

大量移动尚未暂存时，旧路径仍在 Git 索引中而工作区文件已不存在。目标项目原仓库卫生脚本因此在 `path.stat()` 崩溃，同时也看不到新文件。

建议：骨架最终验证说明中明确提醒“移动未暂存时 Git 可能显示旧路径删除和新路径未跟踪”；仓库级扫描器应扫描现存已跟踪文件与未忽略新文件，并跳过已删除路径。

### 4. 跨仓库逐字节资产受行尾策略影响

目标项目用 `.gitattributes` 固定文本为 LF；Skill 仓库只固定 Markdown 为 LF。Windows 上检查 Python 资产差异时出现“下次 Git 接触将改为 CRLF”的提示。当前工作区和目标副本哈希一致，但不同 checkout 配置可能破坏长期逐字节一致性。

建议：Skill 仓库为通用 Python 资产显式固定 `eol=lf`，并把跨平台 checkout 后的哈希比较加入资产自测试。

### 5. 骨架与内容 Skill 的交接需要更显眼

首次迁移中，骨架必须创建空职责文档，但不能自行填写项目事实。对用户而言，“骨架已完成”容易被理解成“文档内容已完成”。

建议：首次迁移最终报告固定分成“结构已完成”“内容仍待一致性审计”两栏；若用户已显式串联两个 Skill，则展示连续阶段而不是两个彼此独立的长说明。

## 建议优化优先级

1. **P0：资产秘密扫描。** 在发布或安装前扫描 Skill 通用资产，避免夹具触发目标仓库 CI。
2. **P0：Python 资产行尾固定。** 让逐字节一致性在 Windows/Linux checkout 间稳定。
3. **P1：白话摘要层。** 先给三句结论，再展开技术证据和精确路径。
4. **P1：迁移态仓库检查指引。** 明确未暂存移动的 Git 表现，并建议扫描器处理删除与新文件。
5. **P1：跨 Skill 阶段交接。** 将“结构完成”和“事实完成”作为两个明确状态展示。
6. **P2：按需复盘模板。** 仅在用户明确要求时生成类似本文件的历史记录，不改变 Skill 默认不持久化运行报告的边界。

## 未执行操作

- 未执行后端 pytest、后端运行时健康检查、Compose 构建、Android JVM 测试或 APK 构建。
- 未操作真实数据、产品进程或第三方网络。
- 未 push、未创建 PR、未发布或安装 Skill。
