from aiogram.types import CallbackQuery, ContentType
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, SwitchTo, Url
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const
from loguru import logger

from business_card.states import TranslateSG
from business_card.utils import get_placeholder_image_url


async def save(event: CallbackQuery, source: Button, manager: DialogManager):
    logger.info("Saved")


translate_dialog = Dialog(  # type: ignore
    Window(
        StaticMedia(
            url=Const(get_placeholder_image_url(text="Translate service")),
            type=ContentType.PHOTO,
        ),
        Const(
            'Нажмите "Попробовать" и выберете чат в который хотите послать собщение.'
        ),
        Url(
            text=Const("✉️ Попробовать"),
            url=Const("https://t.me/intranslabot?start=parameter"),
        ),
        SwitchTo(
            id="btn_translate_settings",
            text=Const("⚙️ Settings"),
            state=TranslateSG.settings,
        ),
        Cancel(text=Const("↩️ Services menu")),
        state=TranslateSG.main,
    ),
    Window(
        StaticMedia(
            url=Const(get_placeholder_image_url(text="Secondary first window")),
            type=ContentType.PHOTO,
        ),
        Row(
            SwitchTo(
                id="btn_translate_save_settings",
                text=Const("✅ Save"),
                state=TranslateSG.main,
                on_click=save,
            ),
            SwitchTo(
                id="btn_translate_discard_settings",
                text=Const("❌ Discard"),
                state=TranslateSG.main,
            ),
        ),
        state=TranslateSG.settings,
    ),
)
