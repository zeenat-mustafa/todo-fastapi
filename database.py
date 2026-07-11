# In-memory "database"

todos = []       # will hold dicts like {"id": 1, "title": "...", "completed": False}
users = []       # will hold dicts like {"username": "...", "hashed_password": "..."}

# Simple counter to auto-generate unique todo IDs
todo_id_counter = 1