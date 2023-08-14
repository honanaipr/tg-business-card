from datetime import date

from peewee import (
    BigIntegerField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
)

db = SqliteDatabase("people.sqlite3")


class Base(Model):
    def to_dict(self) -> dict:
        return self.__dict__["__data__"]

    class Meta:
        database = db


class User(Base):
    id = BigIntegerField(primary_key=True)
    name = CharField()
    is_admin = BooleanField(default=False)

    class Meta:
        table_name = "users"


with db:
    db.create_tables([User])
