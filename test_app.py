from app import app as flask_app


def test_hello_world():
    client = flask_app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data
