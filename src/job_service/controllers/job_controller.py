from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.TaskHistory import TaskHistory, TaskHistoryRequest
from models.TaskSchedule import TaskScheduleRequest, TaskSchedule

router = APIRouter()

@router.get("/task/history/{job_id}")
async def get_task_history(job_id: int, db: Session = Depends(get_db)):
    result = db.query(TaskHistory).filter(TaskHistory.job_id == job_id).first()

    if not result:
        raise HTTPException(status_code=404, detail="Job with this id not found")
    
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