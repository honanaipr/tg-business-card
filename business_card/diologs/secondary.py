from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel

from business_card.states import MainSG, SecondarySG

secondary_diolog = Dialog(
    Window(
        Const("Secondary first"),
        Row(
            SwitchTo(id="btn_help", text=Const("Second"), state=SecondarySG.seccond),
            SwitchTo(id="btn_settings", text=Const("Third"), state=SecondarySG.third),
            Cancel(text=Const("Main menu"))
        ),
        state=SecondarySG.first
    ),
    Window(
        Const("Secondary second"),
        SwitchTo(id="btn_main", text=Const("Back"), state=SecondarySG.first),
        state=SecondarySG.seccond
    ),
    Window(
        Const("Secondary third"),
        SwitchTo(id="btn_main", text=Const("Back"), state=SecondarySG.first),
        state=SecondarySG.third
    )
)
