from sqlalchemy import Column, Integer, String 
from db import Base

from pydantic import BaseModel 

class TaskHistoryRequest(BaseModel):
    job_id: int 
    execution_time: int 
    status: str 
    retry_count: int
    last_update_time: int 

class TaskHistory(Base):
    __tablename__ = "task_history"
    job_id = Column(Integer, primary_key=True, index=True)
    execution_time = Column(Integer)
    status = Column(String)
    retry_count = Column(Integer)
    last_update_time = Column(Integer)
