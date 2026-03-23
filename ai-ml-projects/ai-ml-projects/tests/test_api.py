from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_answer_endpoint():
    response = client.post("/answer", json={"question": "Show me API best practices"})
    assert response.status_code == 200
    data = response.json()
    assert data["matched_topic"] == "api"
    assert "status codes" in data["answer"].lower()
