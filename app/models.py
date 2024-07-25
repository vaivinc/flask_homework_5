from db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    ingredients: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)


    def __str__(self):
        return f"{self.name}"