import pytest
import json
from Apps.web import app as alex_app  # importing web app from file


@pytest.fixture
def app():
    yield alex_app

@pytest.fixture
def client(app):  # passing the app inside
    return app.test_client()


# Testing our Flask web app routs
def test_index_func(app, client):  # testing the first route
    response = client.get('/')  # the first route
    assert response.status_code == 200  # checking status code
    assert response.data == b'{"hi":"alex"}\n'  # checking data


def test_my_endpoint():
    with app.test_client() as client:
        response = client.get('/my-endpoint')
        assert response.status_code == 200
        assert response.data == 'hello world'


def test_my_endpoint2():
    client = app.test_client()
    response = client.get('/my-endpoint')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
