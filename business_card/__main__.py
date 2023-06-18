from business_card.diologs import main_diolog
from business_card.diologs import translate_dialog
from business_card.states import MainSG
from business_card.configuration import configure

import asyncio
from aiogram.filters import CommandObject

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, setup_dialogs, StartMode
from aiogram_dialog.manager.manager import ManagerImpl
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from business_card.utils import get_placehold_image_url

import logging
from business_card.utils import InterceptHandler
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

API_TOKEN = '6244180609:AAGl8bZGQ3fG_otyQONWvu-c6ukKvILJohY'

storage = RedisStorage.from_url("redis://localhost:6379/db", key_builder=DefaultKeyBuilder(with_destiny=True))
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)

dp.include_router(main_diolog)
dp.include_router(translate_dialog)
setup_dialogs(dp)

@dp.message(Command("start"))
async def start_comand(message: Message, dialog_manager: ManagerImpl):
     await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)

@dp.message(Command("cancel"))
async def cancel_dialog(message: Message, dialog_manager: ManagerImpl):
    if len(dialog_manager.current_stack().intents) > 0:
        await dialog_manager.done()
    if len(dialog_manager.current_stack().intents) == 0:
        await dialog_manager.start(MainSG.main)

@dp.message(Command("args"))
async def get_args_handler(message: Message, command: CommandObject):
    args = command.args.split(" ") if command.args else ["No args"]
    await message.answer(" ".join(args))

@dp.message(Command("help"))
async def cancel_dialog(message: Message, dialog_manager: DialogManager):
    await message.answer_photo(photo=get_placehold_image_url(text="Help"), caption="Did that help you?")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())