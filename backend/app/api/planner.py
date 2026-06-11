from fastapi import APIRouter

from app.agents.planner_agent import planner_agent

router = APIRouter(
    prefix="/planner",
    tags=["Planner"]
)

@router.get("/cad")
def create_cad_plan():

    return planner_agent.generate_cad_tasks()