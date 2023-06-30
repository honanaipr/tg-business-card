from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel, Url
from aiogram_dialog.widgets.media import StaticMedia

from aiogram.types import ContentType

from business_card.states import TranslateSG
from business_card.utils import get_placeholder_image_url
from loguru import logger

async def save(event, source, manager):
    logger.info("Saved")


translate_dialog = Dialog(
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Translate service")), type=ContentType.PHOTO),
        Const('Нажмите "Попробовать" и выберете чат в который хотите послать собщение.'),
        Url(text=Const("✉️ Попробовать"), url=Const("https://t.me/intranslabot?start=parameter")),
        SwitchTo(id="btn_translate_settings", text=Const("⚙️ Settings"), state=TranslateSG.settings),
        Cancel(text=Const("↩️ Services menu")),
        state=TranslateSG.main
    ),
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Secondary first window")), type=ContentType.PHOTO),
        Row(
            SwitchTo(id="btn_translate_save_settings" ,text=Const("✅ Save"), state=TranslateSG.main, on_click=save),
            SwitchTo(id="btn_translate_discard_settings" ,text=Const("❌ Discard"), state=TranslateSG.main)
        ),
        state=TranslateSG.settings
    ),
)
