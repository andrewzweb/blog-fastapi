import pytest
import json


@pytest.mark.asyncio
async def test_login_exist_user(user_in_example, web_client):
    # create user
    route = "/api/users/"

    response = await web_client.post(route, data=user_in_example.json())

    assert response.status_code == 201
    assert "id" in response.json() and not "hashed_password" in response.json()

    # login user
    route = "/api/users/login/"
    data = {"email": user_in_example.email, "password": user_in_example.password}

    response = await web_client.post(route, data=json.dumps(data))

    assert response.status_code == 200
    assert "access_token" in response.json() and "token_type" in response.json()
