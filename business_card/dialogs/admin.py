from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, ContentType, Message
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
from loguru import logger

from business_card.db import User
from business_card.dialogs.windows.confirm import ConfirmWindow
from business_card.exceptions import DBError
from business_card.states import AdminSG, MainSG, TranslateSG
from business_card.utils import add_admin, get_placeholder_image_url, is_admin


async def name_handler(
    message: Message, message_input: MessageInput, manager: DialogManager
):
    user = message.forward_from if message.forward_from else message.from_user
    if not user:
        return
    try:
        manager.dialog_data["user"] = User(id=user.id, name=user.full_name).to_dict()
    finally:
        await manager.switch_to(AdminSG.confirm_add_admin)


async def on_add_admin(c: CallbackQuery, button: Button, manager: DialogManager):
    # add_admin(manager.dialog_data["user_id"], manager.dialog_data["user_name"])
    if not is_admin(c.from_user.id):
        logger.warning("Someone non admin try to use add admin")
        return
    message = "Администратор добавлен"
    try:
        add_admin(User(**manager.dialog_data["user"]))
    except DBError as e:
        logger.exception(e)
        message = "Не удалось добавить администратора"
    # manager.show_mode = ShowMode.EDIT
    if not c.message:
        return
    await c.message.delete()
    await c.message.answer(message)


admin_dialog = Dialog(  # type: ignore
    Window(
        StaticMedia(
            url=Const(get_placeholder_image_url(text="Admin panel")),
            type=ContentType.PHOTO,
        ),
        Const("Admins options"),
        Const("/get_users - get user's list\N{scroll}"),
        Const("/add_admin - add new admin 🆕"),
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
            "Username: {dialog_data[user][name]}\nid: {dialog_data[user][id]}"
        ),
        state=AdminSG.confirm_add_admin,
        on_ok=on_add_admin,
    ),
)
