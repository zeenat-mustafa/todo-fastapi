# To-Do List REST API (FastAPI)

A RESTful To-Do List API built with FastAPI, featuring full CRUD operations and JWT-based user authentication. Built as part of Python + AI Bootcamp Week 2 assignment.

## Features
- User registration and login (JWT authentication)
- Create, read, update, and delete to-do tasks
- Protected routes (only logged-in users can manage their tasks)
- In-memory data storage (no database, per assignment requirements)
- Interactive API testing via Swagger UI

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)
- JWT (JSON Web Tokens) for authentication
- Passlib (password hashing)

## Project Structure
```
todo-fastapi/
├── main.py
├── models.py
├── auth.py
├── database.py
├── routers/
│   ├── todos.py
│   └── users.py
├── screenshots/
│   ├── swagger/
│   └── postman/
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup & Installation

1. Clone the repository
```bash
git clone https://github.com/zeenat-mustafa/todo-fastapi.git
cd todo-fastapi
```

2. Create and activate a conda environment
```bash
conda create -n todo-api python=3.11
conda activate todo-api
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn main:app --reload
```

5. Open the interactive API docs in your browser
```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint         | Description              | Auth Required |
|--------|------------------|---------------------------|---------------|
| POST   | /register        | Register a new user       | No            |
| POST   | /login           | Login and get JWT token   | No            |
| POST   | /todos           | Create a new task         | Yes           |
| GET    | /todos           | Get all tasks              | Yes           |
| GET    | /todos/{id}      | Get a task by ID          | Yes           |
| PUT    | /todos/{id}      | Update a task              | Yes           |
| DELETE | /todos/{id}      | Delete a task              | Yes           |

## Testing
All endpoints were tested using Swagger UI and Postman. Screenshots of responses are included in the `/screenshots` folder.

## Author
Zeenat Mustafa