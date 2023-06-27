from aiogram.types import ContentType
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Button, Group, Row, Start, SwitchTo
from aiogram_dialog.widgets.media import Media, StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from business_card import utils
from business_card.dialogs.admin import AdminSG
from business_card.states import MainSG, TranslateSG
from business_card.utils import get_placeholder_image_url, is_admin


async def main_getter(dialog_manager: DialogManager, **kwargs):
    return {"is_admin": is_admin(dialog_manager.event.from_user.id)}

index_dialog = Dialog(
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Main window")), type=ContentType.PHOTO),
        Row(
            SwitchTo(id="btn_start_services", state=MainSG.services, text=Const("🛠️ Services")),
        ),
        Row(
            SwitchTo(id="btn_help", text=Const("📃❓ Help"), state=MainSG.help),
            SwitchTo(id="btn_settings", text=Const("⚙️ Settings"), state=MainSG.settings),
        ),
        Start(id="btn_goto_admin_index", text=Const("Admin panel"), state=AdminSG.index, when="is_admin"),            
        getter=main_getter,
        state=MainSG.main
    ),
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Services")), type=ContentType.PHOTO),
        Const("Здесь находятся бесплатные сервисы"),
        Group(
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            width=2
        ),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.services
    ),
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Help")), type=ContentType.PHOTO),
        Const("Этот бот умеет несколько прикольных вещей.\n /start - перезапустите бота, если у вас возникли трудности."),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.help
    ),
    Window(
        StaticMedia(url=Const(get_placeholder_image_url(text="Settings window")), type=ContentType.PHOTO),
        Const("Возможно здесь когданибуть будут настройки."),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.settings
    )
)