from click import password_option
from app.models import UserDbType, UserDbTypeUpdate, UserDbTypeId, UserDbModel
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import pytest
import asyncio


@pytest.fixture
def db_fixture(
    params=(
        (("Adam", "I am adam"), ("Smith", None)),
        (("Bob", "mysecret"), (None, "my New Secret")),
        (("Carol", "abaabagba"), ("louis", "HeyYo!")),
    )
):
    app = FastAPI()
    register_tortoise(
        app,
        db_url="sqlite://test_tmp.db",
        modules={"models": ["app.models"]},
        config={
            "apps": {
                "models": {
                    "default_connection": "default",
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )
    yield params


def test_db_users(db_fixture):
    async def create(data: UserDbType):
        created_data = await UserDbModel.create(**data.dict())
        return created_data

    async def read(id: int):
        return await UserDbModel.get(id)

    async def update(id: int):
        data = await read(id=id)
        await data.save()

    async def delete(id: int):
        data = await read(id=id)
        data.delete()
        return

    for (
        (create_name, create_credential),
        (update_name, update_credential),
    ) in db_fixture:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            create(UserDbType(name=create_name, credential=create_credential))
        )
        pass

    assert False
