# 项目文档 Skill 轻量验证

本目录只验证三类有直接消费者的故障，不再提供标准骨架、Registry、方案生命周期或 T-DOC 资产同步门禁。

## Markdown 本地链接

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_markdown_links.py
```

脚本先在系统临时目录验证有效链接、失效相对链接和失效标题锚点，再扫描本仓库 `archive/` 历史根以外的 Markdown。
它不要求固定文件或目录，不检查生命周期和文案，不联网验证外链，也不扫描历史正文。

## Skill 包装边界

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_responsibilities.py
```

该入口检查三个 Skill 的名称、显式调用策略、自包含目录和无共享运行包。它不匹配生成文案、固定段落、源码 Token、
文件行数、测试数量或耗时；真实模型行为由可选隔离样例观察。

## 安装器

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_installer.py
```

该入口只在临时目录验证每个 Skill 独立镜像、陈旧目标清理以及来源清单的 `verified`、`mismatch` 和 `missing` 结果，
不安装个人 Skill。

三个命令都属于普通、只读或临时目录验证。只运行本次变更直接影响的入口；未运行项保持 `not_run`。
