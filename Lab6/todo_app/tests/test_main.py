# tests/test_main.py

from fastapi.testclient import TestClient
from main import app  # import your FastAPI instance

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "string", "description": "string", "price": 0, "tax": 3.2},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["item"]["name"] == "string"

    print(response.json())

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "item_id" in data
