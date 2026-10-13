# HTML Briefing

<p align="center">
  <a href="README.md"><img src="assets/lang-en.svg" alt="Read in English" width="132" height="40"></a>
  <a href="README.zh-CN.md"><img src="assets/lang-zh.svg" alt="切换到简体中文" width="132" height="40"></a>
</p>

![HTML Briefing：项目证据、清晰叙事与离线汇报](assets/cover.zh-CN.svg)

以叙事编排为核心，组合 Impeccable、UI UX Pro Max、ImageGen、GSAP 与宿主已有的 Visualize，把项目材料做成有证据支撑的 HTML 汇报。适合需要解释工作机制与结果的技术团队、研究者和业务实践者。

**一个入口，保留已有技能，交付可查看、可操作的解释。**

**0.7.0 版本：** 名称统一为 `html-briefing`，新演示默认使用流程画布。随包提供可编辑模板、单文件示例与回归检查。保留此前的多栏、语言和 Sites 指南；玻璃叠页为可选模式。

[安装](#1-安装) · [试用请求](#3-使用) · [下载 0.7.0 ZIP](https://github.com/thejaytang/html-briefing/releases/download/v0.7.0/html-briefing-0.7.0.zip) · [版本说明](https://github.com/thejaytang/html-briefing/releases/tag/v0.7.0) · [能力映射](plugins/html-briefing/skills/html-briefing/references/capabilities.md)

包内提供可移植的根级 `plugin.json`，并保留受支持的 Codex 兼容清单；这不等于已经验证跨宿主运行。正式标识符为 `html-briefing`，旧名为 `html-brifing`。仓库、插件市场和主技能均使用修正后的名称。这是技能编排插件，不是幻灯片编辑器或自动依赖管理器。

## 1. 安装

需要支持插件的 Codex、文件访问能力和已授权的项目工作区。实际渲染验收需要浏览器。插件包含 12 个技能入口：主技能、3 个辅助技能和 GSAP 的 8 个模块。宿主服务和运行库仍需单独具备，只在任务需要时检查。

从 GitHub 安装固定版本：

```sh
codex plugin marketplace add thejaytang/html-briefing --ref v0.7.0
codex plugin add html-briefing@html-briefing
```

也可以下载 [ZIP](https://github.com/thejaytang/html-briefing/releases/download/v0.7.0/html-briefing-0.7.0.zip) 和 [SHA-256 校验文件](https://github.com/thejaytang/html-briefing/releases/download/v0.7.0/html-briefing-0.7.0.zip.sha256)，核对摘要后，在解压出的 `html-briefing-0.7.0` 目录中运行：

```sh
codex plugin marketplace add .
codex plugin add html-briefing@html-briefing
```

本地安装后保留解压目录。开启**新聊天**，使用 `$html-briefing` 提供材料和听众。如只需环境检查，说“使用 $html-briefing，只检查环境”。普通任务无需先运行完整环境清单。

从旧名迁移时，先安装并验证新插件，再移除旧注册；备份本地定制，并退役可能遮蔽新入口的旧个人兼容指针。详见[维护说明](docs/maintenance.md)。历史 v0.5.0 保留原插件标识，不包含流程画布。

## 2. 插件实际包含什么

**插件内置 12 个真实技能入口**，所需参考资料、脚本与许可一同打包。已有个人技能保留：明确指定已有版本时优先使用，否则主流程使用包内版本。

| 内置工作流 | 入口数 | 来源与职责 |
|---|---:|---|
| HTML Briefing | 1 | Jay Tang：叙事、证据、场景连续性、组合统筹与交付验收 |
| Impeccable | 1 | [pbakaus](https://github.com/pbakaus/impeccable)：主视觉系统与视觉审查 |
| UI UX Pro Max | 1 | [nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)：可搜索的配色、字体、图表与交互参考 |
| Playwright | 1 | [OpenAI](https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md)：浏览器验收规则与命令包装脚本 |
| GSAP Skills | 8 | [GreenSock](https://github.com/greensock/gsap-skills)：core、timeline、scrolltrigger、performance、plugins、utils、react、frameworks，按需选择 |

[全部 12 个入口](plugins/html-briefing/skills/html-briefing/references/bundled-skills.md) · [许可、来源和打包修改记录](plugins/html-briefing/THIRD_PARTY_NOTICES.md)

**叙事编排由主技能负责。** 它确定听众需要理解什么，将主张与证据关联，按目的选择叙事结构，并安排每个场景为什么接在前一个之后。决策汇报、机制讲解、进展说明与平行项目不能强套同一模板。原有[业务经验沉淀](plugins/html-briefing/skills/html-briefing/references/experience.md)完整保留。

ImageGen 使用 Codex 系统 `$imagegen` 技能，包内不再重复分发。宿主未提供时应说明能力缺口。

Impeccable 确定视觉方向；UI UX Pro Max 在该方向内提供具体参考；ImageGen 支持图像表达；GSAP 支持有解释作用的动效。**Visualize 通过宿主已有安装参与组合**，用于对话中的机制探索与交互预览。其原插件标注专有许可，公开包不复制源码。需要对话预览而宿主缺少它时，建议查看宿主官方插件目录；独立 HTML 交付不因此受阻。

不要求每次调用全部技能：静态图表不需要 GSAP，原生 HTML 不需要 React 模块。普通写作、代码、图表与表格使用 Agent 已有能力和项目工具。Humanizer、Ponytail 与科研发表套件仍不打包。工具与运行库在需要时检查，不静默安装。

## 3. 使用

下列为示例请求，不代表已测量的业务效果：

| 场景与输入 | 请求 | 预期交付及成功条件 |
|---|---|---|
| 有项目说明与测试记录的技术项目 | “使用 $html-briefing，为不熟悉项目的同事制作 10 分钟离线 HTML 汇报。” | 上下文、设计、机制与实测结果完整；最终文件经过离线打开验收 |
| 交互混乱的已有汇报 | “使用 $html-briefing，修复这份 HTML 的嵌套说明，保留叙事和视觉方向。” | 局部修复；受影响对象的选择、切换和折叠没有残留说明 |
| 需要形象解释的概念 | “使用 $html-briefing，用 ImageGen 插画与可编辑标签解释这个机制。” | 检查后的概念图、精确标签和完整素材包；生成工具缺失时说明缺口 |
| 仍处在讨论阶段 | “使用 $html-briefing，审阅材料并只给提纲。” | 基于证据的提纲；不实施、不安装、不发布 |

可直接用浏览器打开[虚构离线示例](examples/offline-routing.html)，查看绑定到对象的展开说明。它不连接真实排程系统。

打开[流程画布示例](examples/flow-canvas.html)，体验缩放、三个视角和长内容阅读；按[画布指南](plugins/html-briefing/skills/html-briefing/references/flow-canvas.md)构建和改编。

## 4. 如何组合

![流程：证据与听众目标进入主技能，按需使用已有技能统一制作，再验收最终文件](assets/workflow.zh-CN.svg)

主技能确定听众、论证和证据，选择当前可用的相关辅助技能，统一它们的输出，并验收最终汇报。图示说明工作流程，不代表自动执行引擎。

| 能力 | 内置技能或宿主能力 | 提供什么 |
|---|---|---|
| 叙事编排 | 主技能的 storytelling 指南 | 听众目标、证据论证与场景连续性 |
| 视觉系统 | Impeccable | 统一层级、布局、字体与状态 |
| 设计参考 | UI UX Pro Max | 具体配色、字体、图表与交互选择 |
| 数据图表与表格 | 原生 HTML/SVG 与项目已有图表工具 | 明确指标、忠实图表与核对后的结果表 |
| 位图视觉表达 | ImageGen | 场景、对象、插画、图片编辑和透明素材 |
| 精确关系表达 | 原生 HTML/SVG 与内置图解规则 | 可编辑标签、架构、字段映射和交互 |
| 有解释作用的动效 | 按需选择的 GSAP 模块 | 对象连续性与联动状态 |
| 对话预览 | 宿主已有的 Visualize | 在正式制作前探索机制与交互 |
| 验收 | 宿主浏览器工具或 Playwright | 实际渲染、操作与交付检查 |

辅助技能缺失时采用已写明的基础路径。必要的浏览器或图像生成工具缺失时保留明确缺口。技能文件本身不提供模型、运行环境、凭据或服务权限；不得静默切换到付费 ImageGen API。

## 5. 沉淀的实践经验

- 先让陌生听众理解业务上下文，再进入实现细节。
- 主视图保留方案核心，次要说明绑定到具体对象。
- 控件改变证据、操作或输出，不能只改变装饰。
- 跨场景保持对象身份，正确清理嵌套展开和选中状态。
- 把测试方法、观察结果与可支持的结论放在一起。
- 验收移动或解压后的最终包；开发服务器运行或 Mac 截图不能证明 Windows 离线验收。

[经验沉淀说明](plugins/html-briefing/skills/html-briefing/references/experience.md)区分通用经验与可覆盖的标题、导航、动效偏好。仓库不包含私有业务数据或项目截图。

新演示默认使用[流程画布](plugins/html-briefing/skills/html-briefing/references/flow-canvas.md)：输入与输出、核心步骤、阻塞问题、分支和总结。主题节点允许长内容。移动、1/4/9 缩放、结构展开与阅读书签互相独立，缩放围绕当前居中节点。概览显示页顶，返回聚焦恢复阅读。内置模板可编辑且无需运行时依赖。保留明确选择和既有设计；[编辑式玻璃叠页](plugins/html-briefing/skills/html-briefing/references/editorial-glass.md)是可选模式。

[多栏与查看控件](plugins/html-briefing/skills/html-briefing/references/workspace-controls.md)要求支持边界拖动、辅助栏收纳与恢复，以及窄预览中的重排。新增语言设计前先询问最多三种语言和默认语言；紧凑分段式语言按钮与全屏、退出全屏统一放在右上角，中文保留英文专业术语。这是由 Agent 执行的实现要求，不是内置 UI 运行库。

画布顶部采用自动收纳的关键节点导航，右侧保留语言和全屏入口；导航只定位，展开与收纳在内容内触发。不设置常驻品牌栏、底部状态栏或缩放工具栏。实体触控板和跨平台体验仍需逐份验证。

**在 ChatGPT 中**创建或修改 HTML 时，[Sites 同步交付](plugins/html-briefing/skills/html-briefing/references/chatgpt-sites.md)通过宿主实际提供的 Sites 工作流，从同一来源同步制作站点。沿用已有站点网址和访问范围，新站点默认私有；“仅本地”或“不要发布”优先。Sites 不可用时说明缺口，不据此声明 ChatGPT 插件安装或运行兼容已经验证。

## 6. 适用范围、兼容性与限制

适用于项目汇报、研究解释、技术演示和讲者控制的 HTML 报告。生产应用使用网站开发流程，可编辑 PPTX 使用原生演示流程，纯文字周报使用普通写作流程。

| 环境 | 范围 |
|---|---|
| macOS 上的 Codex | 本次发布目标；实际安装与包验证证据见验证记录 |
| Windows / Linux | 文件和资源可迁移，但尚未验证原生安装和渲染验收 |
| 其他技能宿主 | 不声明兼容；需适配并验证宿主工具和插件格式 |
| GSAP 等内置辅助能力 | 技能文件已内置；运行环境和服务权限单独检查，本次未逐一运行所有组合 |
| ImageGen | 使用 Codex 系统技能和可用图像工具，不重复打包 |
| 离线输出 | 新建独立本地汇报的制作要求，逐份验收；插件安装本身可能联网 |

Agent 根据规则执行工作流，插件不保证确定性的技能调度或所有输出都正确。技能说明以英文为主，详细交付清单保留中文。两份 README 描述相同能力，不等于已验证双语运行表现。

## 7. 开发、证据与来源

```sh
python3 scripts/check_package.py
python3 -m unittest discover -s tests
node tests/canvas-model.test.cjs
```

包检查器与 Python 测试使用 Python 3.10+ 标准库；画布模型检查另需 Node.js。生成的 HTML 不依赖外部运行库。可选锁定文件仅保留官方技能元数据验证器所需的 PyYAML。结构检查不代表浏览器行为通过。贡献前阅读 [AGENTS.md](AGENTS.md)、[当前状态](PROJECT_STATE.md)与[发布验证记录](project-support/release-verification-0.7.0.json)。问题复现说明应包含场景、状态、窗口尺寸与输入，不包含私人材料。

[来源与可选上游](plugins/html-briefing/skills/html-briefing/references/sources.md)区分借鉴来源、推荐技能和宿主文档。再分发的技能保留上游许可与署名；移出的技能套件也不列为补装建议。

[MIT 许可](LICENSE)，版权所有 2026 Jay Tang，覆盖本仓库原创规则、图形和检查工具。内置技能分别保留 MIT 或 Apache-2.0，详见[第三方许可说明](plugins/html-briefing/THIRD_PARTY_NOTICES.md)；运行库和服务保留各自条款。欢迎通过 [Issues](https://github.com/thejaytang/html-briefing/issues) 反馈。
