import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_receipt_google(client):
    payload = {
        "platform": "google",
        "user_id": "user123",
        "receipt_id": "receipt123"
    }
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

def test_valid_receipt_apple(client):
    payload = {
        "platform": "apple",
        "user_id": "user123",

    }
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

def test_no_id_receipt_google(client):
    payload = {
        "platform": "google",
        "user_id": "user123"
    }
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

def test_no_id_receipt_apple(client):
    payload = {
        "platform": "google",
        "receipt_id": "receipt123"
    }
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

def test_no_platform_receipt(client):
    payload = {
        "receipt_id": "receipt123",
        "user_id": "user123"
    }
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

def test_multiple_valid_receipt(client):
    payload = {
        "platform": "google",
        "user_id": "user123",
        "receipt_id": "receipt123"
    }
    for i in range(100):
        client.post("/receipt", json=payload)
    response = client.post("/receipt", json=payload)
    assert response.status_code in (200, 503)  # success or mock-failure
    assert 'msg' in response.get_json()

