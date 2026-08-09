# SKELETON-PYTHON-UTF8-VALIDATION-20260809：Python 文本验证运行编码方案

- 状态：已完成
- 保存日期：2026-08-09
- 主责：骨架候选对后续 Python 文本验证入口的运行编码就绪检查
- 决策依据：[项目术语](../../CONTEXT.md)、[需求文档](../../docs/需求文档.md)、[设计文档](../../docs/设计文档.md)
- 实施授权：用户已确认本方案并授权按第 3 节确定范围实施，覆盖列明的普通验证、结果记录及完成条件满足后的
  生命周期关闭。完整前向试用、跨平台回归、全量测试、正式认证、Skill 安装和 Git 写入不在范围。

## 1. 目标与已确认决定

本方案只解决 Python 文本验证依赖本地默认编码、从而在 Windows 等环境中忽略或误判编码问题的窄缺口：

1. 只约束 skeleton 新规划的、会读取文本的 Python 验证入口，不建立全项目文件编码门禁。
2. 新规划入口必须使用 `-X utf8` 或经当前证据证明等价的显式 UTF-8 运行模式；`-B` 继续独立负责禁止默认
   字节码缓存，两者不能互相替代。
3. 缺少显式 UTF-8 是可以机械查明的候选就绪缺口，由 skeleton 自行修订；修订完成前受影响评审不计入完成轮数，
   不把该事实包装成用户语义决定。
4. 在正确的显式 UTF-8 模式下仍发生 `UnicodeDecodeError` 或等价严格解码错误时，验证结果为失败；不得猜测 GBK
   等本地编码、使用替换字符继续或把环境依赖冒充通过。
5. 成熟等价项目已有的权威命令不自动改写。若它依赖 locale 默认编码，方案记录可移植性残余、影响和可能修订路径，
   未取得对应决定和授权前不迁移。
6. 不扩大 T-DOC 的活动 Markdown 集合，不扫描项目级 Skill 根，不修改 `.gitattributes`，不约束产品源码、产品测试、
   二进制、生成物或 vendor，也不改变 consistency Skill 的职责。
7. 该决定范围小且易于回退，不新增 ADR；`CONTEXT.md` 只定义“验证运行编码”与“文件存储编码”的概念差异，
   具体 Python 参数进入 skeleton 规则、需求和设计真源。

## 2. 初始证据与覆盖／残余矩阵

- 当前 `skill-creator/scripts/quick_validate.py` 使用未指定 `encoding` 的 `Path.read_text()`；本次 Windows 验证在省略
  `-X utf8` 时按本地 GBK 解码 UTF-8 中文并抛出 `UnicodeDecodeError`，改用显式 UTF-8 模式后同一结构校验通过。
- 当前 T-DOC 已要求活动 Markdown 使用 UTF-8 与 LF，其 README 中规则夹具和当前门禁入口都使用
  `python -B -X utf8`；文件存储编码规则不是本次缺口。
- 当前 `.gitattributes` 固定相关 Markdown、YAML 和门禁 Python 资产的 LF；本次决定不把行尾策略扩张为编码迁移。
- `project-doc-skeleton/SKILL.md` 已要求候选处理验证副作用和必要调用参数，但没有把文本验证运行编码列为就绪条件。
- 当前前向契约检查验证副作用、`-B` 和 `not_run`，尚未断言新规划的 Python 文本验证必须显式使用 UTF-8。
- 工作区已有上一事项的未提交修改，且与 `CONTEXT.md`、skeleton、需求、设计和前向契约重叠；这些内容属于既有证据，
  后续实施必须重新冻结并增量编辑，不得覆盖或回退。

| 标识 | 冻结对象 | 状态 | 候选处置与残余 |
| --- | --- | --- | --- |
| F-01 | Windows locale 导致 `quick_validate.py` 误解码 | 已覆盖（存在缺口） | 新规划的 Python 文本验证显式启用 UTF-8；外部脚本本身不修改 |
| F-02 | T-DOC 已有 UTF-8/LF 文件规则与 UTF-8 调用 | 已覆盖（满足） | 保持现有源、镜像和扫描范围，不重复造门禁 |
| F-03 | skeleton 候选就绪规则 | 已覆盖（存在缺口） | 在核心规则和标准验证参考中补窄约束 |
| F-04 | 长期行为与术语 | 已覆盖（存在缺口） | 同步通用术语、需求和设计，不创建 ADR |
| F-05 | 前向可观察断言 | 已覆盖（存在缺口） | 在现有 skeleton 落方案样本中增加最小场景和硬断言 |
| F-06 | 既有成熟命令与跨平台验证 | 已覆盖（保留残余） | 不自动改写；跨平台回归与完整前向试用继续保持未运行 |
| F-07 | 当前未提交重叠修改 | 已覆盖（需要保护） | 实施前重新冻结确定文件并只做增量编辑 |

## 3. 确定实施切片

### 3.1 术语与 skeleton 核心规则

1. 在 `CONTEXT.md` 增加“验证运行编码”：文本验证进程实际采用的解码模式，与被读文件的存储编码是两个独立事实；
   避免把 locale 误解码称为文件损坏，也避免用运行参数替代文件编码门禁。术语正文不写 Python 参数或实施步骤。
2. 修改 `project-doc-skeleton/SKILL.md`：
   - 在候选就绪与评审规则中要求，会读取文本的新增 Python 验证入口必须声明 `-X utf8` 或有证据的等价模式；
   - 缺失模式时由 skeleton 自行修订候选，修订前不计受影响评审轮次，不询问用户机械事实；
   - 明确显式 UTF-8 后的严格解码失败属于验证失败，不允许猜测或静默替换；
   - 对成熟项目已有命令只记录 locale 依赖残余和可能路径，不自动改写；
   - 保持 skeleton 自身只读，不在检查或候选评审中实际运行命令。
3. 修改 `project-doc-skeleton/references/testing-baseline.md`，在标准验证规划中承接运行编码要求，并明确该要求不扩大
   通用 T-DOC 的文件集合、规则职责或等价既有项目的迁移范围。核心停止条件保留在 `SKILL.md`，参考只承接标准路线细节。

### 3.2 长期行为与前向契约

1. 修改 `docs/需求文档.md` 的 skeleton 用户可观察行为：新规划的 Python 文本验证缺少显式 UTF-8 时，候选必须
   自修订；正确模式下的严格解码错误才计为验证失败；成熟权威命令不自动迁移。
2. 修改 `docs/设计文档.md` 的骨架候选流，把运行编码加入验证入口就绪检查，并保持“只记录必要参数、不预写完整
   命令或绑定施工者”的现有边界。
3. 修改 `SoftwareTesting/manual/project_doc_skills/README.md`，在 skeleton 落方案硬断言中加入相同可观察行为，
   明确它是验证入口就绪条件而不是新的文件扫描维度。
4. 修改 `SoftwareTesting/manual/project_doc_skills/contract-cases.md` 的现有 skeleton 落方案最小夹具：物化一个会读取
   含非 ASCII UTF-8 文本、但脚本自身依赖 Python 默认文本编码的验证入口；期望方案记录必要的显式 UTF-8 运行模式，
   不改外部验证脚本、不扩大 T-DOC、不自动转换文件。执行 Skill 的任务仍不得读取契约夹具。

### 3.3 确定路径与排除项

确定修改路径：

- `CONTEXT.md`
- `project-doc-skeleton/SKILL.md`
- `project-doc-skeleton/references/testing-baseline.md`
- `docs/需求文档.md`
- `docs/设计文档.md`
- `SoftwareTesting/manual/project_doc_skills/README.md`
- `SoftwareTesting/manual/project_doc_skills/contract-cases.md`
- 本待办、本方案，以及关闭时的精确归档文件和 `archive/docs/README.md`

静态核对但不预定修改：`project-doc-skeleton/agents/openai.yaml`，确认当前显示信息、默认提示和
`allow_implicit_invocation: false` 仍与 Skill 主责一致。

明确不修改：

- `project-doc-consistency/**` 及其界面元数据；
- 根 `README.md`、`docs/README.md`、`docs/软件测试.md`、`SoftwareTesting/README.md`；
- `.gitattributes`；
- `SoftwareTesting/doc_consistency/**` 与 `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/**`；
- 产品源码、产品测试、其他 Skill 资产、ADR 正文及现有三个验证类待办。

## 4. 验证、副作用与完成条件

- 测试层级：普通验证；不升级为完整 `T-PROJECT-DOC-FORWARD`、全量测试或正式认证。
- 验证影响域：skeleton 候选就绪规则、标准验证参考、长期行为、最小前向契约和现有界面元数据一致性。
- 具体验证项：
  1. 使用当前 `skill-creator` 的 `quick_validate.py` 校验 `project-doc-skeleton`，调用必须同时禁用字节码并显式启用
     UTF-8；不得复用依赖 locale 的默认调用；
  2. 静态核对 `SKILL.md`、`testing-baseline.md`、`agents/openai.yaml`、术语、需求、设计和两份前向契约的职责、
     触发条件、停止条件及排除边界一致；
  3. 使用禁用字节码且显式 UTF-8 的入口运行当前 T-DOC；
  4. 核对两组 T-DOC 源／镜像没有进入修改范围且三对文件仍逐字节一致；
  5. 运行 `git diff --check`，并核对最终修改路径没有越过第 3.3 节。

Python 验证均使用无字节码调用，不产生项目缓存、报告或快照；T-DOC、静态核对、字节比较和补丁检查只读，不创建
仓库外 run。若入口产生未列明文件、外部写入或需要安装／下载，停止并申请授权差额。方案保存时所有动态结果均为
`not_run`；实际实施与验证结果见第 6 节。

完成条件：

1. skeleton 能唯一判断新增 Python 文本验证入口是否具备显式 UTF-8 运行模式，并在缺失时自行修订候选且不计受影响
   评审轮次。
2. 显式 UTF-8 后的严格解码错误与 locale 误解码被明确区分，不使用猜测、替换字符或宽泛文件迁移掩盖失败。
3. 成熟项目已有权威命令保持不变，locale 依赖只作为残余或待决迁移候选。
4. T-DOC、`.gitattributes`、产品范围、Skill 根隔离和 consistency 职责没有扩张。
5. 术语、需求、设计、skeleton 核心、标准参考和前向契约一致，skeleton 结构校验、当前 T-DOC、源／镜像比较和
   补丁格式检查全部通过。
6. 最终范围与漂移复核没有覆盖既有未提交修改，也没有出现确定路径外的新语义决定、消费者或副作用。

完整 `T-PROJECT-DOC-FORWARD`、Linux/macOS 可移植性回归、全量测试、正式认证、Skill 安装、commit、push、PR
和发布保持 `not_run` 或不在范围，不阻止本方案按自身完成条件关闭。

## 5. 保存前候选结论与收尾

- 用户选择评审轮数：两轮；实际完成 `2/2`。
- 最终决定：采用窄运行编码约束；新增入口硬约束，成熟既有入口不自动迁移；不扩大文件编码门禁。
- 冻结发现、覆盖／残余矩阵和候选处置已完成成员与数量对账；没有待决语义切片或授权差额。
- 本节不保存逐轮评语、修订轨迹或独立 review 日志；实际实施与验证结果见第 6 节。

### 收尾与联合复核

- 本方案主责与完成证明：以第 1 节运行编码边界、第 3 节确定切片和第 4 节普通验证共同证明；不证明全部文件为
  UTF-8、所有项目跨平台可移植或完整前向行为已回归。
- 覆盖与残余：第 2 节矩阵；`VALIDATION-CROSS-PLATFORM`、完整前向试用及成熟项目命令迁移保持残余或范围外。
- 确定切片与就绪证明：第 3.3 节文件均承接规则、直接长期消费者或最小契约；T-DOC、`.gitattributes`、consistency
  和产品文件没有直接修改义务。
- 关闭时的状态消费者：skeleton 核心、标准验证参考、术语、需求、设计、两份前向契约、本待办、本方案及归档索引。
- 关联方案、共享文件与对方职责状态：当前没有其他活动方案；工作区存在上一事项的未提交修改，确定路径中的重叠
  文件必须增量保护；consistency 及上一事项归档不由本方案改变。
- 联合只读复核触发条件：不适用；本方案只修改 skeleton 主责及直接长期消费者，不自动调用其他 Skill。
- 最终范围与漂移复核：确认最终活动入口和所有者，核对确定路径、已列状态消费者及修改路径新产生的一跳链接／
  消费者；不递归、不扫描整个工作区、不重做完整结构或内容审计。
- 验收停点：出现成熟命令迁移、T-DOC 范围扩大、新文件编码政策、验证升级、新副作用、候选实质漂移或覆盖既有修改
  时停止并申请相应决定或授权差额。
- 关闭边界与未运行验证：完成条件满足后移除同 ID 待办，将本方案归档为
  `archive/docs/2026-08-09-SKELETON-PYTHON-UTF8-VALIDATION-20260809-Python文本验证运行编码方案.md`，更新归档索引，
  确认并清理本任务创建且为空的 `docs/方案/`，再运行最终 T-DOC。关闭不包含安装、Git 交付、完整前向试用、
  全量测试或正式认证。

## 6. 实施与验证结果

- `CONTEXT.md` 已增加“验证运行编码”术语；skeleton 核心规则已把新增 Python 文本验证入口的显式 UTF-8 模式纳入
  候选就绪条件，并区分 `-B`、严格解码失败和成熟命令残余；标准测试参考只承接必要运行参数和范围边界。
- 需求、设计与两份前向契约已同步可观察行为和最小非 ASCII UTF-8 夹具；没有扩大 T-DOC 文件集合、文件编码规则、
  项目级 Skill 根扫描、consistency 职责或产品范围，也没有修改外部验证脚本或成熟权威命令。
- `project-doc-skeleton/agents/openai.yaml` 静态复核通过：显示信息与默认提示仍匹配 Skill 主责，
  `allow_implicit_invocation: false` 未变。
- 使用 `python -B -X utf8` 运行当前 `skill-creator` 的 `quick_validate.py`：`passed`；当前项目 T-DOC 在施工后和
  生命周期关闭后均为 `passed`，`0 warning(s)`。
- 三份 T-DOC 源／镜像逐字节比较：`passed`；README、主门禁和规则夹具的 SHA-256 分别为
  `05C44FCFB2B1D5A1936EFA3CDDDDC1AA3B13134F2B09A5822ADA4B0B3D499C24`、
  `A139C3B9972F8C4B8A2C72D9E125E8C8E1F01E1E3E2A019861619C61B985B6C0`、
  `700348DD492AC585F66AC6AD2C5190433ACB6EF289D0B4976F2E0A3334BF6F2C`。
- `git diff --check` 在施工后和生命周期关闭后均为 `passed`。最终范围与漂移复核确认任务写入只涉及第 3.3 节
  确定路径及精确关闭消费者；既有重叠修改按当前工作树增量保留，界面元数据、T-DOC 源／镜像、`.gitattributes`、
  consistency、产品源码和产品测试没有进入本任务修改范围。
- 同 ID 待办已移除，方案已进入确定归档路径，归档索引已更新，本任务创建且为空的 `docs/方案/` 已清理。
  完整 `T-PROJECT-DOC-FORWARD`、Linux/macOS 回归、全量测试、正式认证、Skill 安装、commit、push、PR 和发布未执行。
