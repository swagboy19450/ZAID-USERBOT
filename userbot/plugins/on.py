# Thanks to @Shivam_Patel Bro
# Thanks to Sipak .. 
# Idea by @Shivam_Patel 
# Made by @Shivam_Patel & @ProgrammingError ....TEAM DC
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
        dc_text=(f"** ππ°πΈπ³ πΈπ πΎπ½π»πΈπ½π΄**\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\nβ About My System β\n\nβΎ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄** β {version.__version__}\nβΎ **κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ** β [α΄α΄ΙͺΙ΄](https://t.me/Dark_cobra_support)\nβΎ **ΚΙͺα΄α΄Ι΄κ±α΄**  β [ππππ’ πΏπΎ](https://github.com/DARK-COBRA)\nβΎ **α΄α΄α΄ΚΚΙͺΙ’Κα΄ ΚΚ** β [πΏππ§π -πΎπ€ππ§π](https://github.com/DARK-COBRA/DARKCOBRA)\n\nβΎ **α΄α΄α΄Ιͺα΄α΄** β {uptime}\n\nβΎ **α΄Κ α΄α΄sα΄α΄Κ** β [{DEFAULTUSER}](tg://user?id={ok})\n")
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Κα΄α΄α΄", "https://github.com/Itsunknown-12/ZAID-USERBOT"),
                    Button.url("α΄α΄α΄Κα΄Κ", "https://heroku.com/deploy?template=https://github.com/Itsunknown-12/ZAID-USERBOT")],
                    [Button.url("κ±α΄α΄α΄α΄Κα΄", "https://t.me/Zaid_Support"),
                    Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/Zaid_Updates"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DARK Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Dark Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
