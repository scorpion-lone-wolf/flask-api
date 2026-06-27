# from sqlalchemy import Uuid
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column

# import uuid


class User(db.Model):
    __tablename__ = "users"
    # id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(
        db.String(255), nullable=False, unique=True, index=True
    )
