from aiogram.fsm.state import State, StatesGroup

class MainSG(StatesGroup):
    main = State()
    help = State()
    settings = State()
    services = State()

class TranslateSG(StatesGroup):
    main = State()
    settings = State()

class SecondarySG(StatesGroup):
    first = State()
    seccond = State()
    third = State()