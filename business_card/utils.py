import logging
from urllib.parse import quote

from aiogram import Dispatcher, Router
from aiogram_dialog import Dialog
from loguru import logger

from business_card.db import Query, users


def get_placeholder_image_url(
    text: str = "None",
    size: tuple[int, int] = (600, 200),
    font: str | None = "playfair-display",
    format: str | None = "jpg",
) -> str:
    return f"https://placehold.co/{size[0]}x{size[1]}.{format}?text={quote(text)}&font={font}"


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def is_admin(id: int) -> bool:
    """
    check is user is admin by it's id
    """
    _user: Query = Query()
    is_admin: bool = users.contains((_user.is_admin == True) & (_user.id == id))
    return is_admin


def add_admin(id: int) -> None:
    """
    add admin by it's id
    """
    _user: Query = Query()
    users.upsert({"is_admin": True, "id": id}, _user.id == id)


def get_admins():  # noqa ANN201
    """
    get all users
    """
    return users.all()
