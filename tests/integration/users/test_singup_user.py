import pytest


@pytest.mark.asyncio
async def test_singup_user(user_in_example, web_client):
    route = '/api/users/'

    response = await web_client.post(route, data=user_in_example.json())

    assert response.status_code == 201
    assert "id" in response.json() and not "hash_password" in response.json()

    assert response.json()["username"] == user_in_example.username
    assert response.json()["email"] == user_in_example.email
