from pydantic import BaseModel
from typing import Optional


# ---------- TODO MODELS ----------

# Used when CREATING a todo (user doesn't send id, we generate it)
class TodoCreate(BaseModel):
    title: str
    completed: bool = False

# Used when UPDATING a todo (all fields optional, user may update just one)
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

# Full Todo object (used for responses, includes id)
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# ---------- USER MODELS (for auth, used in Chunk 3) ----------

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserInDB(BaseModel):
    username: str
    hashed_password: str