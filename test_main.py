from fastapi.testclient import TestClient
from main import app, tasks_db

client = TestClient(app)

def setup_function():
    tasks_db.clear()

def test_create_task():
    response = client.post("/tasks/", json={"id": 1, "title": "Estudar IA", "completed": False})
    assert response.status_code == 201
    assert response.json()["title"] == "Estudar IA"

def test_read_tasks():
    client.post("/tasks/", json={"id": 1, "title": "Tarefa 1"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_update_task():
    client.post("/tasks/", json={"id": 1, "title": "Tarefa 1"})
    response = client.put("/tasks/1?completed=true")
    assert response.status_code == 200
    assert response.json()["completed"] == True

def test_delete_task():
    client.post("/tasks/", json={"id": 1, "title": "Tarefa 1"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert len(tasks_db) == 0