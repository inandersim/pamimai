from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Workflow(Base):

    __tablename__ = "workflows"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )

    workflow_name: Mapped[str] = mapped_column(
        String(255)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )