from pydantic import BaseModel


class WorkflowCreate(BaseModel):
    project_id: int
    workflow_name: str


class WorkflowResponse(BaseModel):
    id: int
    project_id: int
    workflow_name: str
    status: str

    model_config = {
        "from_attributes": True
    }