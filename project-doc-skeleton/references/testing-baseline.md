# 精简测试基线

## 目录

1. 固定与条件结构
2. 验证层级
3. Registry
4. 测试入口职责
5. 仓库外测试现场
6. 结果与证据
7. 文档机械门禁
8. 资产自测试

## 1. 固定与条件结构

固定：

```text
SoftwareTesting/
├── README.md
├── PROTOCOL.md
├── SAFETY.md
└── doc_consistency/
    ├── README.md
    ├── test_doc_consistency.py
    └── test_doc_consistency_rules.py
```

按需：

```text
SoftwareTesting/<project-suite>/
SoftwareTesting/manual/
archive/SoftwareTesting/
```

产品命令、fixture、进程、端口和交付物必须来自用户确认或 `$project-doc-consistency check` 提供的事实证据；
骨架只建立承接位置，不自行推导或填写。默认不引入核心矩阵、多层快照、Release runner、产品锁、
lease、二进制审计或项目级测试 manifest。

## 2. 验证层级

### 普通验证

默认层级。按实际影响选择最小可证明范围，不自动执行完整测试集合。

### 全量测试

只有用户明确开启时进入。覆盖全部 `full`、本轮受影响的 `affected_only` 和用户明确加入的 `explicit`。

### 正式认证

只有用户明确要求时进入。包含必要全量测试、候选身份核对和结构化交接，不自动授权 commit、push、PR、
真实数据、发布或分发。

普通措辞不提升层级。clean build 是构建义务，不等于全量测试或正式认证。实际对外发布前仍未选择全量
测试或正式认证时停止询问。

活动方案中恰好各出现一次：

- 测试层级
- 验证影响域
- 具体验证项

没有活动方案的小修，在实施前说明和最终报告中记录同样三项。

## 3. Registry

`docs/软件测试.md` 的机器表格固定为：

```markdown
| ID | 执行类别 | 入口 | 唯一职责 |
| --- | --- | --- | --- |
| T-DOC | full | [文档机械门禁](../SoftwareTesting/doc_consistency/README.md) | 检查文档骨架机械一致性 |
```

ID 使用 `T-` 前缀、大写字母、数字和连字符。新 ID 不得复用当前 Registry、测试归档和可发现 Git
历史中的既有 ID。

类别：

- `full`：每次全量测试必须执行；
- `affected_only`：相关能力受影响时执行；
- `explicit`：真实数据、破坏性、联网费用或特殊环境，只有用户明确加入才执行。

`T-DOC` 必须存在且固定为 `full`。Registry 不保存日期、数量、耗时、run-id、哈希或结果。骨架只检查
ID、类别、入口和表格关系；具体测试项的类别与触发条件是否符合项目事实，由 `$project-doc-consistency check`
检查。

## 4. 测试入口职责

### SoftwareTesting/README.md

链接 Protocol、Safety、Registry 和每个活动 suite README。活动 suite README 必须直接可达。

### SoftwareTesting/PROTOCOL.md

保存验证层级、影响域、测试类别、构建与验证关系、结果语义、重试失效、全量与认证顺序和任务交接。
不保存项目具体命令、安全细节或动态结果。

### SoftwareTesting/SAFETY.md

保存测试根、真实数据保护、进程所有权、串行、输出 containment、人工清理和敏感信息规则。项目不涉及
真实数据或产品进程时明确写“不适用”，不编造流程。

### Suite README

保存 Registry ID、独有触发条件、输入、fixture、工作目录、规范命令、断言、失败语义和专项清理。
不复制公共规则或动态结果。骨架只建立其路径和入口；命令、fixture、覆盖声明和产物是否真实，由
`$project-doc-consistency check` 检查。

规范命令直接调用的运行器、运行时或软件包也属于该 suite 的依赖。若项目声明和已有入口未提供该依赖，
逐项确认它是项目管理的依赖、环境预置条件，还是应改用其他命令；不得一边记录依赖型命令，一边写
“外部依赖不适用”，也不得自行安装依赖。

相对命令必须同时确认工作目录。失败语义按执行阶段互斥：环境或前置条件不足通常是 `blocked`；测试已
进入可判定阶段后的断言、收集或项目错误可以是 `failed`；中断或运行器内部异常导致证据不可解释时是
`inconclusive`。项目可以调整具体边界，但不得让同一结果同时满足多个状态，也不得把所有非零退出码
笼统写成 `failed`。

## 5. 仓库外测试现场

默认测试根：

```text
<项目父目录>/<项目名>_test/
```

每次运行：

```text
<项目名>_test/<run-id>/
```

默认根已存在但没有当前项目合法所有权标记时停止，询问复用或改名。已有合法标记时先核对项目所有权。
输出解析后必须仍位于本次直接 run。符号链接、junction、reparse point 或路径逃逸失败关闭。

骨架只把这些约束写入测试治理文档，不提供创建、复用、检查或清理测试现场的运行工具。具体测试任务
需要创建 run 时，必须在自身授权范围内实现并验证所有权和 containment。测试输出默认保留；用户明确
要求清理时，由当前任务重新验证所有权、展示精确绝对路径并另行取得删除授权，只允许删除已确认属于
本次运行的精确 run 目录，不得删除测试根、其他 run 或项目目录。

测试不得修改真实数据库、配置、媒体或账号资料。只能管理本次启动并记录所有权的产品进程，禁止按名称
批量结束进程。

## 6. 结果与证据

动态状态使用：

- `passed`
- `failed`
- `blocked`
- `inconclusive`
- `not_run`

skip 只是项内计数，不能把缺失结论补成成功。同一候选只重跑失败、中断、blocked、inconclusive 或失效
项；产品输入、测试契约或候选身份变化后重新判断范围。

全量测试和正式认证的摘要位于仓库外，绑定验证层级、run-id、候选身份、实际范围、逐项结果和总体结论。
默认骨架不提供 evidence helper；项目首次实际需要时逐项设计。

## 7. 文档机械门禁

默认安装：

- `SoftwareTesting/doc_consistency/test_doc_consistency.py`
- `SoftwareTesting/doc_consistency/test_doc_consistency_rules.py`

这两个源码是经过统一夹具验证的通用资产。安装时必须从 Skill 的 `assets/SoftwareTesting/` 对应路径
逐字节复制并在验证阶段比较内容；不得手工转录、顺手优化或为单个项目制作分叉。目标路径已有不同内容
时停止并展示冲突，由用户决定保留、升级或另行处理。

门禁 error 只包含可以机械证明的问题：

1. 固定文件与条件文件关系；
2. 活动 Markdown 的 UTF-8 与 LF；
3. 普通行内相对链接和固定标题锚点；
4. AGENTS、README、文档入口和测试入口；
5. 活动文档两跳实际可达性；
6. 待办 ID、唯一状态和活动方案数量；
7. 方案中的三项测试决策；
8. Registry 结构、类别和 `T-DOC full`；
9. 归档唯一登记和当前承接；
10. 活动导航不直接链接归档正文。

warning 只包含：

- 当前活动文档中的绝对本地用户路径；
- 机器入口使用了不受支持的复杂 Markdown 语法。

门禁不检查：

- 文档是否符合代码或产品行为；
- 日期、测试结果、耗时、run-id 或哈希的内容职责；
- `CONTEXT.md` 和 ADR 内容；
- 秘密、真实数据或整个仓库的安全状态；
- 固定文案、篇幅、章节数量或文档总数。

机器入口使用普通行内相对链接和简单表格。正文 Markdown 保持自由。无法机械解析时明确报告 warning，
不得假装结构正确。

## 8. 资产自测试

每条会阻断项目的机械规则至少有一个正确夹具和一个错误夹具。每条 warning 至少验证一次触发和一次
不触发。新增或修改规则时必须在同一次变更中更新夹具。
