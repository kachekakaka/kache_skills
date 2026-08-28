# 文档机械门禁

- Registry ID：`T-DOC`
- 执行类别：`affected_only`
- 触发条件：门禁组件的直接输入相对实施开始时冻结的候选基线发生变化；无法可靠形成变更集合、不能证明直接输入未变或
  已有证据失效时执行。与门禁输入无关的产品源码变化本身不触发 T-DOC。
- 输入：`active` 读取当前标准骨架工作区的活动 Markdown 和固定活动路径，不枚举归档正文；`archive` 只读取精确
  归档根、归档索引和登记关系；`all` 合并两者且为兼容默认值。各组件都精确排除任意层级标准项目级 Skill 根中的
  工具资产，不排除相邻工具目录内容或其他位置的 `SKILL.md`。
- fixture：门禁资产自测试使用脚本内置的隔离正反夹具，不使用项目数据。
- 工作目录：仓库根目录。
- 环境条件：环境预置 `python`，仅使用 Python 标准库。

## 规范命令与选择

两个命令是独立能力入口，不是每次选择 T-DOC 后都要执行的固定并集。门禁说明、实现、规则夹具或机械规则合同变化时
运行规则夹具：

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

## 断言

`active` 机械检查固定活动路径与大小写、活动 Markdown 的 UTF-8 与 LF、普通相对链接和标题锚点、必要入口、两跳可达性、待办与方案生命周期、四列测试 Registry 和活动导航边界；它可以确认归档索引存在，但不解析归档表或枚举归档正文。`archive` 只检查归档索引格式、登记唯一性、当前承接和精确归档正文集合；`all` 合并两者。标准根、归档和已排除路径之外，含活动 Markdown 的顶层目录必须由根 README、项目文档入口或测试总入口直接链接目录内的 Markdown 所有者入口。任意层级的 `.agents/skills/**`、`.cursor/skills/**`、`.claude/skills/**`、`.codex/skills/**`、`.opencode/skills/**`、`.opencode/skill/**` 和 `.github/skills/**` 不接受这些通用 Markdown 检查；相邻工具目录内容和其他位置的 `SKILL.md` 仍按原规则检查。`待确认` 待办可以没有方案或链接一份方案；`待实施` 和 `实施中` 待办必须各链接一份方案；`暂缓` 不得保留方案，任一待办最多一份。根 README 与 `docs/README.md` 直接链接至少三份相同专题 Markdown 时给出重复导航 warning。它不解析工具配置或自定义 Skill 根，也不判断正文事实、生命周期语义、测试设计质量、Skill 正文质量或非标准成熟项目是否结构等价。

## 结果语义

- `passed`：本候选实际选择的命令均以退出码 0 完成；未受影响命令保持 `not_run`，不机械并入结论。
- `failed`：命令已进入可判定阶段，并报告机械不一致或夹具断言失败。
- `blocked`：`python` 或必要的只读文件不可用，命令未进入可判定阶段。
- `inconclusive`：命令被中断或运行器内部异常，输出不足以判断一致性。
- `not_run`：命令没有执行；静态检查或其他替代证据不能把本项改写为 `passed`。

结果只绑定命令执行时的工作区。待办退出、方案归档、索引更新或空条件目录清理会同时改变活动与归档输入；生命周期
关闭后使用 `all` 对最终状态运行一次，施工中途结果不能替代最终状态结论。

## 清理

`T-DOC` 只读。规则夹具只使用并自动清理系统临时目录；两个命令都不创建项目测试根或产品进程，也不接触真实数据。
