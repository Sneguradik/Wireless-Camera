from aiogram import executor
from create import dp
from handlers import client, admin
from database import sqlite_db
import asyncio
import datetime

delay = 20

async def on_startup(_):
    print('Bot online')
    sqlite_db.on_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    
    executor.start_polling( dp, skip_updates=True, on_startup=on_startup, loop=loop )
