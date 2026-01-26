from sqlalchemy import Column, Integer, TIMESTAMP, Boolean 
from db import Base


class TaskHistory(Base):
    __tablename__ = "task_history"
    job_id = Column(Integer, primary_key=True, index=True)
    execution_time = Column(TIMESTAMP)
    status = Column(Boolean)
    retry_count = Column(Integer)
    last_update_time = Column(TIMESTAMP)
