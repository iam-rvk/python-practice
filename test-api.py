# file: test_api.py
# Sample REST API testing script using requests

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("GET /posts passed")


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    print("GET /posts/1 passed")


def test_create_post():
    payload = {
        "title": "sample title",
        "body": "sample body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    print("POST /posts passed")


if __name__ == "__main__":
    test_get_posts()
    test_get_single_post()
    test_create_post()
    print("All API tests passed.")
