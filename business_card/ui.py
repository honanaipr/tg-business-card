from typing import Any

from aiogram import Bot
from aiogram.methods.base import Request, TelegramMethod
from aiogram.types import BotCommand, BotCommandScopeDefault

BOT_DESCRIPTION = "This bot can just fuck you🖕🏿\n" "If you want some fuck press /start"

BOT_COMMANDS = [
    BotCommand(command="start", description="Начало работы"),
    BotCommand(command="help", description="Помощь"),
    BotCommand(command="cancel", description="Сбросить"),
]


class SetMyDescription(TelegramMethod[bool]):
    """
    Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success.

    Source: https://core.telegram.org/bots/api#setchatdescription
    """

    __returning__ = bool

    description: str | None = None
    """New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language."""
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description."""

    def build_request(self, bot: Bot) -> Request:
        data: dict[str, Any] = self.dict()
        return Request(method="setMyDescription", data=data)


async def set_commands(bot: Bot):
    commands = BOT_COMMANDS
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def set_description(bot: Bot):
    await bot(SetMyDescription(description=BOT_DESCRIPTION))


async def configure(bot: Bot):
    await set_commands(bot)
    await set_description(bot)
