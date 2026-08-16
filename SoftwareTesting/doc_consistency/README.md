# 文档机械门禁

- Registry ID：`T-DOC`
- 执行类别：`full`
- 触发条件：本仓库或采用标准骨架的目标项目，其文档骨架、入口、链接、生命周期、Registry、归档结构或本仓库
  项目文档 Skill 职责发生变化；全量测试时始终执行。
- 输入：当前标准骨架工作区的活动 Markdown、归档索引和固定路径；精确排除任意层级标准项目级 Skill 根中的
  工具资产，不排除相邻工具目录内容或其他位置的 `SKILL.md`。本仓库额外读取三个 Skill 及共享参考。
- fixture：骨架门禁资产使用脚本内置隔离夹具；职责隔离检查同时包含仓库真实合同和内置正反例。
- 工作目录：仓库根目录。
- 环境条件：环境预置 `python`，仅使用 Python 标准库。

## 规范命令

安装或更新门禁资产时先运行规则夹具：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency_rules.py
```

随后运行本仓库的 Skill 职责隔离与交互检查：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_responsibilities.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_contraction_confirmation.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_consistency_counterevidence.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_independent_review.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_installer.py
```

最后运行当前项目的 T-DOC：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency.py
```

采用标准骨架但不包含本仓库三个 Skill 的目标项目只需要前后两个标准命令；中间命令是本仓库特有机械合同。

## 断言

标准门禁机械检查固定路径与大小写、UTF-8 与 LF、相对链接和标题锚点、必要入口、两跳可达性、待办／方案生命周期、
四列测试 Registry 及归档登记。标准根、归档和已排除路径之外，含活动 Markdown 的顶层目录必须由根 README、
项目文档入口或测试总入口直接链接目录内的 Markdown 所有者入口。

本仓库职责隔离检查额外确认：

- 三个 Skill 只能显式调用；
- consistency 与 contraction 都引用同一共享长审计协议，协议本身不拥有事实或内容处置；
- consistency 只形成事实、契约、状态、所有权、Registry／入口和消费者修正，不生成删除或简化动作；
- contraction 必须取得已验证一致性基线，遇到事实冲突使用 `consistency_blocked`，不得自行裁决；
- contraction 裸调用只读识别当前 `HEAD`，默认 `full + 只读报告`，只问一次是否确认已完成一致性整改并做过验证，
  不索要验证证据或五字段模板；
- contraction 不以篇幅直接判定膨胀，必须检查细节必要性，并覆盖需求夹带设计、术语表越界／术语失真和测试类文档
  失效残留，同时保持术语事实与测试义务的 `consistency_blocked` 边界；
- skeleton 保持自己原有的单一交付路线问题，不继承 contraction 的一致性前置；
- 收缩方案与一致性方案不能混合；
- consistency 的 `full` 必须完成四类跨载体反证扫描，第一轮不能用集合对账或初审正向证据自证；
- 内部完整性门只产生 `audit_complete`；独立方案审阅才可产生 `implementation_ready`，并必须检查双向候选闭环、
  过时事实阻断和 `Cnnn` 失效证据复用；
- 安装器必须精确镜像并生成可验证 `SOURCE-PROVENANCE.json`，文件漂移要报告 `mismatch`；
- 两个内容 Skill 不自动调用彼此。

职责脚本包含一致性方案混入收缩动作、README 分层名义下删除重复内容、收缩 Skill 自行裁决事实冲突和同一方案混合
两类动作等反例；交互脚本拒绝旧五字段前置提示；反证脚本拒绝按组 `N/N 不变`、复用正向证据和缺失防误改轴；安装器
脚本验证精确镜像、来源清单和文件漂移。反例必须被拒绝，正例必须通过；独立审阅脚本还拒绝原任务自批、未闭合候选、过时事实直接删除和失效证据复用。

任意层级的 `.agents/skills/**`、`.cursor/skills/**`、`.claude/skills/**`、`.codex/skills/**`、
`.opencode/skills/**`、`.opencode/skill/**` 和 `.github/skills/**` 不接受通用 Markdown 检查；相邻工具目录内容和
其他位置的 `SKILL.md` 仍按原规则检查。`待确认` 待办可以没有方案或链接一份方案，`实施中` 待办必须链接一份方案，
其他活动状态不得保留方案；任一待办最多一份。根 README 与 `docs/README.md` 直接链接至少三份相同专题 Markdown
时给出重复导航 warning。

T-DOC 不判断目标项目正文事实或收缩质量；职责隔离脚本只检查本仓库 Skill 合同，不替代真实项目审计。

## 结果语义

- `passed`：当前要求执行的命令均以退出码 0 完成。
- `failed`：命令已进入可判定阶段，并报告机械不一致或夹具断言失败。
- `blocked`：`python` 或必要只读文件不可用，命令未进入可判定阶段。
- `inconclusive`：命令被中断或运行器内部异常，输出不足以判断。
- `not_run`：命令没有执行；静态检查或其他替代证据不能把本项改写为 `passed`。

结果只绑定命令执行时的工作区。待办退出、方案归档、索引更新或空条件目录清理会形成新候选；生命周期关闭后必须
对最终状态重新运行本门禁，施工中途结果不能替代最终状态结论。

## 清理

七个验证命令都只读。规则夹具和职责隔离反例只使用并自动清理系统临时目录，不创建项目测试根或产品进程，也不接触
真实数据。
