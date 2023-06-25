from tinydb import TinyDB, Query
from pathlib import Path

db = TinyDB(Path.cwd() / "db.json")
users = db.table("users")
