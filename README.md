# kache_skills

本仓库用于开发和验证两个相互独立的项目文档 Skill。当前 `project-doc-skeleton` 职责收缩第一阶段施工候选已
落地，处于独立验收前停点；`project-doc-consistency` 仍由独立待办继续收敛。Skill 在完成适用校验和独立验收
前，不应安装到个人 Skills 目录或用于批量修改项目。

- [项目文档](docs/README.md)
- [软件测试](SoftwareTesting/README.md)

## 构建与交付

本项目无独立构建步骤。

交付产物为：

- [`project-doc-skeleton`](project-doc-skeleton/)
- [`project-doc-consistency`](project-doc-consistency/)

命令、文件修改、commit、push、PR、发布和 Skill 安装均须分别获得明确授权，不得相互推定。

## project-doc-skeleton

[`project-doc-skeleton`](project-doc-skeleton/SKILL.md) 的中文显示名为“项目文档骨架与结构治理”。它只能显式调用：

- 新一轮首次调用始终只读检查，即使请求包含修复措辞；检查完整覆盖上下文、结构职责、导航、活动/历史、
  待办/方案/记录、测试治理和机械门禁等全部适用结构维度，不在首个缺口短路；
- 先冻结有限的结构维度和本轮文件集合，再在范围内充分读取，不限制为标题、链接 token 或固定行数；
- 检查结束只报告结构结论并询问是否保存方案；用户明确保存后形成 `待确认` 方案，完成裁决且再次选择施工后
  才允许 `apply` 或其他方式写入；
- 标准路线为新项目或明确迁移建立固定主干和条件模块；成熟既有结构按职责和必要安全结果证明等价后保留原
  路径、Registry schema、类别词汇和项目专用门禁；
- 只管理文件、目录、入口、导航、职责归属、生命周期、测试治理结构和机械门禁，不同步产品事实，不审计测试
  设计经济性，也不执行全项目安全认证；
- 施工授权内只允许最小修改可与产品行为分离的结构机械断言；退出旧入口前核对引用、默认配置、启动接线、
  自动化触发、运维入口和结构断言组成的直接消费者闭包，遇到产品行为选择时停止；
- 申请命令授权前在对话中建立临时验证执行账本；自动化或外部副作用裁决先说明会发生、不会发生和既有状态，
  生命周期关闭后必须对最终状态重跑适用门禁；
- 文件修改、命令、Git 和安装分别授权，不调用也不依赖另一个 Skill。

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

[`project-doc-consistency`](project-doc-consistency/SKILL.md) 的中文显示名为“项目文档一致性”。它也只能显式调用：

本节记录当前尚未收缩的候选实现；ADR-0003、ADR-0004 对应变更登记在
[独立待办](docs/已知问题与待做需求.md#doc-consistency-responsibility-refactor收缩一致性-skill-职责)，不会随 skeleton 阶段自动施工。

- `check` 默认只读；`sync` 先执行相同检查，再最小同步现有活动文档中可直接证明的事实；
- 每次都从当前证据重新核对与骨架 Skill 相同的六项治理属性，但运行时互不调用、不共享 profile 或 manifest；
- `full` 同时给出六项治理账本和项目内容覆盖账本；`incremental` 只判断变更及依赖闭包的内容一致性，无法
  可靠界定范围时失败关闭并询问是否升级；
- 测试审计建立“权威契约 → 实现 → 测试义务 → Registry/suite → 实际断言 → CI”证据链，识别覆盖缺口、
  声明错位、有意重叠、冗余候选和过度候选；
- 安全审计核对 CI 默认触发、路径过滤、真实数据/进程规则、输出根、owner marker、containment、保留和删除实现；
- `sync` 在明确修复授权下不逐文件重复确认，但不创建或移动文件、不改变结构、不修改可执行测试代码；测试
  实现缺口形成独立交接。

目录保持最小：

```text
project-doc-consistency/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── entry-freeze-procedure.md
    └── test-design-audit.md
```

## 验证入口

- [文档机械门禁](SoftwareTesting/doc_consistency/README.md)：验证本仓库当前标准骨架及通用 T-DOC 规则夹具。
- [项目文档 Skill 前向试用](SoftwareTesting/manual/project_doc_skills/README.md)：当前协议仍待 consistency 独立阶段按代表性样本收敛，属于 `explicit`，不在 skeleton 普通门禁中执行。
- 动态结果、运行时间和临时候选状态不保存在本 README；每次任务按实际执行结果交接。

未完成验证统一登记在[已知问题与待做需求](docs/已知问题与待做需求.md)。
