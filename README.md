# Kelivo 微信通知 MCP 服务器

通过 Server酱 把消息推送到微信。部署在 Render 上，供 Kelivo 通过 MCP 协议调用。

## 工具说明

| 工具名 | 功能 | 参数 |
|--------|------|------|
| `send_wechat` | 发送带标题和正文的消息 | `title`(标题), `content`(正文,可选) |
| `send_wechat_simple` | 快速发一条纯文本消息 | `message`(消息内容) |

## 部署步骤（Render）

1. 打开 https://render.com ，用 GitHub 账号登录
2. 点 **New +** → **Web Service**
3. 连接你的 GitHub 仓库 `huayuanbaba/kelivo`
4. 配置：
   - **Name**: `kelivo-wechat-mcp`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: Free
5. 点 **Create Web Service**
6. 等待部署完成，拿到公网地址（形如 `https://kelivo-wechat-mcp.onrender.com`）

## Kelivo 配置

在 Kelivo 的 MCP 管理页面添加：

| 配置项 | 值 |
|--------|-----|
| 传输类型 | Streamable HTTP |
| 服务器地址 | `https://kelivo-wechat-mcp.onrender.com/mcp` |
| 启用 | 打开 |
