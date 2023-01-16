import pytest
import pytest_asyncio

from app.posts import service as srv
from app.posts import scheme as shm


@pytest_asyncio.fixture()
async def new_post_example():
    data = {
        "title": "Test Title",
        "description": "Description"
    }
    return shm.PostIn(**data)


@pytest_asyncio.fixture()
async def post_db(user_db, new_post_example):
    user_id = user_db['id']
    return await srv.PostUseCase().create(new_post_example, user=user_id)
