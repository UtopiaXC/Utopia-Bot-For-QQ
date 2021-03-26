import random
from dataclasses import dataclass
from typing import Dict

import nonebot
import nonebot.permission as perm
from nonebot import on_natural_language, NLPSession, IntentCommand


@on_natural_language(only_to_me=False, permission=perm.GROUP)
async def _(session: NLPSession):
    group_id = session.event.group_id
    user_id = session.event.user_id
