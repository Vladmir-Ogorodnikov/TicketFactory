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


@pytest.mark.asyncio
async def test_purchase_invalid_age():
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as ac:
        response = await ac.post("/tickets/purchase" , json = {
            "user_id": str(uuid4()),
            "seats": [
                [
                    1, 2
                ]
            ],
            "age": -5,
            "vip_flag": True
        })

        assert response.status_code == 422

@pytest.mark.asyncio
async def test_receipt_byid():
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as ac:
        response_1 = await ac.post("/tickets/purchase" , json = {
            "user_id": str(uuid4()),
            "seats": [
                [
                    1, 2
                ]
            ],
            "age": 18,
            "vip_flag": True
        })

        receipt_id = response_1.json()["receipt_id"]
        post_data = response_1.json()

        response_2 = await ac.get(f"/tickets/{receipt_id}")
        get_data = response_2.json()

        assert response_2.status_code == 200
        assert post_data["receipt_id"] == get_data["receipt_id"]
        assert post_data["user_id"] == get_data["user_id"]
        assert post_data["tickets"] == get_data["tickets"]
        assert post_data["total_amount"] == get_data["total_amount"]
        assert post_data["created_at"] == get_data["created_at"]







