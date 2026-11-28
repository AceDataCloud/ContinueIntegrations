# ACE Music

在 Continue IDE 扩展中，把 [block.yaml](block.yaml) 复制到工作区的 `.continue/mcpServers/acemusic-acedatacloud.yaml`。使用 Continue CLI 时，把该文件中的服务器配置加入当前 `config.yaml` 的 `mcpServers`。在私有的 `~/.continue/.env` 中设置 `ACEDATACLOUD_API_TOKEN` 并重载。该文件可独立安装，Continue Hub 收录需要另外发布。

在[应用管理](https://platform.acedata.cloud/console/applications?utm_source=continue&utm_medium=integration&utm_campaign=ecosystem-growth)打开 **General application**。还没有通用应用时选择 **Initialize General Application**，创建含 ACE Music 权限的 Key。可先使用 `acemusic_list_models` 查询模型。[查看价格](https://platform.acedata.cloud/services/acemusic?utm_source=continue&utm_medium=integration&utm_campaign=ecosystem-growth)后，可用 `acemusic_generate_music` 创作，也可生成歌词、上传参考、翻唱或融合。保存原 `task_id`，用 `acemusic_get_task` 查询同一任务，部分成功时返回已交付的候选。[English](README.md)
