import pytest

from app.users import service as srv


def test_create_SingupUser(user_scheme_example):
    user_fake = user_scheme_example

    user = srv.SingupUser(user_fake)

    assert user
    assert user.data == user_fake


@pytest.mark.asyncio
async def test_SingupUser_create_user(user_scheme_example, mocker):
    user = user_scheme_example
    mock_create_user = mocker.patch(
        "app.users.service.SingupUser.create_user", return_value=user.dict()
    )

    user = await srv.SingupUser(user_scheme_example).create_user()

    assert user
    mock_create_user.assert_called()
