import pytest

from app.users import scheme as shm


def test_validate_login_data():
    login_data = {
        "email": "user@test.com",
        "password": "test_pass"
    }
    login = shm.Login(**login_data)

    assert login
    assert login.email == login_data["email"]
    assert login.password == login_data["password"]


def test_validate_login_wrong():
    login_data = {
        "email": "user@test.com",
    }

    with pytest.raises(Exception) as exc:
        login = shm.Login(**login_data)
        

def test_validate_token_data():
    token_data = {
        "access_token": "access_token",
        "token_type": "token_type"
    }
    token = shm.Token(**token_data)

    assert token
    assert token.access_token == token_data["access_token"]
    assert token.token_type == token_data["token_type"]


def test_validate_UserIn_data():
    user_data = {
        "username": "user_name",
        "email": "user@test.com",
        "password": "test_password",
        "password2": "test_password"
    }
    user = shm.UserIn(**user_data)

    assert user
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]
    assert user.password2 == user_data["password2"]


def test_validate_UserOut_data():
    user_data = {
        "id": "user_id",
        "username": "user_name",
        "email": "user@test.com",
    }
    user = shm.UserOut(**user_data)

    assert user
    assert user.id == user_data["id"]
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
