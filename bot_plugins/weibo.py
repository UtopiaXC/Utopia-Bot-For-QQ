import asyncio
import datetime
import random
import time
from bs4 import BeautifulSoup

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import requests

__plugin_name__ = 'weibo'
__plugin_usage__ = '用法： 对我说 "weibo"，我会回复微博前十条热搜'



@on_command('weibo', aliases=('热搜',"微博"))
async def _(session: CommandSession):
    res = requests.get("https://s.weibo.com/top/summary")
    soup = BeautifulSoup(res.text)
    res = ""
    for i in range(len(soup.find_all("td", class_="td-02"))):
        if i is 0:
            res += ("置顶热搜：" + soup.find_all("td", class_="td-02")[i].a.get_text() + '\n')
        else:
            res += ("热搜第" + str(i) + "：" + soup.find_all("td", class_="td-02")[i].a.get_text() + '\n')
    localtime = time.asctime(time.localtime(time.time()))
    res += ('北京时间:' + localtime)
    await session.send(res)