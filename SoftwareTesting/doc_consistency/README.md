# 文档机械门禁

- Registry ID：`T-DOC`
- 执行类别：`full`
- 触发条件：文档骨架、入口、链接、生命周期、Registry 或归档结构发生变化；全量测试时始终执行。
- 输入：当前工作区的活动 Markdown、归档索引和固定骨架路径。
- fixture：门禁资产自测试使用脚本内置的隔离正反夹具，不使用项目数据。
- 工作目录：仓库根目录。
- 环境条件：环境预置 `python`，仅使用 Python 标准库。

## 规范命令

安装或更新门禁资产时先运行规则夹具：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency_rules.py
```

随后运行当前项目的 `T-DOC`：

```text
python -B -X utf8 SoftwareTesting/doc_consistency/test_doc_consistency.py
```

## 断言

门禁机械检查固定路径与大小写、UTF-8 与 LF、普通相对链接和标题锚点、必要入口、两跳可达性、待办与方案生命周期、测试 Registry 及归档登记。它不判断正文事实是否符合代码或产品行为。

## 结果语义

- `passed`：当前要求执行的命令均以退出码 0 完成。
- `failed`：命令已进入可判定阶段，并报告机械不一致或夹具断言失败。
- `blocked`：`python` 或必要的只读文件不可用，命令未进入可判定阶段。
- `inconclusive`：命令被中断或运行器内部异常，输出不足以判断一致性。
- `not_run`：命令没有执行。

## 清理

`T-DOC` 只读。规则夹具只使用并自动清理系统临时目录；两个命令都不创建项目测试根或产品进程，也不接触真实数据。
