# from sqlalchemy import Uuid
from sqlalchemy.orm import deferred
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

# import uuid


class User(db.Model):
    __tablename__ = "users"
    # id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(
        db.String(255), nullable=False, unique=True, index=True
    )
    password_hash: Mapped[str] = deferred(
        mapped_column(db.String(255), nullable=False)
    )  # deferred means that it will not be loaded from the database
    role: Mapped[str] = mapped_column(db.String(10), nullable=False, default="user")
    is_active: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=True)

    # Set automatically on creation
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # Set automatically on creation and updated on every modification
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
