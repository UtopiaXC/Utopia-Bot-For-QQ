import asyncio
import datetime
import random
import time

from bs4 import BeautifulSoup
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment  # aiocqhttp 是 nonebot 的自带依赖
import requests
import json

__plugin_name__ = 'english'
__plugin_usage__ = '用法： 对我说 "english"，我会回复随机英语'


@on_command('english', aliases='英语')
async def _(session: CommandSession):
    end_time = datetime.datetime.now()
    start_time = datetime.datetime.now() + datetime.timedelta(days=-600)
    a1 = tuple(start_time.timetuple()[0:9])
    a2 = tuple(end_time.timetuple()[0:9])
    start = time.mktime(a1)
    end = time.mktime(a2)
    t = random.randint(int(start), int(end))
    date_touple = time.localtime(t)
    date = time.strftime("%Y-%m-%d", date_touple)
    res = requests.get("http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title=" + date)
    json_str = json.loads(res.text)
    chinese=json_str["note"]
    english=json_str["content"]
    pic = json_str["picture2"]
    voice=json_str["tts"]
    await session.send( "英文原文：" + english
                       + "\n翻译：" + chinese
                       + "\n封面：" + MessageSegment.image(pic))
    await session.send(MessageSegment.record(voice))


file=open("../source/eng_daily.csv")
urls=file.readlines()
index=random.randint(1,len(urls)-1)
res=requests.get(urls[index])
