from fastapi.testclient import TestClient
from main import app, tasks_db

client = TestClient(app)

def setup_function():  # Função que executa antes de cada teste
    tasks_db.clear()

# --- Testes Básicos (TDD Happy Path) ---

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

    # --- Testes de Borda (Edge Cases) ---

def test_create_task_duplicate_id():
    """Testa se a API recusa a criação de uma tarefa com ID já existente."""
    client.post("/tasks/", json={"id": 99, "title": "Tarefa Original", "completed": False})
    response = client.post("/tasks/", json={"id": 99, "title": "Tarefa Duplicada", "completed": False})
    assert response.status_code == 400
    assert response.json()["detail"] == "Tarefa com este ID já existe."

def test_read_tasks_empty():
    """Testa o retorno da listagem quando não há tarefas."""  # O setup_function já limpa o banco antes do teste
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_tasks_filtered():
    """Testa os filtros de query string para tarefas concluídas e pendentes."""
    client.post("/tasks/", json={"id": 10, "title": "Feita", "completed": True})
    client.post("/tasks/", json={"id": 11, "title": "Pendente", "completed": False})
    
    response_true = client.get("/tasks/?completed=true")
    assert len(response_true.json()) == 1
    assert response_true.json()[0]["id"] == 10
    
    response_false = client.get("/tasks/?completed=false")
    assert len(response_false.json()) == 1
    assert response_false.json()[0]["id"] == 11

def test_update_task_not_found():
    """Testa a atualização de uma tarefa que não existe."""
    response = client.put("/tasks/999?completed=true")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada."

def test_delete_task_not_found():
    """Testa a exclusão de uma tarefa que não existe."""
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada."