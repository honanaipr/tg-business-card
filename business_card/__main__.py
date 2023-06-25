from business_card.dialogs import main_dialog
from business_card.dialogs import translate_dialog
from business_card.states import MainSG
from business_card.ui import configure

import asyncio
from aiogram.filters import CommandObject

from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, setup_dialogs, StartMode
from aiogram_dialog.manager.manager import ManagerImpl
from business_card.utils import get_placeholder_image_url

import logging
from business_card.utils import InterceptHandler
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

from business_card.loader import dp, bot
from business_card.database import users, Query

dp.include_router(main_dialog)
dp.include_router(translate_dialog)
setup_dialogs(dp)

has_admins = False # to skip db request if not needed

@dp.message(Command("start"))
async def start_command(message: Message, dialog_manager: DialogManager):
    _user = Query()
    
    user = users.get(_user.id == message.from_user.id)
    if not user:
        if not has_admins or not users.contains(_user.is_admin == True):
            #have no users yet
            has_admins = True
            user = {"is_admin": True, "id": message.from_user.id}
            users.insert(user)
            await message.answer("You are first user of this bot. Make you an admin!!!")
        else:
            user = {"is_admin": False, "id": message.from_user.id}
            users.insert(user)
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
    await message.answer_photo(photo=get_placeholder_image_url(text="Help"), caption="Did that help you?")

from business_card.routers.translate import translation_router
dp.include_router(translation_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())