from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User
from services import user_service

router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users():
    return user_service.get_all_users()


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/usersbyage/{age}", response_model=User)
def get_user(age: int):
    user = user_service.get_userbyage(age)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    return user_service.update_user(user_id, user)


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}
