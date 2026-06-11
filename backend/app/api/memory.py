from fastapi import APIRouter
from fastapi import Depends
from app.models.memory import Memory
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.memory import Memory

from app.schemas.memory import (
    MemoryCreate,
    MemoryResponse
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.post("/", response_model=MemoryResponse)
def create_memory(
    memory: MemoryCreate,
    db: Session = Depends(get_db)
):

    item = Memory(
        project_id=memory.project_id,
        memory_type=memory.memory_type,
        content=memory.content
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get("/{project_id}")
def get_project_memory(
    project_id: int,
    db: Session = Depends(get_db)
):

    return (
        db.query(Memory)
        .filter(Memory.project_id == project_id)
        .all()
    )