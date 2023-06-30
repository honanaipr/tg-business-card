from typing import List, Optional
from aiogram.fsm.state import State
from aiogram_dialog import Window, ShowMode
from aiogram_dialog.widgets.kbd import Button, Keyboard, Row, Start, Cancel
from aiogram_dialog.widgets.text import Const, Format, Text
from aiogram_dialog.widgets.utils import GetterVariant, WidgetSrc
from aiogram.fsm.state import State

from typing import Callable, Coroutine

class ConfirmWindow(Window):
    def __init__(self, what_to_confirm: Text, state: State, on_ok: Callable | Coroutine):
        super().__init__(
            Const("Подтвердите выбор:"),
            what_to_confirm,
            Row(
                Cancel(
                    text=Const("\N{white heavy check mark}"),
                    id="btn_yes",
                    on_click=on_ok
                ),
                Cancel(
                    text=Const("\N{Cross Mark}"),
                    id="btn_no"
                )
            ),
            state=state,
        )
