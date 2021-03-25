import asyncio

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment # aiocqhttp 是 nonebot 的自带依赖
import requests
import json

__plugin_name__ = 'setu'
__plugin_usage__ = '用法： 对我说 "setu"，我会回复随机一张非R18的动漫图片'

apikey="574971726058618c4c45f8"

@on_command('setu', aliases='涩图')
async def _(session: CommandSession):
    res=requests.get("https://api.lolicon.app/setu/?r18=0&apikey="+apikey)
    json_str=json.loads(res.text)
    url=json_str['data'][0]['url']
    author=json_str['data'][0]['author']
    pid=json_str['data'][0]['pid']
    title=json_str['data'][0]['title']
    await session.send("图片信息：\n"
                       "作者："+str(author)
                       +"\n图片PID："+str(pid)
                       +"\n图片标题："+str(title)
                       +"\n注意：图片将在二十秒后撤回")
    message = await session.send(MessageSegment.image(url))
    if message is not None:
        await asyncio.sleep(20)
        await session.bot.delete_msg(message_id=message['message_id'])
    else:
        await session.send("警告：撤回失败")