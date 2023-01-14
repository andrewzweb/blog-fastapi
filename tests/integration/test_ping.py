import pytest
import httpx


@pytest.mark.asyncio
async def test_get_root_page(web_client: httpx.AsyncClient):
    response = await web_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
