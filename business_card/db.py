import asyncio

from tortoise import Tortoise, run_async

from business_card.models import User


async def init_db() -> None:
    await Tortoise.init(
        config_file="business_card/tortoise_config.json",
    )
    await Tortoise.generate_schemas()
