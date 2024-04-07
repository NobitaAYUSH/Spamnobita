import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph/file/0d57c17b3ccfd304a935d.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ NOBITA_X_SPAM_BOT✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴋɪɴɢ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/NOBITA_DEVLOPE_THINGS"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MONSTER_X_SUDO")], 
              [Button.url("• ʀᴇᴘᴏ •", "https://github.com/WCGKING/KINGSPAM")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**!𝐁𝐎𝐒𝐃𝐈𝐊𝐄 𝐉𝐀 𝐏𝐀𝐄 𝐍𝐎𝐁𝐈𝐓𝐀 𝐊𝐀 𝐋𝐄 𝐕𝐎 𝐅𝐈𝐑 𝐒𝐔𝐃𝐎 𝐃𝐄 𝐃𝐄 𝐆𝐀 🥀**") 
