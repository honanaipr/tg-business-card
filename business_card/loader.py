from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import BaseStorage
from loguru import logger

from business_card.config import config

# if config.TELEGRAM_TEST_SERVER:
#     bot.server = TELEGRAM_TEST
# TODO test server

storage: BaseStorage
if config.redis.host and config.redis.port:
    from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
    from redis.asyncio import Redis

    storage = RedisStorage(
        Redis(host=config.redis.host, port=config.redis.port),
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )
    logger.info(f"redis host: {config.redis.host}, redis port: {config.redis.port}")
elif config.redis.url:
    from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage

    storage = RedisStorage.from_url(
        config.redis.url, key_builder=DefaultKeyBuilder(with_destiny=True)
    )
    logger.info(f"redis url: {config.redis.url}")
else:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()

bot = Bot(token=config.bot.token)
dp = Dispatcher(storage=storage)
