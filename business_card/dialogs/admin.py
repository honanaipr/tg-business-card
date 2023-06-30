from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ContentType, Message
from aiogram_dialog import (
    Dialog,
    DialogManager,
    DialogProtocol,
    ShowMode,
    StartMode,
    Window,
)
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Back,
    Button,
    Cancel,
    Group,
    Next,
    Row,
    Start,
    SwitchTo,
)
from aiogram_dialog.widgets.media import Media, StaticMedia
from aiogram_dialog.widgets.text import Const, Format, Multi

from business_card.dialogs.windows.confirm import ConfirmWindow
from business_card.states import MainSG, TranslateSG
from business_card.utils import add_admin, get_placeholder_image_url, is_admin


class AdminSG(StatesGroup):
    index = State()
    add_admin = State()
    confirm_add_admin = State()
    admin_added = State()


async def name_handler(
    message: Message, message_input: MessageInput, manager: DialogManager
):
    user = message.forward_from.id if message.forward_from else message.from_user
    manager.dialog_data["user_id"] = user.id
    manager.dialog_data["user_name"] = user.full_name
    await manager.switch_to(AdminSG.confirm_add_admin)


async def on_add_admin(c, button, manager: DialogManager):
    add_admin(manager.dialog_data["user_id"])
    manager.show_mode = ShowMode.EDIT
    await c.message.delete()
    await c.message.answer("Администратор добавлен")


admin_dialog = Dialog(
    Window(
        StaticMedia(
            url=Const(get_placeholder_image_url(text="Admin panel")),
            type=ContentType.PHOTO,
        ),
        Const("Admins options"),
        Const("/get_users"),
        Const("/add_admin"),
        Cancel(Const("\N{Leftwards Arrow with Hook} Back")),
        state=AdminSG.index,
    ),
    Window(
        Multi(
            Const("Send user id or forward user's message hear"),
            Const("or /cancel"),
        ),
        MessageInput(name_handler),
        state=AdminSG.add_admin,
    ),
    ConfirmWindow(
        what_to_confirm=Format(
            "Username: {dialog_data[user_name]}\nid: {dialog_data[user_id]}"
        ),
        state=AdminSG.confirm_add_admin,
        on_ok=on_add_admin,
    ),
)
