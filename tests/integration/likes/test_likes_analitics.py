import pytest
import json
from datetime import datetime


def get_likes():

    return [
        {
            "id": 1,
            "post": "7c77c4e45af14551a6889104365cdfe1",
            "reaction": False,
            "user": "dcc128ec24f443bc807baa0e5e529ae4",
            "dateUpdted": datetime.strptime(
                "2023-01-13T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
            "dateCreated": datetime.strptime(
                "2023-01-10T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
        },
        {
            "id": 2,
            "post": "7c77c4e45af14551a6889104365cdfe2",
            "reaction": False,
            "user": "dcc128ec24f443bc807baa0e5e529ae4",
            "dateUpdted": datetime.strptime(
                "2023-01-18T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
            "dateCreated": datetime.strptime(
                "2023-01-15T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
        },
        {
            "id": 3,
            "post": "7c77c4e45af14551a6889104365cdfe3",
            "reaction": True,
            "user": "dcc128ec24f443bc807baa0e5e529ae4",
            "dateUpdted": datetime.strptime(
                "2023-01-22T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
            "dateCreated": datetime.strptime(
                "2023-01-20T15:05:42.704000", "%Y-%m-%dT%H:%M:%S.%f"
            ),
        },
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize("collection_name", ["likes"])
async def test_get_likes_analitics_get_all(web_client, get_token, post_db, collection):
    # setup
    likes = get_likes()
    await collection.collection.insert_many(likes)
    assert await collection.count() == 3

    # like
    route = "/api/likes/analitics/?date_from=2023-01-10&date_to=2025-01-18"

    response = await web_client.get(route)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert len(data) == 3


@pytest.mark.asyncio
@pytest.mark.parametrize("collection_name", ["likes"])
async def test_get_likes_analitics_get_couple(
    web_client, get_token, post_db, collection
):
    # setup
    likes = get_likes()
    await collection.collection.insert_many(likes)
    assert await collection.count() == 3

    # like
    route = "/api/likes/analitics/?date_from=2023-01-15&date_to=2025-01-20"

    response = await web_client.get(route)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert len(data) == 2


@pytest.mark.asyncio
@pytest.mark.parametrize("collection_name", ["likes"])
async def test_get_likes_analitics_get_no_one(
    web_client, get_token, post_db, collection
):
    # setup
    likes = get_likes()
    await collection.collection.insert_many(likes)
    assert await collection.count() == 3

    # like
    route = "/api/likes/analitics/?date_from=2020-01-15&date_to=2020-01-20"

    response = await web_client.get(route)
    data = json.loads(response.content)

    assert response.status_code == 200
    assert len(data) == 0
