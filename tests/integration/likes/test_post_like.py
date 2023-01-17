import pytest
import json


@pytest.mark.asyncio
@pytest.mark.parametrize("collection_name", ["likes"])
async def test_create_like_to_post(web_client, get_token, post_db, collection):
    # create user
    route = "/api/likes/"
    likes_data = {"post": post_db["id"], "reaction": True}
    headers = {"Authorization": "Bearer {}".format(get_token.access_token)}

    response = await web_client.post(
        route, data=json.dumps(likes_data), headers=headers
    )

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["post"] == likes_data["post"]
    assert response.json()["reaction"] == likes_data["reaction"]
    assert "user" in response.json()

    assert await collection.count() == 1


@pytest.mark.asyncio
@pytest.mark.parametrize("collection_name", ["likes"])
async def test_create_like_to_post_and_change_to_unlike(
    web_client, get_token, post_db, collection
):
    # setup
    assert await collection.count() == 0

    # like
    route = "/api/likes/"
    likes_data = {"post": post_db["id"], "reaction": True}
    headers = {"Authorization": "Bearer {}".format(get_token.access_token)}

    print(likes_data)
    response = await web_client.post(
        route, data=json.dumps(likes_data), headers=headers
    )

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["post"] == likes_data["post"]
    assert response.json()["reaction"] == likes_data["reaction"]
    assert "user" in response.json()

    assert await collection.count() == 1

    # unlike
    route = "/api/likes/"
    likes_data = {"post": post_db["id"], "reaction": False}
    print(likes_data)
    response = await web_client.post(
        route, data=json.dumps(likes_data), headers=headers
    )

    assert "id" in response.json()
    assert response.json()["post"] == likes_data["post"]
    assert response.json()["reaction"] == likes_data["reaction"]
    assert "user" in response.json()

    assert await collection.count() == 1
