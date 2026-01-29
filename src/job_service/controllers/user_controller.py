from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service import get_user, create_user, get_all_users
from db import get_db
from models.User import UserRequest
from models.Job import JobPostRequest, Job
from models.TaskSchedule import TaskSchedule

from datetime import datetime

import isodate

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

@router.post("/users/{user_id}")
async def add_job(user_id: int, job_request: JobPostRequest, db: Session = Depends(get_db)):
    now_dt = datetime.now().replace(second=0, microsecond=0)
    created_time = now_dt.timestamp()

    fetched_user = get_user(user_id=user_id, db=db)
    if not fetched_user:
        raise HTTPException(status_code=404, detail="user with this id not found")

    new_job = Job(
        user_id=user_id,
        is_recurring=job_request.is_recurring, 
        interval=job_request.interval, 
        max_retry_count=job_request.max_retry_count,
        created_time=int(created_time)
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    duration = isodate.parse_duration(job_request.interval)
    next_exec_time = (now_dt + duration).timestamp()
    task_schedule = TaskSchedule(
        next_execution_time=int(next_exec_time), 
        job_id=new_job.job_id
    )
    db.add(task_schedule)
    db.commit()
    db.refresh(task_schedule)
    return new_job
