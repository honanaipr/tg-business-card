"""
This file contain all states of bot's fsm,
to avoid circular imports.
"""
from aiogram.fsm.state import State, StatesGroup


class MainSG(StatesGroup):
    main = State()
    main_admin = State()
    help = State()
    settings = State()
    services = State()


class TranslateSG(StatesGroup):
    main = State()
    settings = State()


class SecondarySG(StatesGroup):
    first = State()
    second = State()
    third = State()


class TgServiceSG(StatesGroup):
    main = State()


class AdminSG(StatesGroup):
    index = State()
    add_admin = State()
    confirm_add_admin = State()
    admin_added = State()
