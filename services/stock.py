from .common import fetch_stock

async def get_stock_message(stock: str) -> str:
    return (await fetch_stock(stock)).strip()