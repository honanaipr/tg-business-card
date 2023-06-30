from collections.abc import Callable, Coroutine
from typing import Optional

from aiogram.fsm.state import State
from aiogram_dialog import ShowMode, Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Keyboard, Row, Start
from aiogram_dialog.widgets.kbd.button import OnClick
from aiogram_dialog.widgets.text import Const, Format, Text
from aiogram_dialog.widgets.utils import GetterVariant, WidgetSrc


class ConfirmWindow(Window):
    def __init__(self, what_to_confirm: Text, state: State, on_ok: OnClick):
        super().__init__(
            Const("Подтвердите выбор:"),
            what_to_confirm,
            Row(
                Cancel(
                    text=Const("\N{white heavy check mark}"),
                    id="btn_yes",
                    on_click=on_ok,
                ),
                Cancel(text=Const("\N{Cross Mark}"), id="btn_no"),
            ),
            state=state,
        )
