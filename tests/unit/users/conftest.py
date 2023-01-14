import pytest

from app.users import scheme as shm


@pytest.fixture()
def login_sheme_example():
    data = {
        "email": "user@test.com",
        "password": "test_password"
    }
    return shm.Login(**data)


@pytest.fixture()
def user_scheme_example():
    data = {
        "username": "TestUser",
        "email": "user@test.com",
        "password": "test_password"
    }
    return shm.User(**data)
