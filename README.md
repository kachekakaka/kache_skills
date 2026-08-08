# kache_skills

本仓库开发和验证两个只能显式调用、运行时互不依赖的项目文档 Skill：

- [`project-doc-skeleton`](project-doc-skeleton/SKILL.md)：只读检查项目文档骨架、生命周期、测试治理和机械门禁；用户
  明确要求时只保存方案，后续由普通任务实施。
- [`project-doc-consistency`](project-doc-consistency/SKILL.md)：只读核对活动文档与当前事实；用户明确要求时只保存
  自包含方案，后续由普通任务实施。

当前长期说明从[项目文档](docs/README.md)进入，验证入口见[软件测试](SoftwareTesting/README.md)。

## 构建与交付

本项目无独立构建步骤。交付产物为 `project-doc-skeleton/` 与 `project-doc-consistency/` 两个目录；Skill 安装、
commit、push、PR 和发布仍需分别取得明确授权。

标准骨架路线的 T-DOC 从 `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/` 整文件交付并逐字节比较：

- [suite 说明](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/README.md)
- [文档机械门禁](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency.py)
- [门禁规则夹具](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency_rules.py)

## 验证入口

- [T-DOC](SoftwareTesting/doc_consistency/README.md)：验证标准骨架、活动入口、生命周期、归档和顶层 Markdown 根所有权。
- [项目文档 Skill 前向试用](SoftwareTesting/manual/project_doc_skills/README.md)：`explicit` 协议，不在普通验证中自动执行。

未完成事项统一登记在[已知问题与待做需求](docs/已知问题与待做需求.md)，历史实施和验证结果从
[文档归档](archive/docs/README.md)进入。
