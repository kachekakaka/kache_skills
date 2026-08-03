# `project-doc-consistency` 工作记录

- 记录日期：2026-07-31
- 执行模式：`sync`
- 检查范围：首次迁移后的全量活动文档事实检查
- 项目基线：`0b56000`（D6 fake-adapter Docker E2E 完成）
- 事实同步提交：`2e56c93`
- 交付分支：`agent/docs-skeleton-consistency`
- 交付 PR：Draft PR #22
- 记录性质：事后复盘；不作为当前项目事实或动态验证结果真源

本记录用于优化 `project-doc-consistency`。原 Skill 明确禁止在正常 check/sync 中创建持久化报告；本文件是
原调用完成后由用户另行明确要求的复盘产物，不改变该次 sync 的授权或职责边界。

## 1. 模式、范围与授权

用户的“审计后修复”被解释为 `sync`，且明确授权修复本次范围内所有可直接证明的文档事实。因为目标是
非标准既有项目的首次迁移，采用全量检查，而不是默认增量检查。

执行前分别确认了：

- 文件修改：已授权；
- 普通验证命令：已授权；
- branch、commit、push、Draft PR：分别授权；
- Docker/Rust/真实账号/真实投稿/合并 `main`：未授权且不在普通验证范围。

实施前先集中说明拟同步清单：补全新长期文档；纠正 D6 待完成声明、虚构的 `spool/staging`、旧 PR #8
启动提示、旧扫码分支和 systemd 路径；保留按日期成立的历史批次正文；不修改机器审批元数据。

## 2. 声明—证据调查范围

### 2.1 活动文档

检查了根 README、`THIRD_PARTY_NOTICES.md`、`docs/` 下全部活动 Markdown、manual、reports、Schema
README，以及骨架新增的核心文档和 suite README。归档索引为空，没有把历史正文当作当前事实。

### 2.2 实现与配置证据

重点读取或检索：

- CLI 命令：`src/bili_uploader/cli.py`；
- runtime 模式和调度默认值：`runtime_config.py`、`runtime_service.py`、`scheduler.py`；
- 目录与 hidden staging：`runtime_layout.py`、任务协议模块；
- SQLite schema、状态和提交顺序：`queue_schema.py`、`queue_terminal.py`、恢复模块；
- Schema kind 与 canonical JSON：`contracts/schemas.py`、`io/atomic.py`；
- Docker 事实：`Dockerfile`、`compose.yaml`、容器默认配置、entrypoint；
- 验证入口：四个 GitHub Actions workflow、`scripts/docker-e2e.sh`、`tools/verify_source.py`；
- pinned upstream、patch hash 和审批状态：`vendor/upstream/biliup.lock.json`。

没有采用“代码永远正确”的单一优先级。可靠性规则以协议和恢复文档为决定真源，再检查代码、配置和其他
文档是否冲突；动态“已通过”结论由 Git 历史、测试、PR CI 或用户授权运行提供证据。

## 3. 主要声明分类与处理

| 声明 | 证据 | 初始结论 | 处理 |
| --- | --- | --- | --- |
| D6 仍待完成 | `main` 已含 D6 commit、E2E 脚本和 CI；交接状态也声明完成 | 不一致 | 把当前态文档改为 D6 已交付，下一步仅 D7 |
| 下一任务是检查 PR #8 并从 D1 开始 | AGENTS 和 Git 历史证明 replacement 已合并、旧 PR 已关闭 | 不一致 | 重写 `NEW_CHAT_PROMPT.md` 为 D7 laboratory 启动提示 |
| 存在独立 `spool/staging` | runtime layout 只在 `spool/incoming/.<task_id>.staging` 使用 hidden staging | 不一致 | 修正 P0 状态、交接和挂载说明 |
| Docker 后仍在宿主机调用账号 CLI | 正式交付是 Compose，容器内已安装账号入口 | 不一致 | 根 README 和扫码 runbook 改用 `docker compose exec` |
| 扫码应切换旧 `agent/p0-qr-login` 分支 | 功能已合入当前 `main` | 不一致 | 删除旧分支步骤，要求当前 main 或验证 tag |
| 正式目录使用旧 systemd venv 路径 | 当前用户验收路径是 Docker/Compose | 不一致 | 替换为三个 bind mount 和容器内命令 |
| Python 3.12/3.13 命令可在未限定平台运行 | queue 模块无条件使用 POSIX `fcntl`，CI 只在 Ubuntu 运行 | 不一致 | 明确源码全量检查需要 Linux/WSL2 |
| D1-D6 批次文档中的“下一步”文字 | 文档带基线日期，描述当时阶段 | 一致（历史语境） | 不批量改写；由文档入口声明历史文本不覆盖当前状态 |
| 默认 adapter、调度周期、SQLite v1、result→receipt→SQLite→done | 代码、配置、Schema 和测试相互支持 | 一致 | 写入需求、设计和字段契约的适当抽象层级 |
| stock CLI 退出码可作为成功证据 | 协议、bridge 和 supervisor 都明确否定 | 一致的禁止性契约 | 在新长期文档和 D7 提示中保持，不放宽 |
| lock 的 approval blockers 仍提到 D2-D6 未完成 | D2-D6 已完成，但目标是机器审批元数据而非活动 Markdown | 需要决策／跨边界 | 不修改，在最终报告和 PR body 中单列 |

## 4. 实际同步文件

### 4.1 在骨架已建立职责后补全的长期事实

- `docs/需求文档.md`：当前已交付行为、可靠性验收边界、运行与数据边界、D7 未开放项；
- `docs/设计文档.md`：组件与数据流、身份、SQLite、adapter、持久提交顺序和容器启动；
- `docs/字段契约.md`：Schema 所有权、canonical JSON、身份字段、SQLite 与运行配置真源。

### 4.2 最小修订的既有当前态文档

- `README.md`；
- `THIRD_PARTY_NOTICES.md`；
- `docs/CONTAINER_STORAGE.md`；
- `docs/D6_FAKE_DOCKER_E2E.md`；
- `docs/DOCKER_FIRST_AMENDMENT.md`；
- `docs/DOCKER_TESTING.md`；
- `docs/HANDOFF_DOCKER_MVP.md`；
- `docs/IMPLEMENTATION_PLAN.md`；
- `docs/NEW_CHAT_PROMPT.md`；
- `docs/P0_STATUS.md`；
- `docs/RECOVERY_MATRIX.md`；
- `docs/manual/LOCAL_QR_LOGIN_VALIDATION.md`。

`NEW_CHAT_PROMPT.md` 是唯一大幅重写的既有文档。它的职责是当前可执行交接提示，原正文几乎全部要求重做
已完成的 D1-D6；逐句小修会保留危险的旧执行顺序，因此采用同职责内的整体替换。

## 5. 明确未修改的内容

- D1-D5 批次文档和历史报告中按基线日期成立的旧“下一步”正文；
- 待办状态、活动方案数量、Registry 结构、归档关系和导航，这些由 skeleton 阶段处理；
- `AGENTS.md` 的结构规则和授权规则，这些由 skeleton 阶段处理；
- `vendor/upstream/biliup.lock.json` 的 stale approval-blocker 文案；
- 产品代码、Schema、runtime 配置、Dockerfile、Compose 和 CI workflow；
- 真实账号、Cookie、二维码、真实媒体或真实投稿结果。

## 6. 验证与结果分类

| 验证项 | 本地结果 | 最终结论 |
| --- | --- | --- |
| 文档门禁规则夹具 | 23 项通过 | `passed` |
| 目标 T-DOC | 0 warning | `passed` |
| `compileall` | 返回 0 | `passed` |
| Ruff | `All checks passed!` | `passed` |
| `verify_source.py` | `source verification OK` | `passed` |
| Windows 全量 pytest | 收集时 9 个模块因缺少 POSIX `fcntl` 阻断 | `blocked`，不是断言失败 |
| PR CI Python 3.12 | Ubuntu job 成功 | `passed` |
| PR CI Python 3.13 | Ubuntu job 成功 | `passed` |
| Docker/Rust suite | 本轮未影响且未授权 | `not_run` |
| 真实账号和 D7 | explicit，未授权 | `not_run` |

本地 Windows 环境最初还缺少项目 dev 依赖。使用隔离 Python 3.12 环境后 compile、Ruff 和源码验证通过；
pytest 的剩余阻断来自平台，不是依赖缺失。PR 的 Ubuntu 3.12/3.13 CI 随后补齐全量测试并全部通过。

## 7. 调查中发现的跨平台事实

`verify_source.py` 首次在 Windows 工作树报告 candidate patch SHA-256 不匹配：

```text
锁定值 / LF 规范化值：30f9ee06c81a76f767cac3b051871cc95d5c7aa6fd436311d16ecc260c3aff24
Windows CRLF 工作树值：8a5b8fa909e5fd312197029ec4189cc5203283d57f7dbe5e25e3e1e6dd2dceae
```

Git index 原本就是 LF，补丁语义和 indexed content 没有变化。最终由骨架行尾治理增加 `*.patch text eol=lf`
并规范化工作树，随后 `verify_source.py` 通过。这个问题横跨文档骨架、构建 artifact 和机器锁，现有
consistency 分类没有专门的“非文档但阻断文档任务验证”交接类型。

## 8. 有效做法

1. **五种结论避免过度修订。** 历史批次文档被判为时间语境下一致，没有因为旧“下一步”而全量改写。
2. **先看职责再补事实。** 长期需求、设计和字段契约只记录其抽象层级需要的事实，没有复制源码实现。
3. **直接证据门槛有效。** 调度周期、adapter 模式、SQLite 版本和提交顺序都有代码、配置或测试证据。
4. **冲突不自动服从代码。** 可靠性语义继续以协议/恢复契约为真源，代码只用于检查实现是否违反。
5. **集中清单减少停顿。** 所有可同步项、不会修改项和验证命令一次说明，用户一次确认后连续实施。

## 9. 摩擦点与边界案例

### 9.1 “不持久化报告”不利于 Skill 优化闭环

原 Skill 要求声明—证据映射只保存在内存和交流中，并禁止持久化报告。这能避免项目被一次性审计文件污染，
但也让复杂首次迁移的证据、判定和边界案例在任务结束后难以系统复盘。本文件只能通过用户事后新请求创建。

### 9.2 历史文档识别依赖人工语境

批次文档有日期和阶段，但没有统一机器字段。要区分“历史上正确的下一步”与“当前 runbook 的错误下一步”，
必须结合文件职责、标题、基线日期、入口位置和当前使用方式人工判断。`NEW_CHAT_PROMPT.md` 虽与批次历史相邻，
却是当前执行入口，不能按历史文本保留。

### 9.3 sync 的“最小修订”缺少整篇替换判据

大多数文件适合替换一两句；但当前提示词或 runbook 若绝大部分步骤已过期，逐句修补反而更难审查且容易遗漏。
本次对 `NEW_CHAT_PROMPT.md` 整体重写是必要的，但 Skill 没有明确说明何时这种做法仍属于“维持准确性所需的
最小修订”。

### 9.4 非文档真源的 stale 状态没有可执行交接

lock 文件的 approval blockers 与当前 D2-D6 状态冲突，但 consistency 不能修改机器元数据，也不能把代码
或配置自动交给其他 Skill。最终只能报告“需要决策”，没有标准字段说明建议责任人、影响和解除条件。

### 9.5 平台阻断与远端 CI 证据的关系不够明确

本地 pytest 因 Windows 缺少 `fcntl` 被正确归为 `blocked`，随后相同候选的 Ubuntu CI 全绿。Skill 定义了
结果状态，但没有说明可信 CI 是否可以补齐本地环境阻断、何时可以把 suite 最终结论记为 `passed`。

### 9.6 全量检查成本较高但没有可复用的范围摘要

首次迁移要求检查全部活动 Markdown及相关代码、配置、构建和测试入口。本次读取了大量长篇批次设计；
大部分只需判定为历史语境，无需逐项展开。由于没有路径职责清单或上次证据摘要，后续任务仍可能重复读取。

## 10. Skill 优化建议

| 优先级 | 建议 | 原因 | 可验收结果 |
| --- | --- | --- | --- |
| 高 | 允许用户显式要求“复盘报告模式”，默认仍不持久化 | 兼顾项目整洁和 Skill 优化证据 | 只有单独授权时写入指定路径，并声明不是当前事实真源 |
| 高 | 增加“历史／当前入口／当前契约”识别清单 | 当前主要靠人工语境，容易误改批次记录或漏改 runbook | 每个文件先记录职责、时间语境和是否可执行，再检查声明 |
| 高 | 为当前 prompt/runbook 定义整篇替换条件 | 绝大多数句子过期时逐句小修并不最小 | 当旧步骤会触发错误操作且保留结构无价值时，允许同职责整体替换并说明理由 |
| 高 | 增加跨边界发现的标准交接格式 | stale machine metadata 无法在 sync 中处理 | 输出目标、证据、结论、影响、建议责任域和解除条件，不自动修改 |
| 中 | 明确本地 `blocked` 与可信 CI `passed` 的合并规则 | 跨平台项目常依赖 CI 补齐 POSIX/架构环境 | 同一 commit、同一规范命令和覆盖范围匹配时允许 CI 解除本地环境阻断 |
| 中 | 接受 skeleton 提供的路径职责交接摘要 | 避免首次迁移后重复推导结构 | consistency 启动时可直接验证摘要 freshness，再路由证据读取 |
| 中 | 在全量检查中先做文档角色分组和风险排序 | 长篇历史文档占用大量调查成本 | 优先当前入口、runbook、状态页和长期契约，历史记录只核对时间语境和当前引用 |
| 中 | 对执行证据记录候选 SHA 与环境 | 动态“通过”必须可追溯 | 报告命令、commit、平台、结果来源和是否替代本地阻断 |
| 低 | 增加“非穷举摘要无需扩写”的正向示例 | 该规则正确但实践判断仍主观 | 示例覆盖 README 摘要、字段入口和完整清单三种不同职责 |

## 11. 最终结论与未解决项

文档 sync 范围内、能够由直接证据证明的不一致均已修订；历史记录、结构项和动态 explicit 测试没有越界
改写。由于 `vendor/upstream/biliup.lock.json` 仍有 stale approval-blocker 文案，本次全量项目检查不能宣称
“所有来源整体一致”。该项属于机器审批元数据，需要在单独任务中决定是删除已满足 blocker、改成持续门禁，
还是保留为历史说明。
