from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID

app = FastAPI(title="To-Do API")

# 요청/응답 모델 정의
class TodoCreate(BaseModel):
    title: str
    description: str = ""

class Todo(BaseModel):
    id: UUID
    title: str
    description: str
    completed: bool

# 임시 메모리 DB
DB: dict[UUID, Todo] = {}

# 라우트 정의
@app.get("/")
def root():
    return {"message": "Welcome to To-Do API"}

@app.post("/todos", response_model=Todo)
def create(todo: TodoCreate):
    todo_id = uuid4()
    new_todo = Todo(id=todo_id, title=todo.title, description=todo.description, completed=False)
    DB[todo_id] = new_todo
    return new_todo

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return list(DB.values())

@app.put("/todos/{todo_id}", response_model=Todo)
def update(todo_id: UUID, todo: TodoCreate):
    if todo_id not in DB:
        return {"error": "Todo not found"}
    updated = Todo(id=todo_id, title=todo.title, description=todo.description, completed=False)
    DB[todo_id] = updated
    return updated

@app.delete("/todos/{todo_id}")
def delete(todo_id: UUID):
    if todo_id not in DB:
        return {"error": "Todo not found"}
    del DB[todo_id]
    return {"message": "Deleted successfully"}

@app.patch("/todos/{todo_id}/complete", response_model=Todo)
def mark_complete(todo_id: UUID):
    if todo_id not in DB:
        return {"error": "Todo not found"}
    todo = DB[todo_id]
    updated = Todo(id=todo.id, title=todo.title, description=todo.description, completed=True)
    DB[todo_id] = updated
    return updated
