from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_inject():
    data = {
        "token_sequence": ["wisdom", "cycle", "light"],
        "embedding_space": "R5",
        "timestamp": 12345.6
    }
    response = client.post("/inject", json=data)
    assert response.status_code == 200
    assert "segment" in response.json()
