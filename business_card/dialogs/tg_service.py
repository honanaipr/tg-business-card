from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel, Row, SwitchTo, Url
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const
from loguru import logger

from business_card.states import TgServiceSG
from business_card.utils import get_placeholder_image_url

tg_service_dialog = Dialog(  # type: ignore
    Window(
        StaticMedia(
            url=Const(get_placeholder_image_url(text="Translate service")),
            type=ContentType.PHOTO,
        ),
        Const(
            'Нажмите "Попробовать" и выберете чат в который хотите послать собщение.'
        ),
        Cancel(text=Const("↩️ Services menu")),
        state=TgServiceSG.main,
    ),
)
