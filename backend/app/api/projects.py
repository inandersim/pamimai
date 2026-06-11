from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends

from app.models.project import Project
from app.database.database import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):

    new_project = Project(
        name=project.name,
        project_type=project.project_type
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/")
def list_projects(
    db: Session = Depends(get_db)
):

    projects = db.query(Project).all()

    return projects