# bili_workspace 项目文档 Skill 前向试用

## 范围与边界

- 模式：project-doc-consistency check、project-doc-skeleton check。
- 两个模式使用独立新任务。
- 全程只读；未运行命令、未修改目标工程、未执行 Git 或联网。

## 主要发现

1. docs/需求文档.md、docs/设计文档.md 和 docs/字段契约.md 声明自己是长期真源，正文却只有旧文档路由。
   docs/README.md 承认后续收口，但活动待办为空，也没有退出条件。
2. V0.6、V0.6.2 Review、UI Issue、V0.7 验收和 release notes 仍由活动索引直接枚举；其中部分材料指向
   已删除的旧前端资产。
3. 根 README 与 docs/README.md 重复枚举大量专题；若干根级或模块 README 缺少清晰的两跳活动入口。
4. Registry 只有 T-DOC 和 T-PROJECT；T-PROJECT 同时包揽 Python、Ruff、pytest、前端、Windows 和运行
   资产，无法表达 Playwright、Docker、Windows 发布等独立影响域。
5. Windows 与 Linux 的完整自检不设置 BILI_RUN_PLAYWRIGHT=1，Playwright 测试会被跳过；如果 Playwright
   属于 full，则与完整验证声明冲突，否则应有独立稳定入口。
6. 主 CI 与独立 UI workflow 在相同环境执行基本相同的 Playwright 集合，属于冗余候选；focused、release
   与全量 pytest 的部分重叠具有专项定位或发布信号，暂按有意重叠。
7. Docker 发布门禁声明包含持久化、旧库升级和登录/健康链路，现有静态测试与 CI 没有完整容器行为证据。

## 状态

- Skill 输出质量：95/100。
- 文档治理完成度：42/100。
- 两个 Skill 的静态 check 均形成可执行交接；动态结果无法验证。
- 文档治理：仍开放。

## 建议顺序

1. 先用 consistency sync 把当前源码可证明的需求、设计和字段事实写回核心文档，并登记兼容路由收敛待办。
2. 决定旧专题的独立长期职责和归档边界；没有独立职责的材料在承接后归档。
3. 明确 Playwright、Windows、Docker 与发布门禁是 T-PROJECT 子步骤还是独立 suite。
4. 决定 CI 重复执行的保留、差异化或合并方案。
5. 最后由 skeleton apply 精简导航、处理生命周期和安装一致的机械资产。

