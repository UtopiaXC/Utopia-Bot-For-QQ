from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import time

__plugin_name__ = 'help'
__plugin_usage__ = '用法： 对我说 "help"，我会回复机器人功能表'


@on_command('help', aliases='帮助')
async def _(session: CommandSession):
    localtime = time.asctime(time.localtime(time.time()))
    await session.send('北京时间:' + localtime + "\n"
                                             '/help 或 /帮助 ：查看全部指令\n'
                                             '/sentence 或 /一言 ：随机获取一条名句\n'
                                             '/setu 或 /涩图 ： 随机获取一张非R18的动漫图片\n'
                                             '/daily 或 /日报 ： 随机获取一条知乎今日日报\n'
                                             '/english 或 /英语 ： 随机获取一句英语（来自金山词霸，词库约600，每日更新一句）\n'
                                             '/weibo 或 /微博 或 /热搜 ： 获取当前微博热搜前十条\n'
                                             '/bili 或 /哔哩 或 /哔哩热门 ： 获取当前随机一条哔哩哔哩热门视频'
                                             '/weather 或 /天气 ：查询实时天气，支持参数化与语义分析，参数化：/weather *城市名 详情。语义分析：根据对话自动查询。')