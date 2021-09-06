'''
Fuck
Fixed for userbot.. By @hellboi_atul.
'''
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from userbot.utils import admin_cmd
from telethon import events
#@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:	
        await event.edit(r"ᴠʀᴏ ᴜ ʀ ᴍʏ ᴏᴡɴᴇʀ ꜱᴏ ɪ ᴄᴀɴᴛ ᴍᴜᴛᴇ ᴜ😁!!")	
        	
        return
    elif event.is_private:
        await event.edit("ᴛʀʏɪɴɢ ᴛᴏ ꜰᴜᴄᴋɪɴɢ ᴛᴀᴘᴇ ᴛʜɪꜱ ᴜꜱᴇʀ ᴍᴏᴜᴛʜ!ᴀʙ ᴄʜᴜᴘ ʙᴀɪᴛʜ!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("ᴀʟʀᴇᴀᴅʏ ꜰᴜᴄᴋᴇᴅ ᴛʜɪꜱ ᴜꜱᴇʀ ᴍᴏᴜᴛʜ😷")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ ꜰᴜᴄᴋᴇᴅ ᴛʜɪꜱ ᴜꜱᴇʀ ᴍᴏᴜᴛʜ😷")

#@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("ᴏᴍᴋ !😐")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("ʟᴏʟ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ɪɴ ᴍᴜᴛᴇ ʟɪꜱᴛ")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ ᴜɴɢᴍᴜᴛᴇᴅ")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
