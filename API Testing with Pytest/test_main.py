import pytest
from fastapi.testclient import TestClient

from main import app, todos

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_todos():
    todos.clear()
    yield
    todos.clear()


def test_get_todos_returns_empty_list():
    response = client.get("/todos")

    assert response.status_code == 200
    assert response.json() == []


def test_create_and_get_todo():
    create_response = client.post(
        "/todos",
        json={"title": "Learn FastAPI", "completed": False},
    )

    assert create_response.status_code == 201
    assert create_response.json() == {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False,
    }

    assert client.get("/todos").json() == [create_response.json()]

    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json() == create_response.json()


def test_update_todo():
    client.post("/todos", json={"title": "Learn FastAPI"})

    response = client.put(
        "/todos/1",
        json={"title": "Practice FastAPI", "completed": True},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Practice FastAPI",
        "completed": True,
    }


def test_delete_todo():
    client.post("/todos", json={"title": "Learn FastAPI"})

    response = client.delete("/todos/1")

    assert response.status_code == 204
    assert response.content == b""
    assert client.get("/todos").json() == []


@pytest.mark.parametrize(
    "method, path, payload",
    [
        ("get", "/todos/999", None),
        ("put", "/todos/999", {"title": "Missing todo"}),
        ("delete", "/todos/999", None),
    ],
)
def test_item_routes_return_404_for_missing_todo(method, path, payload):
    request = getattr(client, method)
    response = request(path) if payload is None else request(path, json=payload)

    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_create_todo_requires_title():
    response = client.post("/todos", json={"completed": False})

    assert response.status_code == 422
