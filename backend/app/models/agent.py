from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Agent(Base):

    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    agent_type: Mapped[str] = mapped_column(
        String(100)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active"
    )