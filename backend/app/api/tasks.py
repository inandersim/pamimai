from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.task import Task
from app.schemas.task import (
    TaskCreate,
    TaskResponse
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):

    item = Task(
        workflow_id=task.workflow_id,
        task_name=task.task_name,
        assigned_agent=task.assigned_agent
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get("/")
def list_tasks(
    db: Session = Depends(get_db)
):
    return db.query(Task).all()