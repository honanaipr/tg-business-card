from aiogram import Router
from aiogram.enums import InlineQueryResultType
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.methods import EditMessageText
from aiogram.types import (
    ChosenInlineResult,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from aiogram_dialog import DialogManager, StartMode
from loguru import logger

from business_card import utils
from business_card.dialogs.admin import AdminSG
from business_card.loader import bot

admin_router = Router()


@admin_router.message(Command("get_users"))
async def command_start_handler(message: Message, command: CommandObject):
    if not utils.is_admin(message.from_user.id):
        logger.warning("Someone non admin try to use " + message.text)
        return
    if not command.args:
        answer = "\n".join(
            [
                "Name: " + str(document["name"]) + "\n"
                "Id: " + str(document["id"]) + "\n"
                "Is admin: " + str(document["is_admin"]) + "\n\n"
                for document in utils.get_admins()
            ]
        )
        await message.answer(answer)
    else:
        await message.answer("Not realized for " + command.args)


@admin_router.message(Command("add_admin"))
async def command_add_admin_handler(
    message: Message,
    command: CommandObject,
    dialog_manager: DialogManager,
    state: FSMContext,
):
    if not utils.is_admin(message.from_user.id):
        logger.warning("Someone non admin try to user ", message.text)
        return
    await dialog_manager.start(AdminSG.add_admin)
