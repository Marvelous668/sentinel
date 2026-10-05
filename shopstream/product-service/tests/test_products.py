from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_product():
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Wireless Headphones"


def test_product_not_found():
    response = client.get("/products/999")

    assert response.status_code == 404