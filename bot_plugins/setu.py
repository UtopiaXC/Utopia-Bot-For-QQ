import asyncio

from nonebot import scheduler, _bot
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment  # aiocqhttp 是 nonebot 的自带依赖
from source.config import config
import requests
import json

__plugin_name__ = 'setu'
__plugin_usage__ = '用法： 对我说 "setu"，我会回复随机一张非R18的动漫图片'

apikey = config.setu_apikey


async def task(event,message):
    await asyncio.sleep(20)
    if message is not None:
        await _bot.delete_msg(message_id=message['message_id'])
    else:
        await _bot.send(event,"警告：撤回失败")


@on_command('setu', aliases='涩图')
async def _(session: CommandSession):
    res = requests.get("https://api.lolicon.app/setu/?r18=0&apikey=" + apikey)
    json_str = json.loads(res.text)
    if json_str['code'] == 401:
        await session.send("API接口超过调用限制（每令牌每天限制300）或API令牌被封禁")
        return
    url = json_str['data'][0]['url']
    author = json_str['data'][0]['author']
    pid = json_str['data'][0]['pid']
    title = json_str['data'][0]['title']
    await _bot.send(session.event, "图片信息：\n"
                           "作者：" + str(author)
                    + "\n图片PID：" + str(pid)
                    + "\n图片标题：" + str(title)
                    + "\n注意：图片将在二十秒后撤回")
    message = await _bot.send(session.event, MessageSegment.image(url))
    scheduler.add_job(task, args=[session.event,message])