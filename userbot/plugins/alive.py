# Creadits hell bot.. 

import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "π©πππ π€π’ππ‘πππ£"


global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6e512e693a31e5438fc93.mp4"
file2 = "https://telegra.ph/file/52afb59b51cb0e1eb9890.jpg"
file3 = "https://telegra.ph/file/715372bea81d37c2cc90b.jpg"
file4 = "https://telegra.ph/file/9e64778a6664e1793c91a.mp4"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** ββΆβΎβΉ β·ββΆβΈβ βΎβ βΆββΎββΊ**\n\n"
    pm_caption += "**Κα΄Κα΄ α΄ Κα΄, α΄α΄ α΄‘α΄Κα΄ΙͺΙ΄Ι’ κ°ΙͺΙ΄α΄...**\n\n"
    pm_caption += "β α΄Κα΄α΄α΄ α΄Κ κ±Κκ±α΄α΄α΄ β\n\n"
    pm_caption += f"βΎ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄** β {version.__version__}\n"
    pm_caption += "βΎ **κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ** β [κ±α΄α΄α΄α΄Κα΄](https://t.me/Zaid_Support)\n"
    pm_caption += "βΎ **α΄Κα΄Ι΄Ι΄α΄Κ** β [α΄’α΄Ιͺα΄](https://t.me/Zaid_Updates)\n"
    pm_caption += "βΎ **ΚΙͺα΄α΄Ι΄κ±α΄**  β [α΄’α΄Ιͺα΄ ΚΙͺα΄α΄Ι΄κ±α΄](https://github.com/Itsunknown-12/ZAIDUSERBOT)\n"
    pm_caption += "βΎ **α΄α΄α΄ΚΚΙͺΙ’Κα΄ ΚΚ** β [α΄’α΄Ιͺα΄ α΄κ±α΄ΚΚα΄α΄](https://github.com/Itsunknown-12/ZAIDUSERBOT)\n\n"
    pm_caption += f"βΎ **α΄α΄α΄Ιͺα΄α΄** β {uptime}\n\n"
    pm_caption += f"βΎ **πΌπ πΌπ°πππ΄π** β [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

