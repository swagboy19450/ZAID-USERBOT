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
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "🅩🅐🅘🅓 🅤🅢🅔🅡🅑🅞🅣"


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
    pm_caption = "** ⓏⒶⒾⒹ ⒷⓁⒶⒸⓀ ⒾⓈ ⒶⓁⒾⓋⒺ**\n\n"
    pm_caption += "**ʜᴇʜᴇ ᴠʀᴏ, ᴍᴇ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ...**\n\n"
    pm_caption += "✘ ᴀʙᴏᴜᴛ ᴍʏ ꜱʏꜱᴛᴇᴍ ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ꜱᴜᴘᴘᴏʀᴛ](https://t.me/Zaid_Support)\n"
    pm_caption += "➾ **ᴄʜᴀɴɴᴇʟ** ☞ [ᴢᴀɪᴅ](https://t.me/Zaid_Updates)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ᴢᴀɪᴅ ʟɪᴄᴇɴꜱᴇ](https://github.com/Itsunknown-12/ZAIDUSERBOT)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [ᴢᴀɪᴅ ᴜꜱᴇʀʙᴏᴛ](https://github.com/Itsunknown-12/ZAIDUSERBOT)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **🅼🆈 🅼🅰🆂🆃🅴🆁** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

