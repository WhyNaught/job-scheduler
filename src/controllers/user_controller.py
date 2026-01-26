from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service import get_user, create_user, get_all_users
from db import get_db
from models.User import UserRequest

router = APIRouter()


@router.get("/users")
async def fetch_all_users(db: Session = Depends(get_db)):
    return get_all_users(db=db)


@router.post("/users")
async def create_new_user(new_user: UserRequest, db: Session = Depends(get_db)):
    return create_user(user_email=new_user.user_email, username=new_user.username, db=db)


@router.get("/users/{user_id}")
async def fetch_user_by_id(user_id: int, db: Session = Depends(get_db)):
    fetched_user = get_user(user_id=user_id, db=db)

    if not fetched_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    return fetched_user
