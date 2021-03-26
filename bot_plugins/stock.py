from nonebot.command import CommandSession
from services.common import ServiceException
from services.stock import get_stock_message
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment  # aiocqhttp 是 nonebot 的自带依赖

__plugin_name__ = 'stock'
__plugin_usage__ = (
    '获取股票信息'
)


@on_command('stock', aliases=('股市', '股票', '证券'))
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ', 1)

    if not args[0]:
        stock = await session.aget(key='city', prompt='请输入股票或指数代码（仅支持沪深市场，上交所代码前请加SH，深交所代码前请加SZ）', at_sender=True)
    else:
        stock = args[0]

    try:
        func = get_stock_message
        result = await func(stock)
    except ServiceException as e:
        result = e.message
    await session.send(result,at_sender=True)
    await session.send(MessageSegment.image("http://image.sinajs.cn/newchart/min/n/"+stock.lower()+".gif"))