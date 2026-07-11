from fastapi import APIRouter, HTTPException, Depends
from models import TodoCreate, TodoUpdate, Todo
import database
from auth import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


# CREATE a new todo
@router.post("/", response_model=Todo)
def create_todo(todo: TodoCreate, current_user: dict = Depends(get_current_user)):
    new_todo = {
        "id": database.get_next_id(),
        "title": todo.title,
        "completed": todo.completed
    }
    database.todos.append(new_todo)
    return new_todo


# GET all todos
@router.get("/", response_model=list[Todo])
def get_todos(current_user: dict = Depends(get_current_user)):
    return database.todos


# GET a single todo by id
@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int, current_user: dict = Depends(get_current_user)):
    for todo in database.todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# UPDATE a todo
@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: TodoUpdate, current_user: dict = Depends(get_current_user)):
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
def delete_todo(todo_id: int, current_user: dict = Depends(get_current_user)):
    for todo in database.todos:
        if todo["id"] == todo_id:
            database.todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")