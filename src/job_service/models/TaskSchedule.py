from sqlalchemy import Column, Integer
from db import Base
from pydantic import BaseModel 

class TaskScheduleRequest(BaseModel): 
    next_execution_time: int 
    job_id: int
    script: str

class TaskSchedule(Base):
    __tablename__ = "task_schedule"
    next_execution_time = Column(Integer, primary_key=True)
    job_id = Column(Integer, primary_key=True)
    