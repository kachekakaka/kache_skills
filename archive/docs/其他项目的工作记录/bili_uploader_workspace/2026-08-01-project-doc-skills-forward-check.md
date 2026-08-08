# bili_uploader_workspace 项目文档 Skill 前向试用

## 范围与边界

- 模式：project-doc-consistency check、project-doc-skeleton check。
- 两个模式使用独立新任务。
- 全程只读；未运行命令、未修改目标工程、未执行 Git 或联网。

## 主要发现

1. 核心需求、设计、字段和测试 Registry 已有实质正文；当前主要问题不是空骨架，而是生命周期、重复真源和
   测试执行契约没有收口。
2. D1—D6、旧实施方案和 reports 已被描述为完成或历史，仍由活动索引、根 README 和 AGENTS 直接导航；
   archive/docs/README.md 仍为空。
3. HANDOFF_DOCKER_MVP.md、NEW_CHAT_PROMPT.md 和 P0_STATUS.md 属临时交接/状态材料，与核心文档和待办重复
   承接当前阶段。
4. DOCKER_FIRST_AMENDMENT.md 要求首版覆盖 fake 失败、安全重试和 Compose 升级后数据不覆盖；当前 Registry、
   Docker suite 与 D6 E2E 没有完整覆盖这些容器级场景，因此“D6 已完成”表述超出已登记证据。
5. SoftwareTesting/SAFETY.md 要求仓库外、有所有权和 containment 的 run；docker-e2e.sh 默认写入仓库内
   runtime-e2e，不检查所有权标记或路径逃逸，并自动删除 build case。
6. vendor/upstream/biliup.lock.json 仍把补丁 CI 和 D2—D6 完成列为审批 blocker，与活动状态文档冲突。
7. T-DOC 是 full 且被 AGENTS 列为必跑，但四个 workflow 均未调用其规范命令；Docker、D6 和 patched-biliup
   的路径过滤也存在漏触发或 PR/push 不对称。
8. T-DOCKER 与 T-D6-E2E 分别证明镜像/安全边界和完整队列行为，属于有意重叠，不应合并为重复测试。
9. 评估者复核还确认：adapter result 没有与 attempt 保存的 adapter/upstream 身份比较；磁盘阈值默认值为
   零，与“磁盘不足不得开始 attempt”的长期契约存在直接差距。

## 状态

- Skill 输出质量：96/100。
- 文档治理完成度：52/100。
- 两个 Skill 的静态 check 均形成了明确交接；动态结果无法验证。
- 文档治理：仍开放。

## 建议顺序

1. 先开实现任务修复 adapter 身份校验、非零磁盘门槛、E2E 安全根和缺失容器场景，并补对应负向测试。
2. 决定 stale blocker、D6 完成表述和 DOCKER_FIRST_AMENDMENT.md 的当前权威关系。
3. 确定 D1—D6、reports 和交接三件套的当前承接真源及退出条件。
4. 再由 skeleton apply 精简 AGENTS/README 导航、迁移历史材料、登记归档并更新机械资产。
5. 取得命令授权后运行规则夹具、T-DOC 和受影响 suite。

