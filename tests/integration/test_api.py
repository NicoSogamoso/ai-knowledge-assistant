import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_chat_valid():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/api/v1/chat", json={"question": "¿Qué es FastAPI?"})
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert data["provider"] == "bootstrap-local"

@pytest.mark.asyncio
async def test_chat_too_short():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/api/v1/chat", json={"question": "ab"})
        assert response.status_code == 422

@pytest.mark.asyncio
async def test_info():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/api/v1/info")
        assert response.status_code == 200
        data = response.json()
        assert data["llm_enabled"] is False
