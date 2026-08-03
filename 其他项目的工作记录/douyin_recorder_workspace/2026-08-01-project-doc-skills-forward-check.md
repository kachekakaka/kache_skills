# douyin_recorder_workspace 项目文档 Skill 前向试用

## 范围与边界

- 模式：project-doc-consistency check、project-doc-skeleton check。
- 两个模式使用独立新任务。
- 全程只读；未运行命令、未修改目标工程、未执行 Git 或联网。
- 工作记录不复制 workflow 中的真实房间标识或现场内容。

## 主要发现

1. 权威契约要求首事件前 recipient 状态为 Unknown；当前代码创建 Waiting(waiting_first_event)，多项单元和
   集成测试还把 Waiting 当作正确结果，属于实现不一致和测试声明错位。
2. 核心文档明确承认生产 IM adapter 尚未接线，但 docs/已知问题与待做需求.md 为空，缺口没有活动生命周期。
3. Registry 只有 T-DOC；仓库实际存在大量 unit、integration、replay、媒体、稳定性、Windows、发布和
   live-preflight 入口，无法按 full、affected_only、explicit 可靠选测。
4. SoftwareTesting/SAFETY.md 要求真实现场或特殊环境测试必须 explicit 并取得授权；live-preflight workflow
   却会在 feature push 和 PR 自动使用预置真实房间执行联网 HTTP/CDP 探测并上传报告。
5. T-DOC 声明为 full，但 CI 和 verify.bat 均未调用两条规范命令。
6. 大量已完成计划、实施报告、审查、历史架构和 release/probe/replay 材料仍在活动导航；归档索引只登记
   两份工作记录。
7. AGENTS.md 保存产品事实、阶段状态和专项规则，并存在默认 commit/push 与分别授权基线的冲突。
8. recipient 数据库 replay 单元测试与 CI CLI replay 验证不同边界，属于有意重叠；没有直接证据证明其他
   测试应删除或属于过度。

## 状态

- Skill 输出质量：97/100。
- 文档治理完成度：32/100。
- 两个 Skill 的静态 check 均识别了关键根因；动态结果无法验证。
- 文档治理：仍开放。

## 建议顺序

1. 先停止 live-preflight 的自动 push/PR 触发，只保留取得明确授权的显式入口；该操作需要目标工程修改授权。
2. 为真实现场、常规 Python、replay、媒体、Windows 和发布验证建立可选择的 Registry/suite 映射。
3. 把 Unknown/Waiting 和生产 IM 未接线登记为活动待办，再统一权威契约、实现、schema、fixture 与测试。
4. 对完成报告、旧计划、交接提示、架构基线和发布材料逐组决定承接后归档、直接归档或保留。
5. 精简 AGENTS.md、根 README 和 docs/README.md，最后运行机械门禁。

