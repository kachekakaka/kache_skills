# 项目文档 Skill 共享参考

本目录不是可调用 Skill，不含 `SKILL.md`。它只保存多个项目文档 Skill 共用、但不属于任何一个业务职责的
小型参考：

- [`long-audit-protocol.md`](references/long-audit-protocol.md)：`S000`、`Axxx`、`Cnnn`、累计可恢复尾部、
  上下文恢复和最终索引；
- [`validation-planning.md`](references/validation-planning.md)：由只读审计 Skill 为后续普通实施任务规划
  动态验证、副作用、证据复用和终态边界。

安装 `project-doc-consistency` 或 `project-doc-contraction` 时，必须把本目录按同级路径一起安装。两个 Skill
都只读取共享参考，不调用彼此，也不从共享目录取得事实裁决或内容收缩结论。
