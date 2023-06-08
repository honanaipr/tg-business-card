from business_card.diologs import main_diolog
from business_card.diologs import secondary_diolog
from business_card.states import MainSG
from business_card.configuration import configure

import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogRegistry, DialogManager
from aiogram_dialog.manager.manager import ManagerImpl

from business_card.utils import get_placehold_image_url

API_TOKEN = '6244180609:AAGl8bZGQ3fG_otyQONWvu-c6ukKvILJohY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
reg = DialogRegistry(dp)

reg.register(main_diolog)
reg.register(secondary_diolog)
reg.register_start_handler(MainSG.main)

@dp.message(Command("cancel"))
async def cancel_dialog(message: Message, dialog_manager: ManagerImpl):
    if len(dialog_manager.current_stack().intents) > 0:
        await dialog_manager.done()

@dp.message(Command("help"))
async def cancel_dialog(message: Message, dialog_manager: DialogManager):
    await message.answer_photo(photo=get_placehold_image_url(text="Help"), caption="Did that help you?")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())