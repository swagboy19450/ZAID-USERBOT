#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam
marculs=9
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                            MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                              EditBannedRequest,
                                                EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                                 ChatAdminRights,
                                   ChatBannedRights,
                                     MessageEntityMentionName,
                                       MessageMediaPhoto)
#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam
from userbot.utils import register, errors_handler
from userbot.utils import admin_cmd
from userbot import bot as borg
async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Itz not possible without an user ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Error... Please report at @Dark_cobra_support_group", str(err))           
    return user_obj, extra

#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam
global hawk,moth
hawk="admin"
moth="owner"
async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
@borg.on(admin_cmd(pattern="gpromote ?(.*)"))
async def gben(userbot):
    dc = dark = userbot
    i = 0
    sender = await dc.get_sender()
    me = await userbot.client.get_me()
    await dark.edit("`ᴘʀᴏᴍᴏᴛɪɴɢ..ᴇɴᴊᴏʏ ᴋᴀʀ.`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
       k = await dark.edit("ʜᴀʜᴀ ʙꜱᴅᴋ ᴋʜᴜᴅ ꜱᴇ ʜᴏɴᴀ ʀʜᴛᴀ ᴛᴏʜ 😑😑 waao..")
       return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await dark.edit(f"**ꜱᴏᴍᴛʜɪɴɢ ᴡᴇᴍᴛ ᴡʀᴏɴɢ 🤔**")
    if user:
        telchanel = [d.entity.id
                     for d in await userbot.client.get_dialogs()
                     if (d.is_group or d.is_channel)
                     ]
        rgt = ChatAdminRights(add_admins=False,
                               invite_users=True,
                                change_info=False,
                                 ban_users=True,
                                  delete_messages=True,
                                   pin_messages=True)
        for x in telchanel:
          try:
             await userbot.client(EditAdminRequest(x, user, rgt, rank))
             i += 1
             await dark.edit(f"**ꜱᴏɴ ᴘʀᴏᴍᴏᴛᴇᴅ ɪɴ ᴄʜᴀᴛꜱ **: `{i}`")
          except:
             pass
    else:
        await dark.edit(f"**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀꜱ !!**")
    return await dark.edit(
        f"**ꜱᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴘʀᴏᴍᴏᴛᴇᴅ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ [{user.first_name}](tg://user?id={user.id})\n ᴏɴ ᴄʜᴀᴛꜱ😹 : {i} **"
    )
@borg.on(admin_cmd(pattern="gdemote ?(.*)"))
async def gben(userbot):
    dc = dark = userbot
    i = 0
    sender = await dc.get_sender()
    me = await userbot.client.get_me()
    await dark.edit("`demoting...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
       k = await dark.edit("ʟᴏʟ ᴋʜᴜᴅ ᴋᴏ 😑😑 waao..")
       return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await dark.edit(f"**ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇᴍᴛ ᴡʀᴏɴɢ 🤔**")
    if user:
        telchanel = [d.entity.id
                     for d in await userbot.client.get_dialogs()
                     if (d.is_group or d.is_channel)
                     ]
        rgt = ChatAdminRights(add_admins=None,
                               invite_users=None,
                                change_info=None,
                                 ban_users=None,
                                  delete_messages=None,
                                   pin_messages=None)
        for x in telchanel:
          try:
             await userbot.client(EditAdminRequest(x, user, rgt, rank))
             i += 1
             await dark.edit(f"**ʙᴀʜᴜᴛ ᴜʀʀ ʟɪᴀ ʙᴇᴛᴀ ᴀʙ ᴊᴀᴍᴇᴇɴ ᴘᴇ ᴀᴀ ᴏɴ ᴄʜᴀᴛꜱ **: `{i}`")
          except:
             pass
    else:
        await dark.edit(f"**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!**")
    return await dark.edit(
        f"**ᴊᴀᴍᴇᴇɴ ᴘᴇ ʟᴀɴᴅᴇᴅ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ [{user.first_name}](tg://user?id={user.id})\n ᴏɴ ᴄʜᴀᴛꜱ🔥 : {i} **"
    )
#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam#made by @danish_00 with sh1vam
