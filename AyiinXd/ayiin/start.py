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
                "https://graph.org/file/24e4273e28a6f5cfedf42-c0b42871f0b339ad18.jpg",
                caption="𝗕𝗹𝘂𝗶𝘀𝘁-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/bluist")),
                         (Button.url("2nd", "https://t.me/Fanderrior"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
