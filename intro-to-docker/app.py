# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os

app = FastAPI(title="Todo API")
todos = []
next_id = 1

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "python_version": os.getenv("PYTHON_VERSION", "unknown")
    }

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo_data: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        title=todo_data.title,
        completed=todo_data.completed
    )
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Todo deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
