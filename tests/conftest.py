import os

os.environ["TESTING"] = "True"

import asyncio
import pytest
import pytest_asyncio
import httpx
from asgi_lifespan import LifespanManager
from motor import motor_asyncio

from app.main import app
from app.core import config as cf
from app.core.database import Database


pytest_plugins = [
    "tests.integration.users.fixtures_users",
    "tests.integration.posts.fixtures_posts",
]


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """
    Event loop for tests
    """
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="function")
async def db_engine():
    """Database engine

    If job done drop database

    return: AsyncIOMotorClient
    """
    url, db = f"{cf.MONGODB_URL}", f"{cf.DATABASE_NAME}"
    db = motor_asyncio.AsyncIOMotorClient(url)[db]
    yield db
    # drop database
    collections = await db.list_collection_names()
    list(map(lambda collection: db.drop_collection(collection), collections))


@pytest_asyncio.fixture(scope="function")
async def collection(collection_name, db_engine):
    """Collection

    params: collection_name (in test params)
    return: Database(collection_name)
    """
    collection = Database(collection_name, database=db_engine)
    yield collection
    collection.collection.drop()


@pytest_asyncio.fixture(scope="function")
async def web_client():
    """
    Client for testing
    """
    async with LifespanManager(app):
        async with httpx.AsyncClient(
            app=app, base_url="http://test-app.io/"
        ) as _client:
            yield _client
