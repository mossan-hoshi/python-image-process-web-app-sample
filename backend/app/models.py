from pydantic import BaseModel, Field
from tortoise.models import Model
from tortoise import fields


class UserDbModel(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=255, null=False)
    credential = fields.CharField(max_length=255, null=False)
    creation_time = fields.DatetimeField(null=False)

    class Meta:
        table = "users"
