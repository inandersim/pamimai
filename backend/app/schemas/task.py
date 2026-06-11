from pydantic import BaseModel


class TaskCreate(BaseModel):
    workflow_id: int
    task_name: str
    assigned_agent: str


class TaskResponse(BaseModel):
    id: int
    workflow_id: int
    task_name: str
    assigned_agent: str
    status: str

    model_config = {
        "from_attributes": True
    }