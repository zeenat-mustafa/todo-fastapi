from fastapi import APIRouter, HTTPException
from models import TodoCreate, TodoUpdate, Todo
import database

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


# CREATE a new todo
@router.post("/", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo = {
        "id": database.get_next_id(),
        "title": todo.title,
        "completed": todo.completed
    }
    database.todos.append(new_todo)
    return new_todo


# GET all todos
@router.get("/", response_model=list[Todo])
def get_todos():
    return database.todos


# GET a single todo by id
@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in database.todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# UPDATE a todo
@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: TodoUpdate):
    for todo in database.todos:
        if todo["id"] == todo_id:
            if updated.title is not None:
                todo["title"] = updated.title
            if updated.completed is not None:
                todo["completed"] = updated.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# DELETE a todo
@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for todo in database.todos:
        if todo["id"] == todo_id:
            database.todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")