from nonebot.default_config import *

from datetime import timedelta
from source.config import config


# 表示“超级用户”，也就是机器人的主人。超级用户拥有最高的权限。在这里填入你的 QQ 号。
SUPERUSERS = config.super_admins
# 表示命令的前缀，例如假如命令叫 `天气`，那么只有用户在输入 `/天气` 时候才会触发命令。
COMMAND_START = config.start_with
NICKNAME = config.nick_name
# 表示一条命令的超时（没有用户输入）时间。
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=config.wait_time)
# 服务器和端口
HOST = config.bot_host
PORT = config.bot_port