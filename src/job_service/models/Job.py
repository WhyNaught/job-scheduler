from sqlalchemy import Column, Integer, TIMESTAMP, Boolean, String
from db import Base
from pydantic import BaseModel 

class JobPostRequest(BaseModel):
    is_recurring: bool 
    max_retry_count: int 
    interval: str 

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    is_recurring = Column(Boolean)
    interval = Column(String(45))
    max_retry_count = Column(Integer)
    created_time = Column(TIMESTAMP)
    