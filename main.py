from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Micro-API de Tarefas",
    description="MVP de um gerenciador de tarefas criado para a pós-graduação.",
    version="1.0.0"
)

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks_db: List[Task] = []

@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: Task):
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Tarefa com este ID já existe.")
    tasks_db.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks(completed: Optional[bool] = None):
    if completed is not None:
        return [t for t in tasks_db if t.completed == completed]
    return tasks_db

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, completed: bool):
    for t in tasks_db:
        if t.id == task_id:
            t.completed = completed
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks_db):
        if t.id == task_id:
            del tasks_db[i]
            return {"message": "Tarefa excluída com sucesso."}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")