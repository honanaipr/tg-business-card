from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram import Bot, Dispatcher
from business_card.config import config

storage = RedisStorage.from_url(config.redis.url, key_builder=DefaultKeyBuilder(with_destiny=True))
bot = Bot(token=config.bot.token)
dp = Dispatcher(storage=storage)