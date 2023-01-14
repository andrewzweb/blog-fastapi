import pytest

from app.users import service as srv


def test_create_LoginUser(login_sheme_example):
    login = srv.LoginUser(login_sheme_example)

    assert login
    assert login.email == login_sheme_example.email
    assert login.password == login_sheme_example.password


@pytest.mark.asyncio
async def test_LoginUser_can_login(user_scheme_example, login_sheme_example, mocker):
    user = user_scheme_example

    mock_get_user_from_db = mocker.patch("app.users.service.LoginUser.get_user_from_db", return_value=user)
    mock_check_user_exist = mocker.patch("app.users.service.LoginUser.check_user_exist", return_value=True)
    mock_check_correct_password = mocker.patch("app.users.service.LoginUser.check_correct_password", return_value=True)

    token = await srv.LoginUser(login_sheme_example).login()

    assert token

    mock_get_user_from_db.assert_called()
    mock_check_user_exist.assert_called()
    mock_check_correct_password.assert_called()
