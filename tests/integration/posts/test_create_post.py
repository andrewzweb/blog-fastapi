import pytest
import json


@pytest.mark.asyncio
async def test_create_post(web_client, get_token, user_db):
    # create user
    route = '/api/posts/'
    post_data = {
        "title": "Test Post",
        "description": "Post Description"
    }
    headers = {"Authorization": "Bearer {}".format(get_token.access_token)}


    response = await web_client.post(route, data=json.dumps(post_data), headers=headers)

    assert response.status_code == 201

    assert "id" in response.json()
    assert response.json()["title"] == post_data["title"]
    assert response.json()["description"] == post_data["description"]
    assert "user" in response.json()
