import requests
import json


def test_flask_app():
    url = "http://127.0.0.1:5000/query"
    headers = {"Content-Type": "application/json"}
    data = {"query": "any laptop?"}
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    assert response.status_code == 200


if __name__ == "__main__":
    test_flask_app()
