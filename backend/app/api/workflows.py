from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.workflow import Workflow
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowResponse
)

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"]
)


@router.post("/", response_model=WorkflowResponse)
def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):

    item = Workflow(
        project_id=workflow.project_id,
        workflow_name=workflow.workflow_name
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get("/")
def list_workflows(
    db: Session = Depends(get_db)
):
    return db.query(Workflow).all()