import json
from flask import Flask, request
from flask.testing import FlaskClient
import pytest

from imdb import connect


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.add_url_rule('/', view_func=connect, methods=['POST'])
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_connect(client: FlaskClient):
    # Define the input data for the test
    input_data = {'sentiment': 'positive'}
    input_json = json.dumps(input_data)

    # Send a POST request to the endpoint
    response = client.post('/', json=input_json)

    # Assert that the response contains the expected data
    assert response.status_code == 200
    assert 'response' in response.json
    assert isinstance(response.json['response'], list)

    # Assert that the movies in the response have the expected keys
    for movie in response.json['response']:
        assert isinstance(movie, dict)
        assert 'title' in movie
        assert 'genre' in movie
        assert 'image_url' in movie
