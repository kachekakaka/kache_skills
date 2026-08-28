# 文档机械门禁

- Registry ID：`T-DOC`
- 执行类别：`affected_only`
- 触发条件：门禁或本仓库职责组件的直接输入相对实施开始时冻结的候选基线发生变化；无法可靠形成变更集合、不能证明
  直接输入未变或已有证据失效时执行对应组件。与这些输入无关的产品源码变化本身不触发 T-DOC。
- 输入：`active` 读取当前标准骨架工作区的活动 Markdown 和固定活动路径，不枚举归档正文；`archive` 只读取精确
  归档根、归档索引和登记关系；`all` 合并两者且为兼容默认值。各组件都精确排除任意层级标准项目级 Skill 根中的
  工具资产，不排除相邻工具目录内容或其他位置的 `SKILL.md`。本仓库额外读取三个 Skill 及共享参考。
- fixture：骨架门禁资产使用脚本内置隔离夹具；职责隔离检查同时包含仓库真实合同和内置正反例。
- 工作目录：仓库根目录。
- 环境条件：环境预置 `python`，仅使用 Python 标准库。

## 规范命令与选择

以下七个命令是独立能力入口，不是每次选择 T-DOC 后都要执行的固定并集。只运行本候选直接触发的组件，未选择命令据实
保持 `not_run`。

门禁说明、实现、规则夹具或机械规则合同变化时运行规则夹具：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency_rules.py
```

普通活动文档变化使用 `active`；归档、恢复归档或归档路径／索引变化使用 `archive`；两类输入同时变化或进行生命周期
最终关闭时使用 `all`。未指定组件时默认为 `all`；只有失败修复或相应直接输入再次变化才重跑：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency.py --component active
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency.py --component archive
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency.py --component all
```

本仓库的五个职责命令分别按其脚本和直接读取合同选择：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_responsibilities.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_contraction_confirmation.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_consistency_counterevidence.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_independent_review.py
python -B -X utf8 SoftwareTesting/doc_consistency/test_project_doc_skill_installer.py
```

- Skeleton 源或三个 Skill 的职责隔离合同变化时，选择 `test_project_doc_skill_responsibilities.py`。
- contraction 的裸调用／单次确认合同或与其直接相连的 Skeleton 分流合同变化时，选择
  `test_project_doc_contraction_confirmation.py`。
- consistency 的跨载体反证合同变化时，选择 `test_project_doc_consistency_counterevidence.py`。
- 独立方案审阅合同或其直接消费者变化时，选择 `test_project_doc_independent_review.py`。
- 安装器、来源清单、镜像源集合或 provenance 合同变化时，选择 `test_project_doc_skill_installer.py`。

采用标准骨架但不包含本仓库三个 Skill 的目标项目只保留规则夹具和目标门禁两个标准能力入口，也按各自直接输入选择。

## 断言

`active` 机械检查固定活动路径与大小写、活动 Markdown 的 UTF-8 与 LF、相对链接和标题锚点、必要入口、两跳可达性、
待办／方案生命周期、四列测试 Registry 和活动导航边界；它可以确认归档索引路径存在，但不解析归档表或枚举归档正文。
`archive` 只检查归档索引格式、登记唯一性、当前承接和精确归档正文集合；`all` 合并两者。标准根、归档和已排除路径
之外，含活动 Markdown 的顶层目录必须由根 README、项目文档入口或测试总入口直接链接目录内的 Markdown 所有者入口。

本仓库职责隔离检查额外确认：

- 三个 Skill 只能显式调用；
- 三个 Skill 及其界面元数据不得恢复已退出的额外过程交付物；方案默认一次有界评审，只有实质修订才追加一轮；
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
两类动作等反例，并拒绝已退出的额外过程交付物；交互脚本拒绝旧五字段与固定评审前置提示；反证脚本拒绝按组
`N/N 不变`、复用正向证据和缺失防误改轴；安装器
脚本验证精确镜像、来源清单和文件漂移。反例必须被拒绝，正例必须通过；独立审阅脚本还拒绝原任务自批、未闭合候选、过时事实直接删除和失效证据复用。

任意层级的 `.agents/skills/**`、`.cursor/skills/**`、`.claude/skills/**`、`.codex/skills/**`、
`.opencode/skills/**`、`.opencode/skill/**` 和 `.github/skills/**` 不接受通用 Markdown 检查；相邻工具目录内容和
其他位置的 `SKILL.md` 仍按原规则检查。`待确认` 待办可以没有方案或链接一份方案；`待实施` 和 `实施中` 待办必须
各链接一份方案；`暂缓` 不得保留方案，任一待办最多一份。根 README 与 `docs/README.md` 直接链接至少三份相同专题 Markdown
时给出重复导航 warning。

T-DOC 不判断目标项目正文事实或收缩质量；职责隔离脚本只检查本仓库 Skill 合同，不替代真实项目审计。

## 结果语义

- `passed`：本候选实际选择的命令均以退出码 0 完成；未受影响命令保持 `not_run`，不机械并入结论。
- `failed`：命令已进入可判定阶段，并报告机械不一致或夹具断言失败。
- `blocked`：`python` 或必要只读文件不可用，命令未进入可判定阶段。
- `inconclusive`：命令被中断或运行器内部异常，输出不足以判断。
- `not_run`：命令没有执行；静态检查或其他替代证据不能把本项改写为 `passed`。

结果只绑定命令执行时的工作区。待办退出、方案归档、索引更新或空条件目录清理会同时改变活动与归档输入；生命周期
关闭后使用 `all` 对最终状态运行一次，施工中途结果不能替代最终状态结论。

## 清理

七个验证命令都只读。规则夹具和职责隔离反例只使用并自动清理系统临时目录，不创建项目测试根或产品进程，也不接触
真实数据。
