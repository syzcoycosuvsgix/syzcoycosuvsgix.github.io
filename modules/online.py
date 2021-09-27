# by @msizen

from .. import loader, utils

from asyncio import sleep

@loader.tds
class EternalOnlineMod(loader.Module):
    """Модуль - вечного онлайна."""
    strings = {"name": "EternalOnline"}

    async def client_ready(self, client, db):
        self.db = db

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
