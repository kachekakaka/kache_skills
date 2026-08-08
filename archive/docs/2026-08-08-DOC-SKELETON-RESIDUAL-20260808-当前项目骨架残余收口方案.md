# DOC-SKELETON-RESIDUAL-20260808：当前项目骨架残余收口方案

- 状态：已完成
- 保存日期：2026-08-08
- 主责：当前项目文档骨架、历史生命周期与标准 T-DOC 机械规则；由普通实施任务接手，`project-doc-skeleton` 不施工。
- 测试层级：普通验证
- 验证影响域：根入口、文档归档、标准 T-DOC 源资产及镜像、门禁规则夹具和当前真源声明
- 具体验证项：Skill 结构校验、T-DOC 规则夹具、当前项目 T-DOC、三份标准资产逐字节比较、静态链接与范围复核、关闭后最终 T-DOC

## 1. 目标、证据与决定

当前项目采用标准骨架。保存前 `main` 与 `origin/main` 一致且工作区干净；七类标准项目级 Skill 根均不存在，
`project-doc-skeleton/` 与 `project-doc-consistency/` 是本项目交付物，不按项目级 Skill 工具根排除。

本轮四项决定已经确认，实施任务不再重新选择：

| 差异与影响 | 选项 | 推荐理由 | 用户决定 | 最小补证／停点 |
| --- | --- | --- | --- | --- |
| 17 份外部项目记录仍在活动空间，混淆本项目边界 | 保持活动并补所有者；保留正文并归档；删除或合并 | 正文仍有历史证据价值，但不承接本项目当前事实 | 保留正文和相对层级，全部迁入 `archive/docs/其他项目的工作记录/`，不删除或改写产品结论 | 施工前重新冻结 17 个源路径、工作区重叠和清单外一层消费者；任一漂移即停止 |
| 根 `README.md` 复制需求、设计和两个 Skill 的详细规则，增加漂移面 | 保持详细入口；收缩为最短入口 | 长期事实已有专责真源，根入口只需导航和构建交付 | 收缩，但保留简要能力边界、最短入口、`README.md#构建与交付` 及文档／测试总入口 | 重新解析 `AGENTS.md` 与 `SoftwareTesting/PROTOCOL.md` 的直接消费；发现新消费者即停止 |
| 标准资产清单只写两份 Python，遗漏 suite README | 继续按两份；把 README 纳入三份整文件 | README 承接安装、命令与断言契约，且源／镜像已只读证明逐字节一致 | 安装、比较和资产树统一按三份资产表述 | 写入前重做三份源／镜像字节核对；出现分叉即停止 |
| T-DOC 不识别无所有者的顶层 Markdown 根，后续项目可能复现 | 写死当前目录；增加最小通用所有权规则；扩大为全局语义或两跳审计 | 通用所有权规则可机械证明且覆盖以后项目，不侵入正文和产品目录 | 增加最小通用规则；不得写死 `其他项目的工作记录/`，不得扩大为正文语义、产品目录或全局两跳审计 | 规则必须由正反夹具证明；若需语义解析、项目特例或更宽扫描即停止 |

不在本方案中核对外部项目事实、测试覆盖率、断言质量、成本或全项目安全，也不修改两个 Skill 的阶段职责。

## 2. 覆盖／残余矩阵

| 维度 | 精确范围 | 状态 | 证据／残余 |
| --- | --- | --- | --- |
| 上下文与路线 | 根入口、外部记录根 | 已覆盖（存在缺口） | 主项目是单一标准上下文；未分类外部记录使边界不够明确 |
| 结构与职责 | `README.md`、当前真源、三文件资产 | 已覆盖（存在缺口） | 根入口过度承责；资产清单漏列 README |
| 入口与导航 | 根、文档、测试、归档入口 | 已覆盖（存在缺口） | 标准入口正常；外部记录根没有项目级所有者入口 |
| 活动与历史生命周期 | `其他项目的工作记录/**`、`archive/docs/**` | 已覆盖（存在缺口） | 17 份历史证据仍位于活动空间 |
| 待办、方案与记录 | 当前待办、活动方案目录 | 已覆盖（存在缺口） | 原有三个待办合法；本方案新增一项待确认待办承接本缺口 |
| 测试治理结构 | T-DOC、T-PROJECT-DOC-FORWARD、内嵌资产根 | 已覆盖（满足） | 两个活动项所有者与实现根清楚，无游离顶层测试目录 |
| 机械门禁与授权边界 | T-DOC 实现、规则夹具、AGENTS、PROTOCOL | 已覆盖（存在缺口） | 授权边界一致；门禁未检查无所有者的顶层 Markdown 根 |
| 内容事实 | 外部项目和产品正文 | 未覆盖 | 只保留历史证据，不裁决内容真伪 |
| 测试设计经济性 | 覆盖、重复、断言和成本 | 未覆盖 | 不属于骨架职责 |

## 3. 确定实施切片

### 3.1 历史记录归档

把下表冻结的 17 份文件保持相对层级迁入 `archive/docs/其他项目的工作记录/`，并由 `archive/docs/README.md`
逐份恰好登记一次。历史职责和当前承接按表实施；当前承接路径在归档索引中写成实际 Markdown 链接，“无”不得改成
推测的外部项目真源。

| 归档相对路径 | 历史职责 | 当前承接真源 |
| --- | --- | --- |
| `2026-08-01_项目文档Skill前向试用与F2对照.md` | 记录四项目双 Skill 前向试用、F2 对照和改进建议 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `bili_uploader_workspace/2026-08-01-project-doc-skills-forward-check.md` | 记录上传器项目双 Skill 只读前向试用结果 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `bili_uploader_workspace/P0_BILIUP_BRIDGE_PROTOTYPE.md` | 记录外部上传器兼容桥原型、边界和阻断项 | 无，仅保留历史证据 |
| `bili_uploader_workspace/P0_UPSTREAM_CONTRACT_REVIEW.md` | 记录外部上传器上游 CLI 契约缺口和 P0 取舍 | 无，仅保留历史证据 |
| `bili_uploader_workspace/PROJECT_DOC_CONSISTENCY_WORKLOG.md` | 记录上传器项目一致性审计、同步和改进建议 | `project-doc-consistency/SKILL.md` |
| `bili_uploader_workspace/PROJECT_DOC_SKELETON_WORKLOG.md` | 记录上传器项目骨架迁移、验证和改进建议 | `project-doc-skeleton/SKILL.md` |
| `bili_workspace/2026-07-31_项目文档骨架与一致性审计Skill工作记录.md` | 记录 bili 项目双 Skill 首次执行、修复、验证和改进建议 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `bili_workspace/2026-08-01-project-doc-skills-forward-check.md` | 记录 bili 项目双 Skill 只读前向试用结果 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `bili_workspace/2026-08-04-DOC-LIFECYCLE-20260804-文档生命周期实施工作记录.md` | 记录 bili 项目文档生命周期方案实施和 T-DOC 验证 | `project-doc-skeleton/SKILL.md` |
| `douyin_recorder_workspace/2026-07-31-project-doc-consistency-worklog.md` | 记录抖音录制项目一致性审计、同步和改进建议 | `project-doc-consistency/SKILL.md` |
| `douyin_recorder_workspace/2026-07-31-project-doc-skeleton-worklog.md` | 记录抖音录制项目骨架迁移、验证和改进建议 | `project-doc-skeleton/SKILL.md` |
| `douyin_recorder_workspace/2026-08-01-project-doc-skills-forward-check.md` | 记录抖音录制项目双 Skill 只读前向试用结果 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `douyin_recorder_workspace/README.md` | 记录抖音录制项目两份历史工作记录的旧子索引 | 无，仅保留历史证据 |
| `hg_workspace/2026-07-31-hg-workspace-project-doc-consistency.md` | 记录 HG 项目一致性全量审计、同步和改进建议 | `project-doc-consistency/SKILL.md` |
| `hg_workspace/2026-07-31-hg-workspace-project-doc-skeleton.md` | 记录 HG 项目骨架迁移、验证和改进建议 | `project-doc-skeleton/SKILL.md` |
| `hg_workspace/2026-08-01-project-doc-skills-forward-check.md` | 记录 HG 项目双 Skill 只读前向试用结果 | `SoftwareTesting/manual/project_doc_skills/README.md` |
| `hg_workspace/README.md` | 记录 HG 项目两份历史工作记录的旧子索引 | 无，仅保留历史证据 |

保存前全仓精确搜索未发现清单外消费者。五份文件共有十一条一层 Markdown 链接，移动后的动作冻结如下：

| 原文件 | 链接数 | 移动后动作 |
| --- | ---: | --- |
| `bili_workspace/2026-07-31_项目文档骨架与一致性审计Skill工作记录.md` | 3 | 更新指向 `docs/README.md`、`AGENTS.md`、`SoftwareTesting/README.md` 的三条深度 |
| `hg_workspace/2026-07-31-hg-workspace-project-doc-skeleton.md` | 1 | 更新指向 `project-doc-skeleton/SKILL.md` 的深度 |
| `douyin_recorder_workspace/README.md` | 2 | 两条同目录历史正文链接保持不变并重新解析 |
| `hg_workspace/2026-07-31-hg-workspace-project-doc-consistency.md` | 1 | 更新指向 `project-doc-consistency/SKILL.md` 的深度 |
| `hg_workspace/README.md` | 4 | 两条同目录历史正文链接保持不变；两条当前 Skill 链接更新深度 |

合计七条链接需要更新深度，四条同目录链接保持文本不变但必须重新解析。全部十一条目标确认后才移除空的原目录。

### 3.2 根入口与三文件资产

- 收缩 `README.md` 的两个 Skill 详细规则段，保留交付物、简短行为边界、标准资产入口、验证入口和待办入口。
- 保留被 `AGENTS.md` 与 `SoftwareTesting/PROTOCOL.md` 直接消费的“构建与交付”标题和现有总入口。
- 在 `README.md` 与 `project-doc-skeleton/references/testing-baseline.md` 中把标准 T-DOC 安装、比较和资产树统一为
  `README.md`、`test_doc_consistency.py`、`test_doc_consistency_rules.py` 三份整文件。
- `docs/设计文档.md` 已列出三文件结构；实施时只做最终一致性核对，除非同批门禁行为说明需要同步，否则不为重复
  目录树而改写它。

### 3.3 顶层 Markdown 根所有权门禁

- 在当前 T-DOC 源和 Skill 镜像中增加同一最小规则，并在规则夹具增加一个无所有者顶层 Markdown 根的反例和一个
  由现有总入口精确承接的正例。
- 同步两份 `SoftwareTesting/doc_consistency/README.md` 的机械断言说明；同步
  `project-doc-skeleton/references/testing-baseline.md` 的 error 边界。
- 按当前职责最小同步 `README.md`、`SoftwareTesting/README.md`、`docs/软件测试.md`、`docs/需求文档.md` 和
  `docs/设计文档.md` 中直接声称的现行门禁能力；不得借机重写两个 Skill 的其他行为。

确定修改路径为上述源／目标历史记录、`archive/docs/README.md`、`README.md`、五份当前真源、T-DOC 的 README、
两份 Python 源文件及其 Skill 镜像、`project-doc-skeleton/references/testing-baseline.md`、本待办与本方案生命周期路径。
`project-doc-skeleton/SKILL.md` 和前向试用契约仅做静态复核；只有发现它们直接把资产固定为两份，或现有硬断言会因
新门禁结果失真时，才作为可能路径停止并申请范围差额，不在实施任务中自动扩张。

## 4. 验证、副作用与完成条件

保存时所有动态验证均为 `not_run`。普通实施任务按以下顺序验证：

1. 对修改后的 `project-doc-skeleton` 运行结构校验；
2. 使用 `python -B -X utf8` 运行 T-DOC 规则夹具和当前项目 T-DOC；
3. 逐字节比较当前项目与 Skill 内的三份 T-DOC 资产；
4. 静态核对 17 份归档登记、五个文件中的十一条已知链接、根入口直接消费者、源／镜像同步和确定路径；
5. 检查补丁格式；完成生命周期关闭后再使用同一无字节码调用运行最终 T-DOC。

Python 调用必须禁用字节码并启用 UTF-8，避免生成未列明 `__pycache__`；规则夹具只使用并自动清理系统临时目录，
T-DOC、结构校验、字节比较和补丁检查均不得写项目文件或外部状态。出现报告、缓存、快照、联网、依赖安装或其他
新副作用时停止并申请差额。普通验证不包含 `T-PROJECT-DOC-FORWARD`、全量测试或正式认证。

完成条件：历史记录全部进入归档且唯一登记，原根退出；根 README 恢复最短入口职责且消费者不断；三文件资产声明、
源文件和镜像一致；顶层所有权规则的正反夹具及当前项目门禁通过；当前真源无直接冲突；没有未列路径或残余候选。

### 收尾与联合复核

- 本方案主责与完成证明：骨架、历史生命周期、三文件资产和机械门禁由本方案统一证明；内容事实不在本方案内。
- 覆盖与残余：以第 2 节矩阵、17 文件清单、规则正反夹具和逐字节比较为准；内容与测试经济性保持未覆盖。
- 确定切片与就绪证明：第 3 节路径均有当前入口、职责、直接消费者或机械实现证据；可能路径只按列明条件进入。
- 关闭时的状态消费者：`docs/已知问题与待做需求.md`、`docs/方案/`、`archive/docs/README.md` 和最终 T-DOC。
- 关联方案、共享文件与对方职责状态：无关联活动方案；现有三个验证待办保持原状态，不由本方案关闭。
- 联合只读复核触发条件：不适用；没有其他关联方案，实施任务只执行本方案最终范围与漂移复核。
- 最终范围与漂移复核：确认最终入口与所有者、确定切片、五个文件中的十一条已列链接和修改路径新产生的一跳链接／消费者；不递归、
  不扫描整个工作区、不重做内容或测试设计审计。
- 验收停点：新增语义决定、历史正文需删除或合并、可能路径触发、验证升级、候选实质漂移或新副作用时停止申请差额。
- 关闭边界与未运行验证：完成条件满足后移除本待办，将方案移至
  `archive/docs/2026-08-08-DOC-SKELETON-RESIDUAL-20260808-当前项目骨架残余收口方案.md`，更新归档索引，清理空的
  `docs/方案/` 并运行最终 T-DOC；不包含 Skill 安装、commit、push、PR、发布、全量测试或正式认证。

## 5. 实施与验证结果

- 实施结果：17 份历史记录保持正文和相对层级迁入归档并逐份登记，七条跨根链接按新深度更新，四条同目录链接保持；
  根 README 已收缩，T-DOC 的三份源／镜像资产和当前真源声明已同步，顶层 Markdown 根所有权规则及正反夹具已加入。
- 授权差额：静态复核确认前向试用契约把标准验证固定为“两份资产”；用户已明确授权仅把该断言同步为“三份资产”，
  未运行 `T-PROJECT-DOC-FORWARD`，没有扩大其他路径。

| 验证项 | 状态 | 实际证据 |
| --- | --- | --- |
| `project-doc-skeleton` 结构校验 | `passed` | `quick_validate.py` 返回 `Skill is valid!` |
| T-DOC 规则夹具 | `passed` | 29 项测试全部通过 |
| 当前项目 T-DOC | `passed` | 退出码 0，0 warning |
| 三份标准资产逐字节比较 | `passed` | README 3049 字节、门禁 34628 字节、规则夹具 23120 字节，三组源／镜像均相等 |
| 归档和链接静态复核 | `passed` | T-DOC 接受 17 份唯一登记；五个文件的十一条链接全部存在，其中七条更新、四条保持 |
| 补丁格式 | `passed` | `git diff --check` 退出码 0 |
| 内容一致性审计 | `not_run` | 不属于本方案范围 |
| `T-PROJECT-DOC-FORWARD` | `not_run` | `explicit`，未获本轮执行授权且方案明确排除 |
| 全量测试与正式认证 | `not_run` | 未获授权，普通验证不能替代 |
| 生命周期关闭后的最终 T-DOC | `passed` | 待办退出、方案归档、索引更新和空方案目录清理后退出码 0，0 warning |

第一次三资产比较调用在进入比较前被 PowerShell 解析器拒绝，状态为 `inconclusive` 且没有写入；候选未变化，按协议
只重跑该项后通过。最终范围与漂移复核确认入口和所有者有效、修改路径均属于确定切片或已授权差额，没有新的一跳
消费者、项目级 Skill 范围扩张、缓存、报告、联网、安装或其他副作用。

关闭结果：本待办已退出活动清单，方案已按确定路径归档并唯一登记，空的 `docs/方案/` 已清理；关闭后的最终
T-DOC 通过。归档结果不依赖 commit、push 或 PR。

本轮用户已授权按方案实施及前向试用契约的单文件范围差额；commit、push、PR、发布、Skill 安装、全量测试、正式
认证和外部状态变更仍未获授权。
