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

