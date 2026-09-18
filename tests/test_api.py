import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from uuid import uuid4

@pytest.mark.asyncio
async def test_ticket_buy():
    async with AsyncClient(base_url = "http://test",transport = ASGITransport(app = app)) as ac:
        response = await ac.post("/tickets/purchase", json = {
            "user_id" : str(uuid4()),
            "seats" : [
                [
                    1, 2
                ]
            ],
            "age" : 18,
            "vip_flag" : True
        })
        assert response.status_code == 200


