# 项目文档骨架规则

## 目录

1. 适用范围
2. 固定与条件结构
3. 导航
4. 协作规则
5. 文件职责
6. 待办与方案
7. 归档
8. 新建与迁移
9. 内容 Skill 交接

## 1. 适用范围

本骨架只支持单一上下文项目。发现 `CONTEXT-MAP.md`、多个领域 `CONTEXT.md` 或明显独立的业务
上下文时保持只读，报告证据并建议显式调用 `$grill-with-docs`。

不建立项目级骨架版本、隐藏状态、文档 manifest 或依赖图。机械规则按当前文件检查；通用脚本只保存
自身的资产 ID 和接口 schema。

## 2. 固定与条件结构

固定主干：

```text
/
├── AGENTS.md
├── README.md
├── docs/
│   ├── README.md
│   ├── 需求文档.md
│   ├── 设计文档.md
│   ├── 已知问题与待做需求.md
│   └── 软件测试.md
├── SoftwareTesting/
│   ├── README.md
│   ├── PROTOCOL.md
│   └── SAFETY.md
└── archive/
    └── docs/
        └── README.md
```

按需创建：

```text
CONTEXT.md
docs/字段契约.md
docs/adr/
docs/方案/
docs/运维/
SoftwareTesting/<suite>/
SoftwareTesting/manual/
archive/SoftwareTesting/
```

空的条件目录不落盘。条件后来满足时可再次显式调用 Skill 升格。

## 3. 导航

协作第一入口：

```text
AGENTS.md
├── CONTEXT.md（存在时）
├── README.md#构建与交付
├── docs/README.md
└── SoftwareTesting/README.md
```

面向项目使用者：

```text
README.md
├── docs/README.md
└── SoftwareTesting/README.md
```

专题入口：

```text
docs/README.md
├── 核心文档
├── 条件专题
└── archive/docs/README.md

SoftwareTesting/README.md
├── PROTOCOL.md
├── SAFETY.md
├── docs/软件测试.md
└── 每个活动 suite README
```

README 不反向链接 `AGENTS.md`。每份活动文档必须通过实际 Markdown 链接在两跳内到达：

- 核心文档从 `docs/README.md` 直接到达；
- 活动方案从 `docs/README.md → 已知问题与待做需求.md → 方案` 到达；
- ADR 从 `docs/README.md → 当前设计或相关当前真源 → ADR` 到达；
- 多份运维文档可以由 `docs/运维/README.md` 二级索引；
- 单纯链接目录不自动视为登记其全部后代；
- 活动测试 suite README 必须从 `SoftwareTesting/README.md` 直接到达。

机器读取的入口使用普通行内相对链接。正文 Markdown 不受此限制。

## 4. 协作规则

- 与用户交流使用简体中文。
- 新项目没有既有约定时，文档、代码注释和提交说明默认使用简体中文。
- 既有项目已有语言规则时逐条展示差异；互不依赖的选择可以集中确认，存在冲突或依赖时再逐个询问。
  未确认前保留原规则。
- 修改语言规则与翻译既有内容分别授权，不自动整仓翻译。
- 标识符、公开 API 和协议字段按语言生态使用英文。
- 未得到明确修改授权时只读。
- commit、push 和 PR 分别取得授权；修改授权不包含它们。
- 构建入口、触发条件和交付产物必须明确。
- 普通验证、全量测试和正式认证分层，默认普通验证。
- 不得把 Cookie、Token、Key、密码、真实用户数据和原始运行现场写入仓库。这是协作红线，
  不是本骨架的秘密扫描职责。

## 5. 文件职责

### AGENTS.md

只保存跨任务长期红线、修改与 Git 授权、语言规则，以及 CONTEXT、构建、文档和测试触发入口。
不保存专项命令、产品现状、字段、任务进度或重复规则。

### README.md

保存项目目的、当前能力简要边界、主要目录、最短运行入口和唯一“构建与交付”入口。链接
`docs/README.md` 与 `SoftwareTesting/README.md`，不反向链接 `AGENTS.md`。

### CONTEXT.md

只有存在项目专属术语时创建，固定在根目录，由 `$grill-with-docs` 独占维护。骨架 Skill 只检查
位置和入口，不检查或修改内容。

### docs/README.md

作为活动文档总入口，保存职责索引、阅读顺序、事实分流、生命周期、条件模块和归档入口。机器直接解析
实际链接，不使用第二份文档 manifest。

本骨架只定义各路径声明承接的内容类别，不读取正文判断内容是否放错。正文职责越界由
`$project-doc-consistency check` 检查。

### docs/需求文档.md

承接当前已交付、用户可观察且可验收的行为和支持边界。未实现事项进入待办；内容真实性由
`$project-doc-consistency check` 检查。

### docs/设计文档.md

承接当前实现结构、入口、调用链、数据流和适配边界，并链接必要 ADR。目标架构和实施步骤不属于本文；
内容真实性由 `$project-doc-consistency check` 检查。

### docs/已知问题与待做需求.md

只保存未完成事项。所有二级标题都代表待办；文件说明放在一级标题后，条目内部可使用三级及以下标题。

### docs/软件测试.md

只保存稳定 Registry。测试治理见 `testing-baseline.md`。

### docs/字段契约.md

存在数据库、API、跨进程、配置 schema、事件或多层序列化边界时创建，承接字段所有权、名称、类型、
空值、默认值、映射和兼容规则。

### docs/运维/

存在部署、安装、代理、证书、备份、恢复、升级或当前故障处理时创建。开发构建留根 README，测试规则
留 `SoftwareTesting/`，一次性实施步骤留活动方案。

### 其他专题

只有用户确认或 `$project-doc-consistency check` 已提供证据，证明其同时满足长期有效、职责独立、现有真源无法
承接、有足够内容、有实际入口和明确退出条件时新增。

## 6. 待办与方案

待办格式：

```markdown
## FEATURE-001：标题

- 状态：待确认
```

ID 使用大写字母、数字和连字符，至少一个连字符。状态只允许：

- `待确认`
- `待实施`
- `实施中`
- `暂缓`

新 ID 不得复用当前文档、归档和可发现 Git 历史中的既有 ID；没有历史时只保证当前可见范围。

只有 `实施中` 待办可以且必须拥有一份：

```text
docs/方案/<待办ID>-<名称>.md
```

不提供方案正文模板。机械门禁只要求：

1. 文件与唯一待办 ID 对应；
2. 恰好各出现一次“测试层级、验证影响域、具体验证项”；
3. 方案由对应待办实际链接；
4. 完成、取消、暂缓或被替代后退出活动目录。

机械门禁不判断待办状态、测试层级或验证项在项目事实上是否正确。方案是否区分当前与目标、范围是否
完整、长期真源是否收口，由 `$project-doc-consistency check` 检查；存在真实取舍时交给 `$grill-with-docs`。

## 7. 归档

`archive/docs/README.md` 始终存在。归档条目使用：

```markdown
| 归档文档 | 历史职责 | 当前承接真源 |
| --- | --- | --- |
| [旧方案](旧方案.md) | 当时承担的职责 | [当前设计](../../docs/设计文档.md) |
```

每份归档 Markdown 恰好登记一次；历史职责不能为空；当前承接必须链接项目内活动 Markdown，
确实没有时写“无，仅保留历史证据”。

退役测试资产进入条件目录 `archive/SoftwareTesting/`，首次出现时建立相同三列逻辑的 README。
活动导航只链接归档索引，不直接枚举归档正文。

`$project-doc-consistency check` 只提供过期、重复、冲突和当前承接候选的事实证据。归档价值、合并、删除和新承接
职责属于语义决定，交给 `$grill-with-docs`；确认后再由本骨架实施结构变化。

## 8. 新建与迁移

新项目只生成标题、路径职责、必要导航和用户明确确认的“不适用”，不根据代码、配置、构建或测试推导
项目事实，也不生成大段 TODO、目标架构、虚构能力或通用内容模板。没有项目专属术语时不创建
`CONTEXT.md`。

非空既有项目先取得用户确认的文档职责映射。无法确定一对一承接位置时停止，建议显式调用
`$project-doc-consistency check`。一对一迁移保持事实正文原样。

修改前状态能够从 Git 或其他可靠来源精确恢复时不创建外部备份。未跟踪、已有未提交修改、无版本控制
或其他不可恢复文档与本 Skill 托管资产，在移动、合并、覆盖、归档或删除前必须备份或停止询问。
骨架迁移不得删除产品代码、配置、构建脚本或项目测试；文档和托管资产的删除也必须逐路径明确授权。

现有 `AGENTS.md` 在迁移完成前继续有效。规则冲突逐项展示当前规则、建议规则、影响和推荐，不自动覆盖。

## 9. 内容 Skill 交接

- 声明的路径职责、结构、入口、数量和机械生命周期由 `$project-doc-skeleton` 处理。
- 当前事实、过期内容、重复真源、正文职责越界和候选现有承接文档由 `$project-doc-consistency` 处理：`check` 只读检查，`sync` 同步可直接证明的事实正文。
- 术语、`CONTEXT.md`、ADR，以及合并、拆分、归档、删除和新承接职责等语义取舍由
  `$grill-with-docs` 处理。

交接顺序是“一致性检查提供证据 → `$grill-with-docs` 裁决真实取舍 → 骨架实施结构变化”。不需要真实取舍的
明确事实修订可以由 `$project-doc-consistency sync` 在独立授权后完成。三个 Skill 都必须显式调用；一个 Skill 只能建议另一个，
不得自动触发或继承修改授权。
