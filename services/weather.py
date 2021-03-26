from .common import fetch_text


async def get_current_weather_short(city: str) -> str:
    return (await fetch_text(f'https://wttr.in/{city}?format=1')).strip()

async def get_current_weather_desc(city: str) -> str:
    _format = (
        '%l:\n'
        '+%c+%C:+%t\n'
        '+💦+Humidity:+%h\n'
        '+💧+Precipitation:+%p\n'
        '+🍃+Wind:+%w'
    )
    return await fetch_text(f'https://wttr.in/{city}?format={_format}')