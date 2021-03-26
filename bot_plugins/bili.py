import asyncio
import random
import time

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment  # aiocqhttp 是 nonebot 的自带依赖
import requests
import json

__plugin_name__ = 'bili'
__plugin_usage__ = '用法： 对我说 "bili"，我会回复随机一条热门视频'


@on_command('bili', aliases=('哔哩','哔哩热门'))
async def _(session: CommandSession):
    index = str(random.randint(1, 50))
    res = requests.get("https://api.bilibili.com/x/web-interface/popular?ps=1&pn=" + index)
    json_res = json.loads(res.text)
    title=json_res["data"]["list"][0]["title"]
    pic=json_res["data"]["list"][0]["pic"]
    up=json_res["data"]["list"][0]["owner"]["name"]
    link=json_res["data"]["list"][0]["short_link"]
    bv=json_res["data"]["list"][0]["bvid"]
    localtime = time.asctime(time.localtime(time.time()))
    await session.send('北京时间:' + localtime + "\n哔哩哔哩随机热门第"+index+"："
                       + "\n视频标题：" + title
                       + "\nUP主：" + up
                       + "\nBV号：" + bv
                       + "\n视频链接：" + link
                       + "\n视频封面：" + MessageSegment.image(pic))