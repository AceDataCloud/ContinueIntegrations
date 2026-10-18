# Suno by Ace Data Cloud：Continue 独立服务配置

这是 Ace Data Cloud 提供的 Suno 集成，不是 Suno 官方插件。复用现有 [SunoMCP](https://github.com/AceDataCloud/SunoMCP)，没有复制服务代码。

**2026-10-18 状态：候选，本地文件可加载；未在 Continue Hub 上架。** 当前官方源码已移除 Hub 加载，不能声称搜索 Suno 即可官方安装。

1. 从 [Continue 官方页面](https://marketplace.visualstudio.com/items?itemName=Continue.continue) 安装编辑器扩展。仅下载本目录 `block.yaml`，保存到项目 `.continue/mcpServers/suno-acedatacloud.yaml`；聊天模型另行配置。
2. [注册/登录 Ace → Applications](https://platform.acedata.cloud/console/applications?utm_source=continue&utm_medium=integration&utm_campaign=ecosystem-growth&utm_content=suno_zh_api_key) → **General application**；没有则点 **Initialize General Application**。复制 API Key，或 **Manage Keys → Create** 创建 `Continue Suno` 专用 Token。先核服务权限、有效期、余额及[当前价格](https://platform.acedata.cloud/models?utm_source=continue&utm_medium=integration&utm_campaign=ecosystem-growth&utm_content=suno_zh_pricing)，开启 API 限制时同时允许生成与任务查询接口。
3. 在运行 Continue 的用户 `~/.continue/.env` 中保存 `ACEDATACLOUD_API_TOKEN=你的原始Token`。不要加 Bearer，不用 `platform-...` 管理 Token，不提交真实凭据。YAML 仍用 Secret 占位符。
4. 重载 Continue，在 Agent 模式核 MCP 连接与工具列表。列表出现不证明生成成功；确认费用后才调用 `suno_generate_music`。保留返回的 task_id，反复调用 `suno_get_task` 查询同一个 ID，直到成功或失败；pending 和预览不能当最终结果，不要通过重新生成查进度。
5. 成功后打开最终媒体链接，并对账；此仓未发新的收费请求，没有真实 Continue 媒体完成截图。

![Continue 官方历史配置入口，非 Ace 实测](../../assets/continue-local-config.png)

原图：Continue 官方配置文档，文件最近提交 2025-07-10，产品版本未标注；不是新 Ace 按钮或成功安装证据。

![复制 Key 或打开管理](https://raw.githubusercontent.com/AceDataCloud/SunoDify/8d3d03570e73324220f111f7fe343da0792a8071/_assets/tutorial/get-api-key-en.png)

![创建专用 Key](https://raw.githubusercontent.com/AceDataCloud/SunoDify/8d3d03570e73324220f111f7fe343da0792a8071/_assets/tutorial/create-api-key-en.png)

上两图为 Ace 已发布账户教程的脱敏截图（来自 SunoDify），不是 Continue 内运行截图。

401 查 Token/过期/加载位置，403 查权限或审核；pending 继续查询原 ID。此独立配置只连接当前服务端点；实际 API 访问仍由 Token 权限控制。

完整字段与接口：[English guide](README.md)。
