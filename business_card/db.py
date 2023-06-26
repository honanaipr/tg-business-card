from tinydb import TinyDB, Query
from pathlib import Path

db = TinyDB(Path.cwd() / "db.json", indent=1)
users = db.table("users")
