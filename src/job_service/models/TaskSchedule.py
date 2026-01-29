from sqlalchemy import Column, Integer
from db import Base

class TaskSchedule(Base):
    __tablename__ = "task_schedule"
    next_execution_time = Column(Integer)
    job_id = Column(Integer)
    