from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import requests
import json

types = {
    "a": "动画",
    "b": "漫画",
    "c": "游戏",
    "d": "文学",
    "e": "原创",
    "f": "来自网络",
    "g": "其他",
    "h": "影视",
    "i": "诗词",
    "j": "网易云",
    "k": "哲学",
    "l": "抖机灵"
}

__plugin_name__ = 'sentence'
__plugin_usage__ = '用法： 对我说 "sentence"，我会回复随机一句话'


@on_command('sentence', aliases='一言')
async def _(session: CommandSession):
    res = requests.get("https://v1.hitokoto.cn/")
    json_res = json.loads(res.text)

    try:
        type = types[json_res['type']]
        sentence = json_res['hitokoto']
        author = json_res['from_who']
        if type == "null" or type is None:
            type = "无类型"
        if author == "null" or author is None:
            author = "匿名"
        await session.send("类型：" + type + "\n" + sentence + "\n作者：" + author)
    except Exception as e:
        await session.send("服务器错误，异常栈：%s" % e)
        await session.send("爬虫返回：" + str(json_res))
