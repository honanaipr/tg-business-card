from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel
from aiogram_dialog.widgets.media import StaticMedia

from aiogram.types import ContentType

from business_card.states import MainSG, TranslateSG, SecondarySG
from business_card.utils import get_placehold_image_url

secondary_diolog = Dialog(
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Secondary first window")), type=ContentType.PHOTO),
        Row(
            SwitchTo(id="btn_help", text=Const("Second"), state=SecondarySG.seccond),
            SwitchTo(id="btn_settings", text=Const("Third"), state=SecondarySG.third),
            Cancel(text=Const("Main menu"))
        ),
        state=SecondarySG.first
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Secondary second window")), type=ContentType.PHOTO),
        SwitchTo(id="btn_main", text=Const("Back"), state=SecondarySG.first),
        state=SecondarySG.seccond
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Secondary third window")), type=ContentType.PHOTO),
        SwitchTo(id="btn_main", text=Const("Back"), state=SecondarySG.first),
        state=SecondarySG.third
    )
)
