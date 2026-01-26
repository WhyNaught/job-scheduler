from sqlalchemy import Column, Integer, TIMESTAMP, Boolean 
from db import Base

class TaskSchedule(Base):
    __tablename__ = "task_schedule"
    next_execution_time = Column(TIMESTAMP, primary_key=True)
    job_id = Column(Integer)
    