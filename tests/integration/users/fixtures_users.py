import pytest

from app.users import scheme as shm


@pytest.fixture
def user_in_example():
    data = {
        "username": "testuser",
        "email": "user@test.com",
        "password": "test_pass",
        "password2": "test_pass",
    }
    return shm.UserIn(**data)
