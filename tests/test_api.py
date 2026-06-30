from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "RetailIQ API Running Successfully"


def test_sales_summary():
    response = client.get("/sales-summary")

    assert response.status_code == 200


def test_top_products():
    response = client.get("/top-products")

    assert response.status_code == 200


def test_sales_by_store():
    response = client.get("/sales-by-store")

    assert response.status_code == 200


def test_low_stock():
    response = client.get("/low-stock")

    assert response.status_code == 200


def test_predict():

    payload = {
        "store": 1,
        "item": 1,
        "year": 2017,
        "month": 6,
        "day": 15,
        "dayofweek": 3,
        "weekofyear": 24,
        "quarter": 2,
        "is_weekend": 0
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200
    assert "predicted_sales" in response.json()
    