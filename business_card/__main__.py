import asyncio
import logging

from aiogram import F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs
from aiogram_dialog.manager.manager import ManagerImpl

from business_card.db import User, init_db
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

has_admins = True


async def init_has_admins():
    global has_admins
    has_admins = await User.filter(is_admin=True).exists()


@dp.message(Command("start"))
async def start_command(message: Message, dialog_manager: DialogManager):
    global has_admins
    if not message.from_user:
        return
    user = await User.get_or_none(id=message.from_user.id)
    if not user:
        if not has_admins or not User.filter(is_admin=True).exists():
            # have no users yet
            has_admins = True
            await User.create(
                id=message.from_user.id, name=message.from_user.full_name, is_admin=True
            )
            await message.answer("You are first user of this bot. Make you an admin!!!")
        else:
            await User.create(
                id=message.from_user.id,
                name=message.from_user.full_name,
                is_admin=False,
            )
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
dp.startup.register(init_db)
dp.startup.register(init_has_admins)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
