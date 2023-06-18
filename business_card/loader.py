from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram import Bot, Dispatcher

API_TOKEN = '6244180609:AAGl8bZGQ3fG_otyQONWvu-c6ukKvILJohY'

storage = RedisStorage.from_url("redis://localhost:6379/db", key_builder=DefaultKeyBuilder(with_destiny=True))
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)