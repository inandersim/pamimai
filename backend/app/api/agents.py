from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.agent import Agent

from app.schemas.agent import (
    AgentCreate,
    AgentResponse
)

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.post("/", response_model=AgentResponse)
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):

    new_agent = Agent(
        name=agent.name,
        agent_type=agent.agent_type
    )

    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)

    return new_agent


@router.get("/")
def list_agents(
    db: Session = Depends(get_db)
):
    return db.query(Agent).all()