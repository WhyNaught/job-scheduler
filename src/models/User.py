from sqlalchemy import Column, Integer, String
from db import Base

from pydantic import BaseModel 

class UserRequest(BaseModel):
    username: str 
    user_email: str 

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), index=True)
    user_email = Column(String(45), index=True)
