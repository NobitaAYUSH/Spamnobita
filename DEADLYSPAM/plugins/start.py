import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_IMG = ALIVE_IMG
else:
    DEADLY_IMG = "https://telegra.ph/file/0d57c17b3ccfd304a935d.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "NOBITA"

OWNER_ID = config.OWNER_ID

Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/NOBITA_DEVLOPE_THINGS"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/MONSTER_X_SUDO")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://t.me/B_R_A_N_D_E_D_K_I_N_G")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{NAME}](tg://user?id={user_id})"
        myOwner = f"[{NOBITA}](tg://user?id={6316619883})"
        creator = f"[『NOBITA』| ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ NOBI𓄂⃝🔱 𝗕 ❤️ 𝗪](tg://user?id={6316619883})"
        DEADLY_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs NOBITA ʙʀᴀɴᴅᴇᴅ sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {nobi}!

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {NOBITA}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {kairv}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
