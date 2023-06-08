from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Start

from business_card.states import MainSG, SecondarySG

main_diolog = Dialog(
    Window(
        Const("started"),
        Row(
            SwitchTo(id="btn_help", text=Const("Help"), state=MainSG.help),
            SwitchTo(id="btn_settings", text=Const("Settings"), state=MainSG.settings),
        ),
        Start(id="btn_secondary", state=SecondarySG.first, text=Const("To secondary")),
        state=MainSG.main
    ),
    Window(
        Const("help"),
        SwitchTo(id="btn_main", text=Const("Back"), state=MainSG.main),
        state=MainSG.help
    ),
    Window(
        Const("settings"),
        SwitchTo(id="btn_main", text=Const("Back"), state=MainSG.main),
        state=MainSG.settings
    )
)
    