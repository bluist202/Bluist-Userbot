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
                "https://graph.org/file/d22e91671529c80c7f564-f93371b5e632c19ddd.jpg",
                caption="𝗩𝗼𝗿𝘁𝗮𝘅-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/marknost")),
                         (Button.url("Ress", "https://t.me/resshunter"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
