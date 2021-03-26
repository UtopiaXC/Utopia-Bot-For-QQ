import time

from httpx import AsyncClient, HTTPError

from .log import logger
import requests


class ServiceException(Exception):
    'Base of exceptions thrown by the service side'

    def __init__(self, message: str) -> None:
        super().__init__(message)

    @property
    def message(self) -> str:
        return self.args[0]


async def fetch_text(uri: str) -> str:
    async with AsyncClient(headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}) as client:
        try:
            res = await client.get(uri)
            res.raise_for_status()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('API 服务目前不可用')
        return res.text


async def fetch_stock(stock: str) -> str:
    try:
        headers = {
            'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        }
        url = 'https://xueqiu.com/S/' + stock
        rsp = requests.get(url=url, headers=headers)
        if rsp.text.__contains__("404__bg"):
            return "请查证股票代码后再查询"
        text = ''
        for row in rsp.text.split("\n"):
            if 'quote: {"' in row:
                text = row.strip()
                break
        dic = {}
        list_data = text[8:-2].split(",")
        for i in range(len(list_data)):
            list_item = list_data[i].split(":")
            if list_item[1][-1] == '"':
                item = list_item[1][1:-1]
            else:
                item = list_item[1]
            dic[list_item[0][1:-1]] = item
        time_local = time.localtime(int(dic['time'][:-3]))
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

        return "数据更新：北京时间" + dt + "\n" + dic['name'] + \
               "\n现价：" + str(dic['current']) + \
               "\n跌涨幅：" + str(dic['percentStr']) + \
               "\n昨收：" + str(dic['last_close']) + \
               "\n今开：" + str(dic['open']) + \
               "\n最高：" + str(dic['high']) + \
               "\n最低：" + str(dic['low']) + \
               "\n交易量（手）：" + str(dic['volume'])[:-2] + \
               "\n交易额（万元）：" + format(int(dic['amount']) / 10000, ".2f")
    except:
        raise ServiceException("接口异常")
