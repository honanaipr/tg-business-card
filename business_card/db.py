from pathlib import Path

from tinydb import Query, TinyDB
from tinydb.table import Table

from business_card.config import config

db = TinyDB(Path.cwd() / "db.json", indent=1)
cache_size = 0 if config.debug else Table.default_query_cache_capacity
users = db.table("users", cache_size=cache_size)
