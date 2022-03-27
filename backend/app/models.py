from datetime import datetime
from pydantic import BaseModel, Field
from tortoise.models import Model
from tortoise import fields


class UserDbType(BaseModel):
    name: str
    credential: str
    creation_time: datetime = Field(default_factory=datetime.now)
    update_time: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class UserDbTypeUpdate(UserDbType):
    name: str
    credential: str
    update_time: datetime = Field(default_factory=datetime.now)


class UserDbTypeId(UserDbType):
    id: int


class UserDbModel(Model):
    id = fields.IntField(pk=True, generated=True)
    name = fields.CharField(max_length=255, null=False)
    credential = fields.CharField(max_length=255, null=False)
    creation_time = fields.DatetimeField(null=False)

    class Meta:
        table = "users"
