import asyncio
import logging

from aiogram import F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs
from aiogram_dialog.manager.manager import ManagerImpl

from business_card.db import Query, users
from business_card.dialogs import admin_dialog, index_dialog, translate_dialog
from business_card.loader import bot, dp
from business_card.routers.admin import admin_router
from business_card.routers.translate import translation_router
from business_card.states import MainSG
from business_card.ui import configure
from business_card.utils import InterceptHandler, get_placeholder_image_url, is_admin

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

dp.include_router(admin_router)
dp.include_router(index_dialog)
dp.include_router(translate_dialog)
dp.include_router(admin_dialog)
setup_dialogs(dp)

_user = Query()
has_admins = users.contains(_user.is_admin == True)  # to skip db request if not needed
del _user


@dp.message(Command("start"))
async def start_command(message: Message, dialog_manager: DialogManager):
    _user = Query()
    global has_admins
    if not message.from_user:
        return
    user = users.get(_user.id == message.from_user.id)
    if not user:
        if not has_admins or not users.contains(_user.is_admin == True):
            # have no users yet
            has_admins = True
            user = {  # type: ignore
                "is_admin": True,
                "id": message.from_user.id,
                "name": message.from_user.full_name,
            }
            users.insert(user)  # type: ignore
            await message.answer("You are first user of this bot. Make you an admin!!!")
        else:
            user = {  # type: ignore
                "is_admin": False,
                "id": message.from_user.id,
                "name": message.from_user.full_name,
            }
            users.insert(user)  # type: ignore
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)


@dp.message(Command("cancel"))
async def cancel_dialog(message: Message, dialog_manager: DialogManager):
    stack = dialog_manager.current_stack()
    if stack and len(stack.intents) > 0:
        await dialog_manager.done()
    else:
        await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)


@dp.message(Command("args"))
async def get_args_handler(message: Message, command: CommandObject):
    args = command.args.split(" ") if command.args else ["No args"]
    await message.answer(" ".join(args))


@dp.message(Command("help"))
async def help_dialog(message: Message, dialog_manager: DialogManager):
    await message.answer_photo(
        photo=get_placeholder_image_url(text="Help"), caption="Did that help you?"
    )


dp.include_router(translation_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
