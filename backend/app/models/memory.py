from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Memory(Base):

    __tablename__ = "memories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )

    memory_type: Mapped[str] = mapped_column(
        String(100)
    )

    content: Mapped[str] = mapped_column(
        Text()
    )