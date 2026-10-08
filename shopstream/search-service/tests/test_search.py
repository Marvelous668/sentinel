from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@patch("app.main.httpx.get")
def test_search_products(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = [
        {
            "id": 1,
            "name": "Wireless Headphones",
            "price": 45000,
            "category": "Electronics",
        },
        {
            "id": 2,
            "name": "Mechanical Keyboard",
            "price": 35000,
            "category": "Electronics",
        },
    ]

    mock_get.return_value = mock_response

    response = client.get("/search?q=headphones")

    assert response.status_code == 200
    assert response.json()["query"] == "headphones"
    assert len(response.json()["results"]) == 1
    assert response.json()["results"][0]["name"] == "Wireless Headphones"


@patch("app.main.httpx.get")
def test_search_no_match(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = [
        {
            "id": 1,
            "name": "Wireless Headphones",
            "price": 45000,
            "category": "Electronics",
        }
    ]

    mock_get.return_value = mock_response

    response = client.get("/search?q=laptop")

    assert response.status_code == 200
    assert response.json()["results"] == []


def test_search_requires_query():
    response = client.get("/search")

    assert response.status_code == 422