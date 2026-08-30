# PROJECT-DOC-ADVISORY-AUDIT-20260830：项目文档 Skill 建议型审计轻量化方案

- 状态：已完成
- 保存日期：2026-08-30
- 完成日期：2026-08-30
- 对应待办：`PROJECT-DOC-ADVISORY-AUDIT-20260830`（完成后从活动待办清理）
- 用户决定：保留三个现有 Skill 名称；全部改成显式、只读、只报告的建议型审计；默认检查全部活动文档，但事实证据只展开一层直接关系；不再由 Skill 形成方案、管理生命周期或实施
- 设计依据：[ADR-0015](../../docs/adr/0015-document-skills-are-advisory-auditors.md)、[ADR-0016](../../docs/adr/0016-stop-shipping-the-generic-doc-gate.md)、[ADR-0017](../../docs/adr/0017-full-active-docs-compact-report.md)、[ADR-0018](../../docs/adr/0018-evidence-not-governance-compliance.md)、[ADR-0019](../../docs/adr/0019-compatible-names-and-behavioral-checks.md)
- 实施授权：用户于 2026-08-30 明确要求“补齐后实施”；覆盖本方案确定修改、精确删除、普通验证与生命周期关闭
- 仍未授权：安装个人 Skill、commit、push、PR、前向试用、全量测试、正式认证、跨平台回归和其他项目验证
- 测试层级：普通验证（已执行）；未升级
- 验证影响域：三个 Skill 包、显式安装器、本仓库轻量文档自检、少量行为回归及其活动一跳文档消费者
- 具体验证项：三个包的 `quick_validate.py`、轻量 Markdown 链接检查、Skill 包装／边界检查、安装器单元测试、删除路径的活动直接引用复核和 `git diff --check`
- 容器收尾：`docs/方案/` 由本次保存创建；方案归档后已确认目录为空并精确删除

## 1. 目标与确定边界

本次不推倒重建三个 Skill，也不把它们合并成通用治理框架。实施结果必须同时满足：

1. 保留 `project-doc-skeleton`、`project-doc-consistency`、`project-doc-contraction` 三个名称和显式调用策略；三个 Skill 仍不自动调用彼此。
2. 三个 Skill 都只读取目标项目，交付问题、直接证据、影响、建议和未覆盖边界后停止；不写目标项目，不生成或保存方案，不登记待办，不改变生命周期，不判断实施就绪，不实施建议。
3. 用户未限定文件或主题时，从项目当前文档入口识别并逐份检查全部活动文档；明确给出范围时只检查该范围。当前入口不足以可靠界定活动范围时，报告范围不明与未覆盖内容，不退化为全仓扫描，也不自行规定标准路径。源码、测试、CI、配置、历史和归档不自动全量扫描，只在裁决某条声明确有需要时读取一层直接证据。
4. 输出使用简短问题清单，不生成 `S000/Axxx/Cnnn/Rxxx`、覆盖矩阵、审计轨迹、固定评审轮次或独立复审包。高风险发现只建议使用对应专业审查，不把当前 Skill 扩张成安全、协议、合规、架构或测试体系治理。
5. Skeleton 只报告真实结构问题：入口或链接失效、竞争所有者、活动与历史边界不清。成熟项目已有等价治理时默认复用；缺少标准文件、路径不同、没有 Registry 或没有自动门禁都不单独构成问题。
6. Consistency 只核对文档声明与当前直接事实是否一致。当前权威不能裁决时报告冲突证据、影响和可选处理方向，留给后续普通任务决定；不在审计内持续访谈，也不把一处测试或 CI 证据扩张为测试体系治理。
7. Contraction 直接基于当前活动文档和一层证据提出删除、合并、迁移、摘要或简化建议；不要求不可变 SHA、干净工作树、事先完成一致性整改或验证。事实、所有者或消费者不清时将对应内容列为保留项，同时继续检查其他独立内容。
8. 三个 Skill 在建议新增规则、文档或测试前都应用同一道反过度治理门：保护的具体行为或合同、真实消费者、已经发生或合理预期的失败、已有证据为何不足、何时可以删除。任一项没有答案，只给可选建议，不建议形成长期项目资产。

## 2. 确定实施切片

| 切片 | 确定路径 | 实施结果 |
| --- | --- | --- |
| 三个运行入口 | `project-doc-skeleton/SKILL.md`、`project-doc-consistency/SKILL.md`、`project-doc-contraction/SKILL.md` | 各自改为自包含的轻量建议型审计；保留职责差异、完整活动文档范围、一层直接证据、简洁报告和只读停点 |
| 界面元数据 | 三个 `agents/openai.yaml` | 缩短显示说明和默认提示，明确 `$skill-name`、只读审计和简短建议；保留 `allow_implicit_invocation: false` |
| 旧运行支持 | 三个 Skill 的 `references/`、Skeleton 的 `assets/`、`project-doc-shared/` | 将仍需的少量判据收进对应 `SKILL.md` 后精确删除；不建立新的共享协议或资源目录 |
| 安装交付 | `SoftwareTesting/doc_consistency/install_project_doc_skills.py`、`test_project_doc_skill_installer.py` | 每个 Skill 只镜像自身目录；保留显式安装和来源清单／校验能力，但 Skill 运行时不检查 provenance，也不依赖共享目录 |
| 本仓库文档自检 | `SoftwareTesting/doc_consistency/test_doc_consistency.py`、`test_doc_consistency_rules.py`、该目录 README | 删除标准骨架、固定路径、Registry、生命周期、文件白名单和源／资产同步规则，替换成一个只捕获活动 Markdown 失效相对链接或锚点的小型只读检查 |
| Skill 回归 | `test_project_doc_skill_responsibilities.py`、三个旧流程专项测试、`SoftwareTesting/manual/project_doc_skills/` | 保留一个小型包装／边界检查和少量隔离行为场景；删除不可变基线、长反证、独立复审和精确文案 Token 合同 |
| 活动说明 | 根 `README.md`、`docs/README.md`、`docs/需求文档.md`、`docs/设计文档.md`、`docs/软件测试.md`、`SoftwareTesting/README.md`、`PROTOCOL.md`、`SAFETY.md`、`SoftwareTesting/doc_consistency/README.md` | 同步新的产品合同、模块结构、安装方式、轻量测试入口和本项目自用生命周期边界；不再把本项目治理当成目标项目标准 |
| 决策与历史入口 | `CONTEXT.md`、ADR-0015～0019、`docs/设计文档.md` 的 ADR 索引、`archive/docs/README.md` | 保留已记录术语和决定；标明旧决定被替代的范围；只修正归档索引中将因删除现行 reference 而失效的直接链接，不改写历史方案正文 |

## 3. 精确删除、替换与保留

实施时先复核下列文件仍是本方案识别的直接消费者，再进行精确删除。

删除的 Skill 支持文件：

- `project-doc-skeleton/references/skeleton-rules.md`
- `project-doc-skeleton/references/testing-baseline.md`
- `project-doc-skeleton/references/test-asset-structure.md`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/README.md`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency.py`
- `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency_rules.py`
- `project-doc-consistency/references/counterevidence-audit.md`
- `project-doc-consistency/references/test-design-audit.md`
- `project-doc-contraction/references/content-contraction.md`
- `project-doc-shared/README.md`
- `project-doc-shared/references/long-audit-protocol.md`
- `project-doc-shared/references/independent-plan-review.md`
- `project-doc-shared/references/validation-planning.md`

删除或替换的本仓库测试文件：

- 删除 `SoftwareTesting/doc_consistency/test_doc_consistency.py` 和 `test_doc_consistency_rules.py`，新增一个职责单一的 `test_markdown_links.py`。
- 原位重写 `test_project_doc_skill_responsibilities.py`，只检查三个包可显式调用、元数据有效、没有随附 T-DOC／共享运行依赖等可观察包装边界；不检查固定文案、段落、Token 数量、源码行数、固定测试数量或耗时。
- 删除 `test_project_doc_contraction_confirmation.py`、`test_project_doc_consistency_counterevidence.py` 和 `test_project_doc_independent_review.py`；它们只证明已经退出的前置确认、长反证和独立复审流程。
- 收缩 `SoftwareTesting/manual/project_doc_skills/README.md` 与 `contract-cases.md`，取消固定五样本矩阵、方案接力和长期运行记录要求；只保留可在用户显式授权后执行的隔离行为样例。

明确保留：

- `install_project_doc_skills.py` 及其小型单元测试，因为个人 Skill 的显式安装仍有真实消费者；来源清单只证明安装包来源和镜像结果，不成为审计结果正确性的前置认证。
- 本仓库自己的待办、活动方案和归档生命周期，因为它们仍由当前项目协作流程消费；轻量链接检查不再强制其他项目复制这套结构。
- 历史 ADR 和归档方案正文，保留当时语境；活动设计索引用“被替代／部分被替代”说明当前关系。

## 4. 少量行为回归场景

行为样例只验证用户能观察到的边界，不绑定模型的逐字措辞：

1. 成熟小项目已有等价入口、所有者和活动／历史边界时，Skeleton 报告没有真实结构问题，产生零写入、零新文档、零新测试。
2. 项目以固定文案、路径白名单、源码 Token、固定数量或性能耗时作为治理断言时，对应 Skill 指出脆弱性和实际风险，不把这些断言复制成新标准。
3. 同一行为已经由一个直接测试证明时，审计不再要求 CI、另一套 suite 或新证据格式重复证明。
4. Consistency 只读取裁决声明所需的一层源码、测试、配置或 CI 证据，报告冲突但不修改产品代码，也不建设架构、安全或测试治理方案。
5. 没有真实消费者和失败模式时，三个 Skill 不建议建设证据 schema、保留策略、运行账本或 GC 工具。
6. 治理设施明显重于被治理内容时，报告成本和收缩方向；Contraction 对不确定内容采用保留项，不为删除少量文字先生成更大的审计设施。

前四项覆盖三个 Skill 的主边界，后两项覆盖共用反过度治理门。实现中只有发现新的、独立且合理预期的失败类型时才增加场景；不得为凑数量扩充夹具。

## 5. 反过度治理门对本方案资产的核对

| 资产 | 保护对象与消费者 | 失败与现有证据缺口 | 删除条件 |
| --- | --- | --- | --- |
| 三个 `SKILL.md` | 保护显式调用者得到职责明确、只读且有界的审计 | 当前合同会扩张为方案和治理体系；包装检查不能代替行为说明 | 对应 Skill 退役或职责被明确合并 |
| `test_markdown_links.py` | 保护仓库维护者能从活动入口到达真实目标 | 失效链接是直接故障；旧 T-DOC 用大量无关规则证明 | 仓库不再以 Markdown 提供入口，或已有同一入口完整覆盖 |
| 包装检查与行为样例 | 保护维护者修改 Skill 时不恢复写入、长流程或无界取证 | 单看 YAML／目录不能证明用户可观察边界，单看人工样例不能证明包装 | 有更小的现有检查完整覆盖同一失败类型 |
| 显式安装器 | 保护选择安装的用户获得完整、可追溯的独立 Skill 包 | Skill 行为测试不覆盖文件镜像和来源漂移 | 项目不再提供本地安装方式或由现有安装机制完整替代 |

不新增证据 schema、持久运行记录、保留策略、GC、性能门槛、文件数量门槛或新的测试 Registry。

## 6. 实施顺序与停止条件

1. 实施开始时把本待办改为 `实施中`，重新读取当前工作区差异，保护讨论阶段已经写入的 `CONTEXT.md` 和 ADR-0015～0019，不覆盖用户或其他任务的新修改。
2. 先重写三个 `SKILL.md` 与 `agents/openai.yaml`，再删除已失去消费者的 references、Skeleton 资产和共享目录；不得先删后猜运行合同。
3. 更新安装器的独立包映射和单元测试，再收缩本仓库链接检查、Skill 包装检查及可选行为样例。
4. 同步活动需求、设计、测试和入口文档；对删除路径做一跳直接引用复核，只最小修正归档索引，不扫描或改写归档正文。
5. 运行本方案列明的普通验证，修复范围内失败；随后完成待办退出、方案归档、索引更新和空条件目录清理，再对最终状态运行一次轻量链接检查。

如果实施发现必须新增第四个 Skill、共享运行协议、目标项目资产、持久证据设施、产品代码改动、未列明测试文件，或需要决定是否保留现有 Skill 名称和职责，应停止并申请语义或授权差额。普通验证失败只在本方案确定范围内修复；需要全量测试、实际安装、外部项目试用或新副作用时另行授权。

## 7. 普通验证与交付

实施获授权后执行以下最小集合：

1. 使用已安装 `skill-creator` 的 `quick_validate.py` 分别校验三个 Skill 包的 frontmatter、名称和目录结构。
2. 运行 `python -B -X utf8 SoftwareTesting/doc_consistency/test_markdown_links.py`，先以小型临时夹具证明有效链接通过、失效相对链接或锚点失败，再检查本仓库 `archive/` 历史根以外的 Markdown；不设置必需文件白名单，不联网验证外链，也不扫描历史归档正文。
3. 运行 `python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_responsibilities.py`，验证三个包的显式调用和无随附治理资产边界。
4. 运行 `python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_installer.py`，验证每个 Skill 独立镜像、来源清单的 `verified/missing/mismatch` 结果和无共享目录依赖。
5. 静态确认活动文件不再引用本方案删除的共享协议、Skeleton 资产和旧流程测试；确认三个 YAML 都保留 `allow_implicit_invocation: false`，并执行 `git diff --check`。

`SoftwareTesting/manual/project_doc_skills/` 的隔离行为样例保持 `explicit` 和 `not_run`；个人 Skill 安装、`--verify-only`、全量测试、正式认证、跨平台回归、其他项目检查、commit、push 和 PR 都不属于普通验证，也不能由静态结果冒充通过。

## 8. 四类收尾

- 完成证明：三个名称不变的 Skill 已成为自包含、显式、只读、只报告且一层取证的建议型审计；旧共享协议、Skeleton T-DOC 资产和流程型测试已退出活动树；安装器只交付独立包；活动文档已同步新合同。
- 覆盖与残余：确定路径和删除路径的一跳活动消费者均已处置；历史 ADR／归档正文保持原貌，正文中的退役路径文字或旧链接不批量改写，只修复当前归档索引；显式行为试用、个人安装、其他项目、跨平台、全量测试和正式认证均为 `not_run`，结论不外推到这些范围。
- 验证结果或未运行原因：三个 `quick_validate.py` 均通过；链接检查的 2 项自测试和本仓库非历史 Markdown 检查通过；安装器 4 项通过；包装检查首次因补丁工具遗留的空目录失败，核实为空并精确删除后 2 项通过；活动 Markdown 旧引用扫描无命中，`git diff --check` 通过。隔离行为样例未执行，因此只证明源码合同与包装边界，不声称真实模型行为已经通过前向验证。
- 生命周期关闭：同 ID 活动待办已移除，本方案已归档并登记；本次创建的 `docs/方案/` 已在确认为空后精确删除；关闭后的最终轻量链接检查通过。关闭未执行也不授权 commit、安装、push 或 PR。
