# 将结构治理与内容一致性重新收归各自 Skill

> 状态：部分被替代。结构治理与内容一致性分责继续有效；consistency 不再直接修订文档，按
> [ADR-0006](0006-consistency-ends-after-plan-handoff.md) 保存方案后退出；已就绪的产品、测试等跨职责切片可按
> [ADR-0008](0008-consistency-plan-coordinates-cross-responsibility-slices.md) 进入同一综合方案。

ADR-0002 曾要求 `project-doc-skeleton` 与 `project-doc-consistency` 各自独立证明同一组六项治理属性；实际试用表明，这会让内容审计重复承担结构认证、安全认证和机械门禁认证，造成职责重叠与能力膨胀。现决定由 `project-doc-skeleton` 独占骨架、入口、职责、生命周期、结构等价和机械门禁治理；`project-doc-consistency` 只核对文档与当前代码事实是否一致，并识别职责含混、内容重复或膨胀、内容放置不当，在授权后修订现有文档内容。

本 ADR 替代 ADR-0002 中“两个 Skill 共享六项治理账本并分别认证治理等价”的决定；ADR-0002 关于不新增 profile/manifest、允许 skeleton 按治理结果保留成熟既有结构的决定继续有效。测试、CI 和安全实现只有在它们是某项文档声明的直接证据时才进入一致性审计，不再自动扩展成独立的项目治理认证。两个 Skill 发现超出自身职责的问题时提供精确交接，不自动调用对方，也不继承授权。

“不修改产品测试”按断言职责而不是文件路径判断。`project-doc-skeleton` 可以在施工授权内最小修改直接约束已确认路径、入口、生命周期或自动化副作用的结构机械断言；即使这些断言与产品测试位于同一文件，也不得修改版本、API、数据库、权限、下载或其他产品行为断言，无法可靠分离时必须停止并交接。`project-doc-consistency` 继续不修改任何可执行测试代码，只形成事实或测试实现交接。
