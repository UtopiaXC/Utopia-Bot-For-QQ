import asyncio
import random
import time

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment  # aiocqhttp 是 nonebot 的自带依赖
import requests
import json

__plugin_name__ = 'daily'
__plugin_usage__ = '用法： 对我说 "daily"，我会回复随机一条知乎今日日报'


@on_command('daily', aliases='日报')
async def _(session: CommandSession):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 "
                      "Safari/537.36 "
    }
    res = requests.get("https://news-at.zhihu.com/api/3/stories/latest", headers=header)
    json_str = json.loads(res.text)
    index = random.randint(0, len(json_str["stories"]) - 1)
    title = json_str["stories"][index]["title"]
    image = json_str["stories"][index]["images"][0]
    url = json_str["stories"][index]["url"]
    print(title)
    print(image)
    print(url)
    localtime = time.asctime(time.localtime(time.time()))
    await session.send('北京时间:' + localtime + " 知乎日报"
                       + "\n文章标题：" + title
                       + "\n文章链接：" + url
                       + "\n文章封面：" + MessageSegment.image(image))
