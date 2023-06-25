from tinydb import TinyDB, Query
from pathlib import Path

db = TinyDB(Path.cwd() / "users.json")
users = db.table("users")
