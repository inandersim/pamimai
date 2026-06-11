from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Task(Base):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    workflow_id: Mapped[int] = mapped_column(
        ForeignKey("workflows.id")
    )

    task_name: Mapped[str] = mapped_column(
        String(255)
    )

    assigned_agent: Mapped[str] = mapped_column(
        String(100)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )