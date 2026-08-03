# hg_workspace 项目文档 Skill 前向试用

## 范围与边界

- 模式：project-doc-consistency check、project-doc-skeleton check。
- 两个模式使用独立新任务。
- 全程只读；未运行命令、未修改目标工程、未执行 Git 或联网。
- 动态测试、构建产物和 CI 历史状态均未认证。

## 主要发现

1. 固定主干、文档入口、四个 suite、六个待办和归档关系基本完整。四份历史材料已经退出活动导航并由
   archive/docs/README.md 登记，正向控制没有被强行拆分或归档。
2. docs/adr/0011-android-playback-contract.md 要求 Android 对 expiry 做基本安全校验；BackendApi.kt
   只检查非空，没有校验格式、时区或是否已经过期。现有单元测试还接受已经过期的时间值。
3. T-DOC suite 规定门禁源码变化或首次安装时运行规则夹具，CI 当前只运行目标项目门禁，没有运行规则夹具。
4. 后端 health 单元测试与运行镜像 smoke、服务端与 Android playback 契约测试具有不同边界和故障信号，
   属于有意重叠。
5. CI 没有路径过滤，纯文档变化也会构建后端运行镜像和 Android APK；这是过度候选，是否接受需要成本
   和项目策略证据。
6. 根 README 的测试命令和 CI 范围与 SoftwareTesting 入口存在候选重复；是否精简应由用户决定。

## 状态

- Skill 输出质量：92/100，达到 HG 正向控制门槛。
- 文档治理完成度：88/100。
- project-doc-consistency 范围：静态全量 check 完成，动态结果无法验证。
- project-doc-skeleton 范围：静态分类与方案完成，机械命令未运行。
- 文档治理：仍开放。

## 建议顺序

1. 由实现任务修复 Android expiry 校验，并补 malformed、无时区、已过期和未来时间测试。
2. 明确规则夹具是否进入 CI 的 T-DOC 稳定入口。
3. 决定是否精简根 README 测试细节，以及是否需要为项目术语建立 CONTEXT.md。
4. 取得命令授权后再运行规则夹具和目标 T-DOC。

