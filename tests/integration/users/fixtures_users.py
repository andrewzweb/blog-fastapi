import pytest
import pytest_asyncio

from app.users import scheme as shm
from app.users import service as srv

@pytest_asyncio.fixture()
def user_in_example():
    data = {
        "username": "testuser",
        "email": "user@test.com",
        "password": "test_pass",
        "password2": "test_pass",
    }
    return shm.UserIn(**data)


@pytest_asyncio.fixture()
async def user_db(user_in_example):
    return await srv.SingupUser(user_in_example).create_user()


@pytest_asyncio.fixture()
async def get_token(user_db, user_in_example):
    return await srv.LoginUser(user_in_example).login()
