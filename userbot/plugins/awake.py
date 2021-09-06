
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/9e64778a6664e1793c91a.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**💦🅩🅐🅘🅓 🅑🅞🅣 🅘🅢 🅦🅞🅡🅚🅘🅝🅖👀 \n\n\n**"
   ALIVE_MESSAGE += "`🅼🆈 🆂🆃🅰🆃🆄🆂 \n\n\n`"
   ALIVE_MESSAGE += f"`ᴛᴇʟᴇᴛʜᴏɴ: TELETHON-1.20.0 \n\n`"
   ALIVE_MESSAGE += f"`ᴘʏᴛʜᴏɴ: PYTHON-3.9.5 \n\n`"
   ALIVE_MESSAGE += "`ᴛᴇʀᴀ ꜱᴀᴛʜ ɴʜɪ ᴄʜʜᴏʀᴜɴɢᴀ ᴠʀᴏ ᴛᴇɴꜱɪᴏɴ ᴍᴀᴛ ʟᴇ ʙᴀꜱꜱ ᴅʏɴᴏꜱ ᴅᴇᴋʜ ʟɪᴏ!!☠ \n\n`"
   ALIVE_MESSAGE += f"`ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ` : @zaid_Support \n\n"
   ALIVE_MESSAGE += f"`🅼🆈 🅼🅰🆂🆃🅴🆁🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.zaid$")
@borg.on(admin_cmd(pattern=r"Zaid"))
async def amireallyalive(awake):
    """ For .zaid command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
