from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_default_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 0.2,
            "sepal_width": 0.2,
            "petal_length": 0.2,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"prediction": "setosa"}
