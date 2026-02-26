from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.TaskHistory import TaskHistory, TaskHistoryRequest
from models.TaskSchedule import TaskScheduleRequest, TaskSchedule
from models.Job import Job

router = APIRouter()

@router.get("/task/history/{job_id}")
async def get_task_history(job_id: int, db: Session = Depends(get_db)):
    result = db.query(TaskHistory).filter(TaskHistory.job_id == job_id).all()

    if not result or len(result) == 0:
        raise HTTPException(status_code=404, detail="Histories with this id not found")
    
    return result 

@router.post("/task/history/")
async def upload_task_history(task_history: TaskHistoryRequest, db: Session = Depends(get_db)): 
    new_task_history = TaskHistory(
        job_id=task_history.job_id, 
        execution_time=task_history.execution_time, 
        status=task_history.status, 
        retry_count=task_history.retry_count, 
        last_update_time=task_history.last_update_time, 
    )

    db.add(new_task_history)
    db.commit()
    db.refresh(new_task_history)
    return new_task_history

@router.post("/task/schedule")
async def schedule_task(task_schedule: TaskScheduleRequest, db: Session = Depends(get_db)):
    new_task_schedule = TaskSchedule(
        job_id=task_schedule.job_id, 
        next_execution_time=task_schedule.next_execution_time
    )

    db.add(new_task_schedule)
    db.commit()
    db.refresh(new_task_schedule)
    return new_task_schedule

@router.get("/tasks/{user_id}")
async def get_all_user_tasks(user_id: int, db: Session = Depends(get_db)):
    fetched_tasks = db.query(Job).filter(Job.user_id == user_id).all()

    return fetched_tasks

@router.get("/tasks/scripts/{job_id}")
async def get_job_script(job_id: int):
    try:
        with open(f"/app/scripts/{job_id}.py", "r") as script:
            content = script.read()
    except FileNotFoundError:
        print(f"No script found for job_id: {job_id}")

    return content 