from typing import Any

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    name = fields.TextField()
    is_admin = fields.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }
