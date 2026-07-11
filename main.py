from fastapi import FastAPI
from routers import todos

app = FastAPI(title="To-Do List API")

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}