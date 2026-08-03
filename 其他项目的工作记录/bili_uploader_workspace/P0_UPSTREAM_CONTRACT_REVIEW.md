# P0 上游 CLI 契约审查

- 审查日期：2026-07-19
- 参考仓库：`biliup/biliup`
- 参考 revision：`adf6a1c03be9f777a76c8c501038c27f3d90a097`
- 结论：stock CLI 暂不具备本项目生产适配器资格

## 已确认的契约缺口

1. `upload` 命令面向人工使用，外部调用者主要得到进程退出状态，未形成稳定的机器可读 BVID/AID 结果协议。
2. 媒体上传和最终投稿位于同一进程路径，外部包装层无法仅凭退出码可靠判断最终投稿请求是否已经发出。
3. 当前提交接口枚举是 `app`、`web`、`bcut_android`；不存在旧方案中的 `client`。
4. 项目 `line=auto` 必须映射为不传上游 `--line`。
5. stock CLI 不能通过现有 argv 设置每个分 P 的自定义标题。
6. 上游断点文件默认由视频路径列表推导并写入平台本地数据目录/临时目录，未绑定任务摘要、账号 MID 和内容哈希。
7. 续期路径可能原地改写 Cookie，且上游日志不应未经脱敏直接持久化。

## P0 选择

当前代码采用“独立、契约化外部 bridge”边界：

```text
核心队列
  └── UploaderAdapter v1
        ├── fake adapter（本阶段已实现）
        └── biliup bridge（待技术验证）
```

真实 bridge 可以使用固定的 biliup 库版本或最小维护分支，但必须对外满足
`docs/ADAPTER_PROTOCOL.md`，不能让核心队列解析上游人类日志。

## 下一步验证

- 固定一个可复现的上游 revision；
- 原型实现 `capabilities`、`account-inspect`、阶段事件、`result.json` 和 `--checkpoint-dir`；
- 使用测试账号验证单视频和多 P；
- 验证 BVID/AID、账号 MID、断点重用拒绝和提交窗口异常；
- 形成带系统、架构、版本和日期的人工报告。
