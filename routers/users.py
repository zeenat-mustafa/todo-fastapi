from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from models import UserCreate
import database
from auth import hash_password, verify_password, create_access_token

router = APIRouter(tags=["Auth"])


@router.post("/register")
def register(user: UserCreate):
    for existing_user in database.users:
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")

    new_user = {
        "username": user.username,
        "hashed_password": hash_password(user.password)
    }
    database.users.append(new_user)
    return {"message": "User registered successfully"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in database.users:
        if user["username"] == form_data.username:
            if verify_password(form_data.password, user["hashed_password"]):
                token = create_access_token(data={"sub": user["username"]})
                return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")