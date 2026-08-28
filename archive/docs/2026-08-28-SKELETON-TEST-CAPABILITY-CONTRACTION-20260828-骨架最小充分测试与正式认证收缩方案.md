# SKELETON-TEST-CAPABILITY-CONTRACTION-20260828：骨架最小充分测试与正式认证收缩方案

- 状态：已完成
- 保存日期：2026-08-28
- 修订日期：2026-08-28
- 完成日期：2026-08-28
- 主责：`project-doc-skeleton` 的标准测试选择、T-DOC 触发条件与 T-DOC 单次执行效率
- 对应待办：`SKELETON-TEST-CAPABILITY-CONTRACTION-20260828`（完成后已从活动待办清理）
- 用户决定：完整测试与正式认证按最小充分软件能力收缩；不新增测试收缩引擎、合成测试或固定前向矩阵；不使用任何现有业务项目实施或验收
- 实施授权：用户于 2026-08-28 明确要求“开始实施”，授权本方案确定范围内的文件修改、列明的普通验证、结果记录，以及完成条件满足后的待办清理、方案归档和索引更新
- 仍未授权：Skill 安装、Git 写入、全量测试、正式认证、固定前向矩阵、业务项目读取或验证，以及方案外新增测试或副作用
- 容器收尾：`docs/方案/` 由本方案首次保存创建；归档后已确认目录为空并精确删除

## 1. 目标与边界

本方案只收缩骨架默认施加的测试义务，并修复标准 T-DOC 的已知重复遍历。它不建立一套新的测试经济性审计流程，也不
让 Skeleton 自动检查或删除目标项目的测试实现。

已确认以下结果：

1. 完整测试是“最小充分能力证明集”，不是全部测试资产、参数组合或历史场景的并集。
2. `full` 只保留对所有候选都适用、且未被其他测试重复证明的最小核心能力；`affected_only` 只在对应能力或输入实际
   受影响时选择；`explicit` 继续只在用户明确加入后执行。
3. 正式认证不会自动扩大测试范围。骨架只规定：将来某个目标项目自行应用本规则时，只能选择该项目本次已经声明并
   实际交付的能力及其必要条件；骨架修改任务本身不读取、运行或认证任何其他项目。
4. 独立活动测试应有独有能力或故障模式。已有直接证据证明被其他测试完全覆盖、产品已退役，或在当前支持合同和生产
   前置约束下不可达的场景，不进入完整测试或正式认证；“历史上没发生过”不能单独证明不可达。
5. Skeleton 继续只负责结构和选择规则，不把上述判据扩张成逐测试审计引擎。目标项目以后是否合并或删除具体测试，仍由
   该项目在独立任务中依据自己的产品合同和实现证据决定。
6. 不新增 reference、ADR、持久能力矩阵、profile、manifest、测试类别或第四个 Skill。
7. 不新增合成测试，不修改固定前向案例，不运行 `T-PROJECT-DOC-FORWARD`，也不使用 SM_GeoPlatform、F2、
   bili_workspace 或任何其他业务项目作为夹具、试验场或验收现场。

## 2. 当前证据与修改理由

- `F-01`：[标准测试治理基线](../../project-doc-skeleton/references/testing-baseline.md)当前把全量测试定义为全部 `full`、
  受影响的 `affected_only` 和明确加入的 `explicit`，同时强制 `T-DOC` 为 `full`。产品源码变化即使没有改变文档输入，
  也会在完整测试中重复运行 T-DOC。
- `F-02`：同一基线要求标准方案逐项列规则夹具、目标 T-DOC、三份资产比较、静态复核和关闭后最终 T-DOC，没有按
  规则资产、镜像资产和目标文档输入分别判断触发条件。
- `F-03`：T-DOC 的 `_all_markdown()` 使用全树 `rglob` 后再过滤忽略路径；一次执行又从 Markdown 校验、链接图、顶层
  所有权和绝对路径等入口重复建立活动集合并重复读取内容。
- `F-04`：当前 Skeleton 已明确不评价覆盖率、断言质量和测试经济性。保留该职责边界即可避免普通骨架检查因为本次优化
  变成新的重型测试审计。
- `F-05`：当前 T-DOC 规则夹具已经覆盖标准机械规则，现有前向试用也已是 `explicit`。本次不需要再新增合成场景或执行
  固定前向矩阵。
- `F-06`：首次保存前工作树无本地修改；本方案与对应待办是首次保存产生的唯一写入。当前覆盖保存只修订这两份文件。

| 维度 | 当前结论 | 本方案处置 |
| --- | --- | --- |
| 完整测试选择 | `full` 成员和 T-DOC 容易被机械并入 | 收紧 `full` 的最小核心语义，T-DOC 改为 `affected_only` |
| 正式认证 | “必要全量测试”仍可能被理解为扩大矩阵 | 明确只证明目标项目自己声明的实际交付能力，不自动扩张 |
| 冗余与不可达 | 标准基线缺少排除原则 | 增加简短选择规则，不建立逐测试审计流程 |
| T-DOC 规划 | 规则夹具、镜像比较和目标门禁容易重复 | 分别按真实输入触发，最终候选只运行一次目标门禁 |
| T-DOC 实现 | 多次全树遍历和重复解码 | 单次剪枝清单并复用本轮内容 |
| 新测试与外部项目 | 不需要 | 不新增、不运行、不读取业务项目 |

## 3. 确定实施切片

### 3.1 收紧 Skeleton 标准测试选择

1. 在 `project-doc-skeleton/SKILL.md` 只增加一条边界说明：标准完整测试和正式认证不得被解释为全部测试资产或全部环境
   的机械并集；Skeleton 仍不审计测试覆盖、断言质量、重复实现或成本。
2. 在 `references/testing-baseline.md` 修订三个执行类别和两个验证层级：
   - `full`：所有候选都适用且没有等价替代的最小核心能力证明；
   - `affected_only`：对应能力、输入或已声明条件实际变化时执行；
   - `explicit`：继续遵守真实数据、产品进程、特殊环境和外部副作用授权；
   - 完整测试：全部 `full`、本候选实际触发的 `affected_only` 和用户明确加入的 `explicit`；
   - 正式认证：在上述最小集合上核对候选身份，不得自动增加目标项目未声明、未交付或无直接敏感性依据的平台与环境。
3. 在标准 Registry 说明中明确：“唯一职责”应表达独有能力或故障模式。重复证明、已经退役或有直接证据证明不可达的
   场景不作为完整／正式独立项；仅凭历史无命中不得删除。
4. 不要求 Skeleton 建立能力矩阵、读取全部测试实现或形成删除测试的实施切片；发现目标项目需要具体去重时，只报告
   项目级后续任务及所需证据。

### 3.2 调整标准 T-DOC 触发条件

1. 标准 Registry 中 `T-DOC` 从 `full` 改为 `affected_only`。标准门禁组件的直接输入包括活动 Markdown、归档索引、固定
   结构、Registry、门禁说明、实现和规则夹具；产品源码变化本身不触发该组件。
2. 本仓库的 T-DOC README 继续承接项目专属职责检查，但改为按组件的直接输入选择命令：Skeleton 源或相关职责合同变化
   时运行 `test_project_doc_skill_responsibilities.py`；Consistency、Contraction、独立审阅和安装器命令只在各自直接输入
   变化时运行，不因 T-DOC 被选择而机械全跑。
3. `affected_only` 相对普通实施任务开始时冻结的候选基线判断，使用能够覆盖已跟踪和未忽略新文件的当前变更集合。集合
   不能可靠形成、直接输入是否变化无法证明或已有证据已失效时，执行对应组件，不凭经验跳过。
4. 规则夹具只在 T-DOC 说明、实现、夹具或机械规则合同改变时运行。
5. `test_doc_consistency.py` 和 `test_doc_consistency_rules.py` 的本仓库源文件与 Skeleton 资产分别保持逐字节一致；两个
   README 因本仓库含项目专属职责命令而允许不同，改为分别静态核对标准职责和本仓库扩展职责。
6. 目标仓库门禁只在其直接输入变化时运行；普通实施任务完成目标文件和生命周期变更后，对最终候选运行一次。失败修复
   或之后直接输入再次变化才重跑。
7. 更新两个 T-DOC README、Registry 解析及现有规则夹具中关于 `T-DOC full` 的机械断言，不改变其他规则。

### 3.3 优化 T-DOC 单次执行

1. 在一次 `check_repository()` 调用内只建立一次 Markdown 资产清单，在进入标准 Skill 根、缓存和构建目录前完成剪枝，
   不先遍历再过滤。
2. 同一轮复用已解码文本、标题、链接、图和路径归属；每份活动 Markdown 最多解码一次。
3. 保留现有 Python 标准库约束、UTF-8／LF、链接、两跳可达性、生命周期、Registry、归档、顶层所有权、warning、错误
   文本和退出码语义。
4. 只重构共享扫描与读取方式，不趁机新增机械规则、目录 schema、测试类别或项目专用忽略项。

### 3.4 同步当前直接消费者

1. 更新 `docs/需求文档.md` 与 `docs/设计文档.md` 中 Skeleton 标准测试治理的简短当前合同；不复制完整算法。
2. 更新 `docs/软件测试.md` 和 `SoftwareTesting/PROTOCOL.md` 的 T-DOC 类别、完整测试和正式认证语义。
3. 在本仓库 T-DOC README 中把七个现有命令改为按直接输入选择，并保持每个命令原有职责；标准资产 README 只保留
   标准门禁命令，不复制本仓库扩展。
4. `SoftwareTesting/README.md`、根 `README.md` 和 Skeleton 界面元数据只做静态核对；当前说明仍准确时不修改。
5. 不修改 consistency、contraction、前向试用协议、contract cases、安装器或其他项目文档 Skill 测试。

## 4. 路径、顺序与排除项

### 4.1 确定路径

- `project-doc-skeleton/SKILL.md`
- `project-doc-skeleton/references/testing-baseline.md`
- `SoftwareTesting/doc_consistency/README.md`
- `SoftwareTesting/doc_consistency/test_doc_consistency.py`
- `SoftwareTesting/doc_consistency/test_doc_consistency_rules.py`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/README.md`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency.py`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency_rules.py`
- `docs/需求文档.md`、`docs/设计文档.md`、`docs/软件测试.md`
- `SoftwareTesting/PROTOCOL.md`
- 本待办、本方案，以及关闭时的归档方案与 `archive/docs/README.md`

### 4.2 条件路径

- `SoftwareTesting/README.md`、`README.md`：仅在直接职责说明因实施结果失真时最小同步。
- `SoftwareTesting/doc_consistency/test_project_doc_skill_responsibilities.py`：作为直接读取 Skeleton 源码的现有验证入口，
  本方案只运行、不修改；只有实施发现其现有合同断言与已确认新规则直接冲突时才停止并申请路径差额。
- 其他现有 T-DOC 机械测试不修改、不运行；其直接输入未变，且本方案会在 T-DOC README 中保留对应触发关系。

### 4.3 明确排除

- 不新增 reference、ADR、测试、前向案例、Registry ID、profile、manifest 或持久性能记录。
- 不修改 `project-doc-consistency/`、`project-doc-contraction/`、`project-doc-shared/`、前向试用协议和 contract cases。
- 不读取、修改或运行 SM_GeoPlatform、F2、bili_workspace 及其他业务项目。
- 不执行 `T-PROJECT-DOC-FORWARD`、全量测试、正式认证、产品进程、真实数据测试、网络、Skill 安装或 Git 写入。

### 4.4 实施顺序

普通实施任务先重新冻结工作树并保护用户修改；修订标准测试语义；修改 T-DOC 源实现和现有规则夹具，同步两个 Python
资产并分别更新两个 README；同步当前长期真源；执行第 5 节现有验证；完成最终范围复核后关闭生命周期。出现新的产品语义决定、必须新增测试、需要
访问业务项目、确定路径外消费者或验证升级时停止，只申请授权差额。

## 5. 验证与授权边界

- 测试层级：普通验证。
- 验证影响域：Skeleton 主入口与标准测试基线、T-DOC 触发和选择说明、两个标准 Python 门禁资产、当前需求／设计／
  Registry／协议，以及本方案生命周期最终状态。
- 具体验证项：以下六项现有校验；不新增合成测试或测试文件。

1. 使用 `skill-creator` 的现有 `quick_validate.py` 校验 `project-doc-skeleton/` 的 frontmatter、名称和包结构。
2. 运行现有 `test_doc_consistency_rules.py` 一次；因为本方案直接修改标准门禁实现和既有 Registry 断言，该项属于受影响
   普通验证。
3. 运行现有 `test_project_doc_skill_responsibilities.py` 一次；它直接读取本次修改的 Skeleton 源码，其他四个本仓库专属
   T-DOC 职责命令因直接输入未变而不运行。
4. 分别比较 `test_doc_consistency.py` 和 `test_doc_consistency_rules.py` 的本仓库源文件与 Skeleton 资产；两个 README
   不做逐字节比较，分别静态核对标准职责、本仓库扩展职责和按输入选择命令。
5. 运行差异格式检查，并静态确认所有 Markdown 枚举和读取均经本轮共享清单／缓存，核对确定路径、链接、Registry 和
   修改路径新产生的一跳消费者。
6. 完成第 6 节生命周期变更后，对最终仓库状态运行一次 `test_doc_consistency.py`；失败修复或其直接输入再次变化时才
   重跑。

不运行前向试用、全量测试或正式认证，不创建额外合成目录，不访问任何业务项目。方案保存阶段以上全部为 `not_run`。

## 6. 完成条件与生命周期关闭

### 6.1 关闭前就绪条件

1. Skeleton 和标准基线一致说明完整测试是最小充分能力集，正式认证不会自动扩大到目标项目未声明或未交付的条件。
2. `full`、`affected_only`、`explicit` 的选择边界清楚；标准合同要求独立活动项表达独有能力或故障模式，并禁止把历史
   无命中当成不可达证明。
3. 标准 `T-DOC` 为 `affected_only`，规则夹具、两个 Python 资产比较、本仓库职责命令和目标门禁分别按直接输入触发。
4. T-DOC 一轮只建立一次剪枝清单，每份活动 Markdown 最多解码一次，现有机械规则和错误语义不变。
5. 没有新增测试、前向案例、reference、ADR、矩阵、manifest 或业务项目依赖。
6. 第 5 节第 1～5 项验证通过；未运行层级和未受影响命令据实保持 `not_run`。
7. 最终范围复核只核对第 4 节确定路径、已列消费者及修改路径新产生的一跳关系，不递归、不审计业务项目。

### 6.2 生命周期变更与最终验收

关闭前就绪条件满足后，普通实施任务删除同 ID 活动待办，将本方案移入 `archive/docs/`、在归档索引登记一次，并确认由
本方案首次保存创建的 `docs/方案/` 已为空后精确删除。随后执行第 5 节第 6 项最终门禁：

- 通过时，在归档方案记录实际验证和完成日期，整体结论才成为已完成；
- 失败时，只在确定生命周期／文档范围内修正机械问题并重跑失效的最终门禁；需要新语义、确定范围外修改或新增副作用时
  停止并申请授权差额，不得提前宣称完成。

关闭不依赖 commit、push 或 PR。

## 7. 修订评审与当前残余

- 本次修订删除了原候选中的测试能力收缩引擎、新 reference、新 ADR、两个合成前向案例、固定前向矩阵改造、合成性能
  现场和跨 Skill 契约修改，避免用新的测试治理复杂度解决测试复杂度。
- 两轮静态复核分别确认：`F-01`～`F-06` 均有确定处置；标准规则仍能排除冗余和有证据不可达的正式选择，同时不会
  误把历史无命中当作删除证据，也不会让 Skeleton 默认读取测试实现。
- 本次 review 差额已修订：补齐三项方案字段；把两个 Python 文件的逐字节比较与两个 README 的职责核对分开；加入
  `quick_validate.py` 和 Skeleton 职责检查；固定 `affected_only` 基线与证据不足回退；拆分关闭前就绪和最终门禁。
- 用户于 2026-08-28 明确要求“开始实施”；本方案确定修改、关闭前普通验证、生命周期关闭和最终 T-DOC 均已完成。

## 8. 实施与验证记录

- 实施结果：已收紧 Skeleton、标准测试基线和当前项目协议；`T-DOC` 已改为 `affected_only`；两个 README 已分别改为
  标准组件／本仓库扩展组件按直接输入选择；T-DOC 已改为一次剪枝清单并缓存字节、解码文本、标题和文件级链接。
- `skill-creator` 的 `quick_validate.py`：`passed`，输出 `Skill is valid!`。
- `test_project_doc_skill_responsibilities.py`：`passed`，5 项通过；其直接输入在此后未变化。
- `test_doc_consistency_rules.py`：并行首跑因运行器未保留最终退出码而记为 `inconclusive`，同项重试 29 项通过；之后静态
  review 修正了目录词法归属并恢复全局排序，该直接输入变化使前一结果失效，最终重跑 29 项通过（13.920 秒）。
- 两组 Python 源／资产 SHA-256：分别相同；两个 README 已分别静态核对标准职责、本仓库七命令扩展职责和按输入选择。
- `git diff --check`：`passed`；静态复核确认 Markdown 枚举只由一次顶层剪枝 `os.walk` 清单提供，唯一字节读取位于缓存
  helper，解码、标题与文件级链接均复用本轮缓存；确定路径、Registry、根入口和一跳消费者无缺口。
- `test_project_doc_contraction_confirmation.py`、`test_project_doc_consistency_counterevidence.py`、
  `test_project_doc_independent_review.py`、`test_project_doc_skill_installer.py`、前向试用、全量测试和正式认证均按方案保持
  `not_run`。
- 最终 `test_doc_consistency.py`：`passed`，在待办退出、方案归档、索引更新和空目录清理后的最终候选上运行一次，输出
  `文档机械一致性检查通过（0 warning(s)）。`；此后只更新本归档正文的完成记录，不改变门禁活动输入。
