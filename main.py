from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model = defines the shape/validation of a Todo
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory storage (per instructions: no database)
todos = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}