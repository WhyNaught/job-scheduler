from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.TaskHistory import TaskHistory

router = APIRouter()

@router.get("/task/history/{job_id}")
async def get_task_history(job_id: int, db: Session = Depends(get_db)):
    result = db.query(TaskHistory).filter(TaskHistory.job_id == job_id).first()

    if not result:
        raise HTTPException(status_code=404, detail="Job with this id not found")
    
    return result 

@router.post("/task/history/")
async def upload_task_history(task_history: TaskHistory, db: Session = Depends(get_db)): 
    db.add(task_history)
    db.commit()
    db.refresh(task_history)
    return task_history
