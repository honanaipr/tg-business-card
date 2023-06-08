from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Start
from aiogram_dialog.widgets.media import StaticMedia, Media

from aiogram.types import ContentType

from business_card.states import MainSG, SecondarySG
from business_card.utils import get_placehold_image_url

main_diolog = Dialog(
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Main window")), type=ContentType.PHOTO),
        Row(
            SwitchTo(id="btn_help", text=Const("Help"), state=MainSG.help),
            SwitchTo(id="btn_settings", text=Const("Settings"), state=MainSG.settings),
        ),
        Start(id="btn_secondary", state=SecondarySG.first, text=Const("To secondary")),
        state=MainSG.main
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Help window")), type=ContentType.PHOTO),
        SwitchTo(id="btn_main", text=Const("Back"), state=MainSG.main),
        state=MainSG.help
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Settings window")), type=ContentType.PHOTO),
        SwitchTo(id="btn_main", text=Const("Back"), state=MainSG.main),
        state=MainSG.settings
    )
)
    