from business_card.diologs import main_diolog
from business_card.diologs import secondary_diolog
from business_card.states import MainSG

import asyncio

from aiogram import Bot, Dispatcher

from aiogram_dialog import DialogRegistry

API_TOKEN = '6244180609:AAGl8bZGQ3fG_otyQONWvu-c6ukKvILJohY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
reg = DialogRegistry(dp)

reg.register(main_diolog)
reg.register(secondary_diolog)
reg.register_start_handler(MainSG.main)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())