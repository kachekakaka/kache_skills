# kache_skills

本仓库开发和验证三个只能显式调用、不会自动互相调用的项目文档 Skill：

- [`project-doc-skeleton`](project-doc-skeleton/SKILL.md)：只读检查项目文档骨架、生命周期、测试治理和机械门禁；用户
  明确要求时只保存方案，后续由普通任务实施。
- [`project-doc-consistency`](project-doc-consistency/SKILL.md)：只读核对活动文档的事实、契约、状态、所有权和直接
  消费者；用户明确要求时只保存纯一致性方案。
- [`project-doc-contraction`](project-doc-contraction/SKILL.md)：只在用户确认当前或指定的不可变提交已完成一致性整改并
  做过一致性验证后，只读审计重复、镜像、过程快照、职责错位和复杂内容；裸调用默认识别当前 `HEAD`，只问一次确认。

两个内容 Skill 共用的非可调用参考位于
[`project-doc-shared`](project-doc-shared/README.md)。它只提供长审计恢复与验证规划，不包含 `SKILL.md`，也不让
任一 Skill 调用另一个 Skill。

当前长期说明从[项目文档](docs/README.md)进入，验证入口见[软件测试](SoftwareTesting/README.md)。

## 构建与交付

本项目无独立构建步骤。交付时按用途安装：

- `project-doc-skeleton/`
- `project-doc-consistency/` + `project-doc-shared/`
- `project-doc-contraction/` + `project-doc-shared/`

Skill 安装、commit、push、PR 和发布仍需分别取得明确授权。取得安装授权后，推荐使用：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/install_project_doc_skills.py --apply --skills project-doc-consistency
```

安装器精确镜像目标目录，并在可调用 Skill 中生成 `SOURCE-PROVENANCE.json`；可用 `--verify-only` 复核源提交与逐文件
SHA-256。直接复制仍允许，但缺少或不匹配 provenance 时审计只能报告版本无法验证。

标准骨架路线的 T-DOC 从 `project-doc-skeleton/assets/SoftwareTesting/doc_consistency/` 整文件交付并逐字节比较：

- [suite 说明](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/README.md)
- [文档机械门禁](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency.py)
- [门禁规则夹具](project-doc-skeleton/assets/SoftwareTesting/doc_consistency/test_doc_consistency_rules.py)

## 验证入口

- [T-DOC](SoftwareTesting/doc_consistency/README.md)：验证标准骨架、活动入口、生命周期、归档、顶层 Markdown 根
  所有权，以及本仓库三个 Skill 的职责隔离、consistency 反证审计和安装 provenance 合同。
- [项目文档 Skill 前向试用](SoftwareTesting/manual/project_doc_skills/README.md)：`explicit` 协议；当前标准矩阵
  继续验证 skeleton 与 consistency 的既有用户可观察合同，不在普通验证中自动执行。

未完成事项统一登记在[已知问题与待做需求](docs/已知问题与待做需求.md)，历史实施和验证结果从
[文档归档](archive/docs/README.md)进入。
