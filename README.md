# kache_skills

本仓库用于开发和验证两个相互独立的项目文档 Skill。`project-doc-skeleton` 与 `project-doc-consistency` 当前都按
各自活动方案收缩为只检查与落方案的候选。未完成事项以活动待办和方案为准；尚未完成当前活动方案验收的候选
不应安装到个人 Skills 目录或用于批量修改项目。

- [项目文档](docs/README.md)
- [软件测试](SoftwareTesting/README.md)

## 构建与交付

本项目无独立构建步骤。

交付产物为：

- [`project-doc-skeleton`](project-doc-skeleton/)
- [`project-doc-consistency`](project-doc-consistency/)

命令、文件修改、commit、push、PR、发布和 Skill 安装均须分别获得明确授权，不得相互推定。

## project-doc-skeleton

[`project-doc-skeleton`](project-doc-skeleton/SKILL.md) 的中文显示名为“项目文档骨架检查与方案”。它只能显式调用：

- 开始处理一个新骨架问题且尚无对应活动方案时始终只读检查，即使请求包含修复或 `apply`；首次检查完整覆盖
  全部适用结构维度，不在首个缺口短路；
- 先冻结有限的结构维度和本轮文件集合，再在范围内充分读取，不限制为标题、链接 token 或固定行数；
- 检查结束只报告结构结论并询问是否保存方案；用户明确保存后形成并静态自审一份 `待确认` 方案，然后停止；
- 不提供 `apply`、施工、验证、重试或生命周期关闭能力；已有活动方案时默认交给普通实施任务，只有明确授权
  “仅修订方案”时才修改方案本身；
- 标准路线为新项目或明确迁移规划固定主干和条件模块；成熟既有结构按职责和必要安全结果证明等价后保留原
  路径、Registry schema、类别词汇和项目专用门禁；
- 只检查文件、目录、入口、导航、职责归属、生命周期、测试治理结构和机械门禁，不同步产品事实，不审计测试
  设计经济性，也不执行全项目安全认证；
- 保存的方案必须区分证据、决定、确定与可能路径、完成条件和结果，并实例化项目级收尾字段，使普通任务能够
  独立施工、验收并退出活动生命周期；
- 保存授权只覆盖方案及必要待办，不授权目标文件、命令、Git、安装或关闭，也不调用或依赖另一个 Skill。

### 标准路线通用资产

```text
project-doc-skeleton/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── skeleton-rules.md
│   └── testing-baseline.md
└── assets/SoftwareTesting/doc_consistency/
    ├── test_doc_consistency.py
    └── test_doc_consistency_rules.py
```

通用 T-DOC 只在标准骨架路线从 Skill 资产整文件逐字节安装并比较结果；不预设永久复制 helper，不能保证整文件
复制时停止，不以片段补丁替代。已证明等价的成熟项目保留项目专用门禁，不安装、不覆盖也不要求改名为 T-DOC。

`test_doc_consistency.py` 只检查标准路径、入口、链接、生命周期、四列 Registry 和归档关系；“待确认”待办可选
一份方案，“实施中”待办必须一份，其他状态禁用方案。
`test_doc_consistency_rules.py` 用隔离正反夹具验证门禁自身。两者都不判断正文事实或成熟既有治理是否等价。

## project-doc-consistency

[`project-doc-consistency`](project-doc-consistency/SKILL.md) 的中文显示名为“项目文档一致性检查与方案”。它也只能显式调用：

本节记录当前活动候选；完成状态以[活动待办](docs/已知问题与待做需求.md)及对应方案为准。

- 新问题始终只读检查；检查后询问是否保存，明确保存后写入并静态自审一份主责方案，然后停止；
- 只读取足以识别活动真源所有者的入口与职责声明，不重新认证标准骨架或六项治理；所有权不清时停止并形成
  skeleton 交接；
- 未限定项目文档范围时默认 `full`；明确文件、功能、声明或差异时使用 `incremental`，只展开一轮直接依赖，
  无法形成可靠边界时询问是否升级；
- 核对活动文档与当前代码、配置、构建或可观察行为，识别事实不一致、职责不清、内容膨胀和位置不当；
- 测试、CI 与安全实现只在它们是当前声明的直接证据，或用户明确要求测试设计审计时进入范围；
- 保存的主责方案正文聚焦目标、目标路径、动作边界、完成条件和验证要求，并实例化任务特定的“收尾与联合复核”；
  不预写脚本或精确命令；
- 不提供 `sync`、施工、验证或关闭能力；已有活动方案时默认由普通任务接手，只有明确授权“仅修订方案”时才
  修改方案本身；
- 保存的方案只把现有活动文档内容修订列为自身目标，结构、产品实现和测试实现问题继续精确交接，并让普通任务
  能够独立施工、验收和退出活动生命周期。

目录保持最小：

```text
project-doc-consistency/
├── SKILL.md
├── agents/openai.yaml
└── references/
    └── test-design-audit.md
```

## 验证入口

- [文档机械门禁](SoftwareTesting/doc_consistency/README.md)：验证本仓库当前标准骨架及通用 T-DOC 规则夹具。
- [项目文档 Skill 前向试用](SoftwareTesting/manual/project_doc_skills/README.md)：分别验证两个 Skill 的独立职责、阶段边界和范围收敛，属于 `explicit`，不在普通门禁中执行。
- 动态结果、运行时间和临时候选状态不保存在本 README；每次任务按实际执行结果交接。

未完成验证统一登记在[已知问题与待做需求](docs/已知问题与待做需求.md)。
