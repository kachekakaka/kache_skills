# kache_skills

本仓库开发三个只能显式调用、彼此独立的项目文档建议型审计 Skill：

- [`project-doc-skeleton`](project-doc-skeleton/SKILL.md)：只读发现入口、导航、所有者和活动／历史边界中的真实结构问题。
- [`project-doc-consistency`](project-doc-consistency/SKILL.md)：只读核对活动文档声明与一层直接事实，报告不一致和无法裁决的冲突。
- [`project-doc-contraction`](project-doc-contraction/SKILL.md)：只读识别重复、镜像、过程残留、内容错位和非必要复杂度，证据不足时保留内容。

三个 Skill 默认从目标项目自己的入口检查全部活动文档，事实证据只展开一层直接关系；入口无法可靠界定范围时报告未覆盖，
不改为全仓扫描。它们只交付简短问题清单和建议，不写项目、不形成方案、不管理生命周期、不运行验证，也不自动调用彼此。

本项目不再交付标准骨架、通用 T-DOC、共享长审计协议或目标项目测试资产。成熟项目保留自己的路径、治理和验证方式。

## 构建与交付

本项目无独立构建步骤。三个 Skill 都是自包含目录，可以分别交付：

- `project-doc-skeleton/`
- `project-doc-consistency/`
- `project-doc-contraction/`

Skill 安装、commit、push、PR 和发布分别需要明确授权。取得安装授权后，可使用：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/install_project_doc_skills.py --apply --skills project-doc-consistency
```

安装器精确镜像所选 Skill，并生成 `SOURCE-PROVENANCE.json` 供安装时或后续显式校验来源；该清单不是 Skill 运行前置，
也不证明审计结论正确。

## 验证与文档

- [轻量验证入口](SoftwareTesting/doc_consistency/README.md)：检查本仓库非历史 Markdown 本地链接、Skill 包装边界和安装器。
- [可选行为样例](SoftwareTesting/manual/project_doc_skills/README.md)：仅在用户显式要求时做隔离前向试用。
- [项目文档](docs/README.md)：当前需求、设计、待办和测试说明。
- [历史归档](archive/docs/README.md)：保留过往方案及其当时语境。
