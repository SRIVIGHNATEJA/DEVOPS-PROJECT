import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data


def test_health_probe(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'


def test_ready_probe(client):
    response = client.get('/ready')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ready'


def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"flask_http_request_duration_seconds" in response.data or b"app_info" in response.data
