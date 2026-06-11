from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine
from app.models.memory import Memory

from app.api.projects import router as project_router
from app.api.memory import router as memory_router
from app.models.agent import Agent
from app.api.agents import router as agent_router
from app.models.workflow import Workflow
from app.models.task import Task

from app.api.workflows import router as workflow_router
from app.api.tasks import router as task_router
from app.api.planner import router as planner_router




Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PamiMai",
    version="0.2.0"
)

app.include_router(project_router)
app.include_router(memory_router)
app.include_router(agent_router)
app.include_router(workflow_router)
app.include_router(task_router)
app.include_router(planner_router)


@app.get("/")
def root():
    return {
        "name": "PamiMai",
        "version": "0.2.0",
        "status": "running"
    }