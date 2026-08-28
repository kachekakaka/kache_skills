# PROJECT-DOC-SKELETON-GOVERNANCE-SLIM-20260828：骨架治理精简方案

- 状态：已完成
- 保存日期：2026-08-28
- 完成日期：2026-08-28
- 主责：`project-doc-skeleton` 的标准生命周期、方案交互、最小充分验证治理和 T-DOC 活动／归档分层；三个项目文档 Skill 的反哺报告退出由本方案统一同步
- 对应待办：`PROJECT-DOC-SKELETON-GOVERNANCE-SLIM-20260828`（完成后已从活动待办清理）
- 用户决定：采用最小充分治理；反哺报告从 Skeleton、Consistency、Contraction 及其活动直接消费者中完全退出；不读取、修改或验证其他项目
- 评审：完成 `2/2` 有界评审；第一轮发现并补齐 Contraction 直接消费者，修订后的第二轮未发现新范围问题
- 实施授权：用户于 2026-08-28 明确要求“实施”；授权覆盖本方案确定切片和普通验证，不包含安装、Git 提交或推送
- 仍未授权：Skill 安装、Git 提交、推送、前向矩阵、全量测试、正式认证、跨平台回归和其他项目验证
- 容器收尾：`docs/方案/` 由本次保存创建；方案归档后已确认目录为空并精确删除

## 1. 目标与边界

本方案修复上一版只完成测试选择收缩、却没有让下层规则和资产全部服从新治理结论的问题。实施以替换、删除和复用现有
结构为主，不新增 reference、Registry ID、测试文件、前向案例、能力矩阵、profile、manifest、后台清理器或第四个 Skill。

确定结果：

1. `待确认` 承接仍有未决语义或必要就绪条件的待办，可有零或一份活动方案；`待实施` 必须有且只有一份定稿、自包含、
   验证规划齐备且已经满足必要就绪条件的方案，但没有实施授权；`实施中` 必须有且只有一份方案并已取得本次实施授权。
2. 标准方案只固定完成证明、覆盖与残余、验证结果或未运行原因、生命周期关闭四类收尾信息。其他内容只在任务真实触发
   时出现，不生成“不适用”占位行。
3. 三个 Skill 不再询问或生成反哺报告。方案默认进行一次有界评审；只有发现会改变结论的问题才修订并追加一轮，最多
   两轮，仍不稳定则不保存。当前请求已明确要求保存且评审没有产生新范围、语义决定或授权差额时，直接一次保存；只要求
   形成方案时仍进入保存确认停点。保存不授权实施。
4. 普通验证、完整测试和正式认证都保持各自证明目标并选择最小充分证据。先复用候选、输入和失效条件未变的结果；必须
   运行时优先现有最小输入和最低副作用检查。只有证明目标被另一项完整覆盖时才删除重复测试，只有受支持入口、配置和
   消费者均不可达时才删除场景；一次未覆盖或历史无命中不足以证明不可达。
5. Skeleton 继续只负责结构和选择关系，不建立逐测试经济性审计引擎，不替目标项目自动删除测试，也不为骨架形式新增
   没有真实消费者的合成夹具。目标项目如需修改具体测试，只形成独立项目任务交接。
6. 成功关闭时精确清理本任务拥有的临时测试输出；失败、阻断或结论不明的现场只有记录所有者和复查日期才可暂存；历史
   留存必须显式指定，不后台自动删除，不处理所有权不明目标。
7. T-DOC 保持一个 Registry ID，提供 `active`、`archive`、`all` 三种组件选择；默认 `all` 保持现有直接调用兼容。
   普通活动文档任务使用 `active`，只有归档、恢复归档或归档路径／索引变化时选择 `archive`；两类输入同时变化时选择
   `all`。任何组件都只检查当前目标项目。

## 2. 确定实施切片

| 切片 | 确定路径 | 结果 |
| --- | --- | --- |
| Skill 交互 | 三个 `SKILL.md`、三个 `agents/openai.yaml` | 删除反哺报告和固定轮数首问；加入一次默认评审、一次条件追加及显式保存意图规则；保持显式调用和只读退出边界 |
| 生命周期与收尾 | `project-doc-skeleton/references/skeleton-rules.md`、`docs/README.md` | 修正三种状态与方案数量；九项模板缩为四类核心，条件模块不写占位项 |
| 最小充分验证 | `project-doc-skeleton/SKILL.md`、`references/testing-baseline.md`、`references/test-asset-structure.md`、`project-doc-shared/references/validation-planning.md`、`SoftwareTesting/PROTOCOL.md`、`SoftwareTesting/SAFETY.md` | 补齐最小输入、最低副作用、复用、删除证据和测试现场保留／清理规则，同时保持 Skeleton 不做逐测试实现审计 |
| T-DOC 分层 | 本仓库与 Skeleton 资产中的 `doc_consistency` 两个 README、两个 `test_doc_consistency.py`、两个 `test_doc_consistency_rules.py` | 增加组件选择；`active` 不遍历归档正文，`archive` 只枚举精确归档根，`all` 合并两者且不重复读取活动文件；更新生命周期规则 |
| 活动合同 | `docs/需求文档.md`、`docs/设计文档.md`、`SoftwareTesting/manual/project_doc_skills/README.md`、`contract-cases.md` | 同步三个 Skill 的交互、四类收尾、测试选择、T-DOC 组件和输出清理；原位收缩旧案例，不新增案例 |
| 机械职责断言 | `test_project_doc_skill_responsibilities.py`、`test_project_doc_contraction_confirmation.py` | 在现有真实合同检查中拒绝三个 Skill 和界面元数据重新出现反哺报告，替换旧“两轮、不生成”断言；不新增测试函数或临时夹具 |
| 决策真源 | `CONTEXT.md`、ADR-0009～0011、ADR-0013、ADR-0014 及 `docs/设计文档.md` 的 ADR 入口 | 保留访谈阶段已记录的术语、替代关系和决定；实施只修正发现的直接一致性差额，不扩写历史 ADR 正文 |

T-DOC 的 `active` 组件检查固定活动路径存在性、活动 Markdown、入口／链接、两跳可达性、顶层所有权、待办／方案、
Registry 和活动导航边界；它可以确认归档索引路径存在，但不解析归档表或枚举归档正文。`archive` 组件只检查
`archive/docs` 与存在时的 `archive/SoftwareTesting` 索引、登记唯一性、当前承接和归档正文集合。程序接口和命令行在未
指定组件时都使用 `all`；非法组件失败关闭。仓库源与 Skeleton 资产中的两个 Python 文件继续逐字节一致，两个 README
分别保留本仓库扩展职责和标准资产职责。

## 3. 条件路径与排除项

- `README.md`、`SoftwareTesting/README.md`、`docs/软件测试.md`：当前入口和单一 `T-DOC` 身份仍准确时只静态核对；只有
  实施结果使其失真才做最小同步。
- `project-doc-consistency/references/test-design-audit.md`：继续承接一致性审计不评价测试经济性的边界，不因 Skeleton 的
  结构选择规则而修改。
- `install_project_doc_skills.py` 与 `test_project_doc_skill_installer.py`：安装与 provenance 机制不变，不修改；交付阶段用
  现有入口安装并验证。
- 历史归档保留当时术语和执行记录，不批量改写；ADR 中为解释替代关系而保留的“反哺报告”历史文字不算活动入口残留。
- 不新增或运行前向矩阵，不执行全量测试、正式认证、产品进程、真实数据、网络验证或其他项目检查。
- 不读取、修改或运行 SM_GeoPlatform、F2、bili_workspace 及任何其他业务项目。

出现新语义决定、确定路径外必改消费者、需要新增测试文件／案例、组件分层无法保持现有规则能力、验证升级或新副作用时
停止，只申请差额。施工前重新冻结上述路径并保护既有修改。

## 4. 普通验证与交付顺序

保存阶段以下项目全部为 `not_run`。实施获授权后只执行现有最小集合：

1. 使用 `skill-creator` 现有 `quick_validate.py` 校验三个 Skill 的 frontmatter、名称和包结构。
2. 运行现有 `test_doc_consistency_rules.py`；原位改写生命周期和归档用例以同时证明 `active` 跳过归档、`archive` 捕获归档
   缺口、`all` 保持完整规则，不增加测试文件或用例数量。
3. 在一次现有 unittest 调用中运行 `test_project_doc_skill_responsibilities.py` 与
   `test_project_doc_contraction_confirmation.py`；其他职责测试的直接合同未变，保持 `not_run`。
4. 比较两组 Python 仓库源与 Skeleton 资产字节一致；静态确认活动消费者不再提供反哺报告、组件清单没有重复活动遍历，
   并执行差异格式检查。
5. 完成待办退出、方案归档、索引更新和空条件目录清理后，对最终候选运行一次 `T-DOC --component all`；只有失败修复或
   组件直接输入再次变化才重跑。

前向试用、全量测试、正式认证、跨平台回归、安装器自测试和其他项目验证均不属于本方案普通验证。

仓库验证与生命周期关闭完成后，若另行取得本方案范围的 commit、安装和 push 授权：先创建包含最终归档状态的本地提交；
安装器要求源仓库干净且 provenance 指向提交，因此再从该提交安装三个 Skill 并执行 `--verify-only`；安装验证通过后才
推送同一提交。安装失败时不推送，先报告精确失败和所需差额。

## 5. 四类收尾

- 完成证明：三个 Skill、下层 references、T-DOC 源／资产和活动直接消费者已一致承接本方案七项确定结果；两组 Python
  文件逐字节一致，活动入口不再提供已退出的额外过程交付物，`active` 不遍历归档正文，`archive` 只枚举精确归档根，
  `all` 保持兼容默认行为。
- 覆盖与残余：确定路径及一跳消费者均已处置；历史归档正文未批量改写，其他项目、前向矩阵、跨平台、安装器自测试、
  全量测试和正式认证均按方案保持 `not_run`，不用未运行层级支持更强结论。
- 验证结果或未运行原因：三个 Skill 的 `quick_validate.py` 均通过；`test_doc_consistency_rules.py` 的 29 个既有用例通过；
  职责与交互联合命令的 8 个既有用例通过；两组 Python 源／资产 SHA-256 分别一致；差异格式检查通过；生命周期关闭后的
  `T-DOC --component all` 通过且为 0 warning。首次职责联合命令暴露两条旧提示逐字断言，原位改为新提示的等价合同后
  仅重跑该命令并通过。
- 生命周期关闭：同 ID 活动待办已移除；本方案已移入 `archive/docs/` 并登记一次；本次创建的 `docs/方案/` 已在确认
  为空后精确删除；最终 `T-DOC --component all` 已通过。关闭未执行也不依赖 commit、安装、push 或 PR。
