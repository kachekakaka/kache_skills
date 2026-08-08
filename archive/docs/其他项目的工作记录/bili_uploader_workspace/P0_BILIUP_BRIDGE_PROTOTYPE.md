# P0 biliup bridge 原型报告

- 报告日期：2026-07-19
- 里程碑：P0-B
- 状态：兼容桥接原型已实现；真实无人值守投稿仍禁止
- 上游仓库：`biliup/biliup`
- 固定提交：`adf6a1c03be9f777a76c8c501038c27f3d90a097`
- 上游 workspace 版本：`1.2.2`

## 1. 本批次目标

本批次不尝试把普通 biliup CLI 包装成“看起来已经生产可用”的上传器，而是先把能够安全验证的边界实现出来：

1. 固定并记录被审查的上游提交；
2. 从 biliup 登录文件的已知结构中离线提取账号 MID；
3. 在上传前复核账号、媒体大小、SHA-256 和 checkpoint 身份；
4. 将项目投稿参数确定性映射为 stock CLI argv；
5. 将 stock CLI 的 HOME、XDG 数据目录和临时目录限制在当前 attempt 的 checkpoint 目录；
6. 在上游进程启动前持久化保守的远端提交边界；
7. 上游进程启动后，在没有结构化 BVID/AID 的情况下始终返回 `UNCERTAIN`；
8. 默认不启动真实上传。

## 2. 为什么仍不能作为生产适配器

固定提交中的 stock CLI 将媒体上传和最终投稿封装在一个面向人工使用的命令中。外部监督程序可以观察进程退出码和文本输出，但不能稳定获得：

- 可作为成功权威证据的结构化 BVID/AID；
- 可持久消费的媒体上传/最终提交阶段协议；
- 显式 checkpoint 目录参数以及完整身份绑定；
- 平台级幂等键。

因此本原型不把退出码 0 解释为成功，也不通过正则解析日志来制造 BVID/AID。只要 stock CLI 进程已经进入可能提交的执行区间，终态就是 `UNCERTAIN`。

## 3. 两种运行模式

### 3.1 `preflight-only`（默认）

执行：

- request Schema 校验；
- Cookie 文件必须是普通文件，且组/其他用户无读写权限；
- 从 `token_info.mid`、顶层 `mid` 或 `DedeUserID` 中提取唯一 MID；
- `expected_account_mid` 比较；
- 每个视频和封面的普通文件、链接数、大小、SHA-256 和读取期间稳定性检查；
- checkpoint v1 身份文件创建或一致性检查。

全部通过后仍不会调用 biliup，而是写入合法终态：

```text
status = permanent_failure
error.class = production_disabled
remote_submission_started = false
```

该模式用于开发机、CI 和部署前预检。

### 3.2 `lab-stock-cli`（显式实验）

只有显式指定该模式才启动 stock CLI。启动前先写：

```text
PREFLIGHT_STARTED
PREFLIGHT_COMPLETED
MEDIA_UPLOAD_STARTED
SUBMIT_REQUEST_STARTED(remote_submission_started=true)
```

由于 stock CLI 内部何时发出最终投稿请求对外不可见，`SUBMIT_REQUEST_STARTED` 必须在进程启动前持久化。这会扩大 `UNCERTAIN` 区间，但可避免把一次可能已经投稿的运行自动重放。

进程结束后的分类：

```text
退出码 0      -> UNCERTAIN / stock_cli_no_structured_remote_result
非零退出码    -> UNCERTAIN / stock_cli_failed_after_start
超时          -> UNCERTAIN / stock_cli_timeout
边界标记后无法启动 -> UNCERTAIN / stock_cli_start_failed_after_submit_boundary
```

实验模式不是生产模式，不能由定时 worker 自动启用。

## 4. 参数映射

项目参数到固定上游 CLI 的映射：

```text
submit=app           -> --submit app
submit=web           -> --submit web
submit=bcut_android  -> --submit b-cut-android
line=auto            -> 完全不传 --line
line=<具体线路>       -> --line <具体线路>
```

同时映射：

```text
--limit
--copyright
--source（仅转载）
--tid
--title
--desc
--tag
--cover
视频绝对路径（按 request 数组顺序）
```

所有调用使用 argv 数组，不使用 shell；自定义分 P 标题仍不在能力范围内。

## 5. 账号 MID 检查边界

当前 `account-inspect` 是离线凭据结构检查，不代表 Cookie 在 Bilibili 服务器端仍有效。它只接受能从以下已知位置得到唯一 MID 的文件：

```text
token_info.mid
顶层 mid
cookie_info.cookies[].name == DedeUserID
顶层 cookies[].name == DedeUserID
```

多个位置出现不同 MID 时拒绝；权限过宽、符号链接、非 JSON 或缺少 MID 时返回无效。

仍需在后续 bridge 中增加在线账号验证，且在线结果不得泄漏 Cookie、token、CSRF 或完整响应。

## 6. checkpoint 控制

每个 attempt 的项目 checkpoint 元数据固定包含：

```text
task_id
attempt_no
manifest_sha256
submission_fingerprint
expected_account_mid
视频/封面路径、大小和 SHA-256
adapter name/version
上游 revision
submit/line/limit
```

已有 checkpoint 与当前 request 任一身份字段不一致时，在启动上游前返回永久失败。

实验模式额外设置：

```text
HOME=<checkpoint>/home
XDG_DATA_HOME=<checkpoint>/xdg-data
TMPDIR=<checkpoint>/tmp
```

这使当前 Linux 上游通过 `dirs::data_local_dir()` 选择的隐藏断点状态进入 attempt 管理范围。该行为仍需在真实固定二进制上验证，不能只依赖单元测试推断。

## 7. 安全与故障处理

- Cookie 文件要求组/其他用户权限为 0；
- 文件打开使用 `O_NOFOLLOW`（平台支持时）；
- 媒体要求 `st_nlink == 1`；
- 哈希前后复核设备号、inode、大小和修改时间；
- 子进程独立进程组运行；
- 超时时先终止进程组，必要时强杀；
- stdout/stderr 只形成有限、脱敏诊断，不作为状态协议；
- 若桥接进程被 SIGKILL、机器断电或结果损坏，核心包装器仍按既有规则将缺失终态结果归为 `UNCERTAIN`。

## 8. 自动测试覆盖

本批次增加测试覆盖：

- 从 token 和 Cookie 两种位置提取 MID；
- 冲突 MID 拒绝；
- Cookie 私有权限要求；
- `line=auto` 不传 `--line`；
- `bcut_android` 映射；
- 转载来源映射；
- preflight-only 不启动上传并写安全终态；
- checkpoint 身份不一致时阻止执行；
- 实验进程退出 0 仍为 `UNCERTAIN`；
- HOME/XDG/TMP 均限制在 checkpoint 目录。

## 9. 尚未解除的 P0 阻断项

1. 选择能返回真实结构化 BVID/AID 的 bridge 实现；
2. 实现在线账号有效性和 MID 检查；
3. 在真实 biliup 1.2.2 固定构建上验证 XDG checkpoint 重定向；
4. 让最终投稿响应先形成原子 `result.json`，再向核心返回；
5. 对断网、SIGTERM、SIGKILL、超时和最终提交窗口进行真实故障注入；
6. 使用专用测试账号完成人工创作中心核对；
7. 记录构建产物 SHA-256、系统架构和完整测试报告。

在这些项目完成前，`vendor/upstream/biliup.lock.json` 保持：

```json
"production_approved": false
```
