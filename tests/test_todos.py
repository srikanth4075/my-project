from fastapi.testclient import TestClient

from app.main import app
from app import database


client = TestClient(app)


def setup_function():
    database._todos.clear()
    database._next_id = 1


def test_list_empty():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo():
    response = client.post("/todos", json={"title": "Test task"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test task"
    assert data["description"] is None
    assert data["completed"] is False


def test_create_todo_with_description():
    response = client.post(
        "/todos", json={"title": "Task", "description": "Some details"}
    )
    assert response.status_code == 201
    assert response.json()["description"] == "Some details"


def test_get_todo():
    client.post("/todos", json={"title": "Task"})
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Task"


def test_get_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404


def test_list_todos():
    client.post("/todos", json={"title": "First"})
    client.post("/todos", json={"title": "Second"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_todo():
    client.post("/todos", json={"title": "Task"})
    response = client.put("/todos/1", json={"completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    assert data["title"] == "Task"


def test_update_todo_title():
    client.post("/todos", json={"title": "Old title"})
    response = client.put("/todos/1", json={"title": "New title"})
    assert response.status_code == 200
    assert response.json()["title"] == "New title"


def test_update_todo_not_found():
    response = client.put("/todos/999", json={"title": "Nope"})
    assert response.status_code == 404


def test_delete_todo():
    client.post("/todos", json={"title": "Task"})
    response = client.delete("/todos/1")
    assert response.status_code == 204
    assert client.get("/todos").json() == []


def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
