import os
os.environ["TESTING"] = "True"

import asyncio
import pytest
import pytest_asyncio
import httpx
from asgi_lifespan import LifespanManager

from app.main import app


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def web_client():
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test-app.io/") as _client:
            yield _client
