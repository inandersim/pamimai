from pydantic import BaseModel
from app.models.memory import Memory

class MemoryCreate(BaseModel):

    project_id: int
    memory_type: str
    content: str


class MemoryResponse(BaseModel):

    id: int
    project_id: int
    memory_type: str
    content: str

    model_config = {
        "from_attributes": True
    }