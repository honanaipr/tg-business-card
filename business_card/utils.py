from aiogram import Dispatcher, Router
from aiogram_dialog import Dialog, DialogRegistry

def add_dialog(registry: DialogRegistry, dialog: Dialog, router: Router):
    registry.register(dialog)
    registry.dp.include_router(router)