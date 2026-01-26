from sqlalchemy import Column, Integer, TIMESTAMP, Boolean, String
from db import Base


class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    is_recuring = Column(Boolean)
    interval = Column(String(45))
    max_retry_count = Column(Integer)
    created_time = Column(TIMESTAMP)
    