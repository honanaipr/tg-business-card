from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel, Url
from aiogram_dialog.widgets.media import StaticMedia

from aiogram.types import ContentType

from business_card.states import TgServiceSG
from business_card.utils import get_placehold_image_url
from loguru import logger

tg_service_dialog = Dialog( 
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Translate service")), type=ContentType.PHOTO),
        Const('Нажмите "Попробовать" и выберете чат в который хотите послать собщение.'),
        Cancel(text=Const("↩️ Services menu")),
        state=TgServiceSG.main
    ),

)