from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/40dc97c81ce7e67f4dc5d-d2b60fd5a4e4965547.jpg",
                caption="𝗖𝗹𝗮𝘄𝘀𝘆-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/minnimart")),
                         (Button.url("LPM", "https://t.me/LPM_PLUSHIE"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
