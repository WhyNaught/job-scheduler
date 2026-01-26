from sqlalchemy.orm import Session
from src.models.User import User

from typing import List 

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.user_id == user_id).first()

def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()

def create_user(db: Session, username: str, user_email: str) -> User:
    new_user = User(username=username, user_email=user_email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
