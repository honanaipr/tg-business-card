import logging
from collections.abc import Callable
from functools import wraps
from typing import Any
from urllib.parse import quote

from aiogram import Dispatcher, Router
from aiogram_dialog import Dialog
from loguru import logger
from peewee import ModelSelect

from business_card.db import User
from business_card.exceptions import APIError, DBError


def raises(exception: type[Exception]) -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def wrapper(*args: Any, **kwds: Any) -> Any:  # noqa: ANN401
            try:
                return f(*args, **kwds)
            except Exception as e:
                raise exception from e

        return wrapper

    return decorator


@raises(APIError)
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


@raises(DBError)
def is_admin(id: int) -> bool:
    is_admin = User.select().where((User.id == id) & (User.is_admin == True)).exists()
    return is_admin


@raises(DBError)
def add_admin(from_user: User) -> None:
    user, created = User.get_or_create(
        id=from_user.id, defaults={"name": from_user.name}
    )
    user.is_admin = True
    user.save()


@raises(DBError)
def get_users() -> ModelSelect:
    return User.select()
