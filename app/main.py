from fastapi import FastAPI, HTTPException

from app import database
from app.models import TodoCreate, TodoUpdate, TodoResponse

app = FastAPI(title="Todo API")


@app.get("/todos", response_model=list[TodoResponse])
def list_todos():
    return database.get_all()


@app.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate):
    return database.create(todo)


@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    todo = database.get_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate):
    updated = database.update(todo_id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if not database.delete(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
