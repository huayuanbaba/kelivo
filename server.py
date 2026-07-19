"""
Kelivo 微信通知 MCP 服务器
通过 Server酱 把消息推送到你的微信
"""
from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("wechat-sender")

# 从环境变量读取 SendKey（在 Render 里配置，更安全）
SENDKEY = os.environ.get("SERVERCHAN_SENDKEY", "SCT381683TZZJHhPDcuXc4X1iERsCt5Toq")


@mcp.tool()
def send_wechat(title: str, content: str = "") -> str:
    """
    给微信发消息。

    参数:
        title: 消息标题（必填，不超过32字）
        content: 消息正文（可选，支持 Markdown）
    """
    try:
        r = requests.post(
            f"https://sctapi.ftqq.com/{SENDKEY}.send",
            data={"title": title, "desp": content},
            timeout=10,
        )
        result = r.json()
        if result.get("code") == 0:
            return f"\u2705 发送成功：{title}"
        return f"\u274c 发送失败：{result}"
    except Exception as e:
        return f"\u274c 发送异常：{str(e)}"


@mcp.tool()
def send_wechat_simple(message: str) -> str:
    """
    快速给微信发一条消息（只有标题，无正文）。

    参数:
        message: 要发送的消息内容
    """
    return send_wechat(title=message, content="")


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
