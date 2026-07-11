from fastapi import FastAPI
from routers import todos, users

app = FastAPI(title="To-Do List API")

app.include_router(users.router)
app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}