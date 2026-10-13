
from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    creature: Mapped[Creature | None] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )


class Creature(Base):
    __tablename__ = "creatures"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(30), nullable=False, default="Lil_Guy"
    )
    personality: Mapped[str] = mapped_column(
        String(30), nullable=False, default="Curious"
    )
    current_mood: Mapped[str] = mapped_column(
        String(20), nullable=False, default="neutral"
    )
    is_sleeping: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    owner: Mapped[User] = relationship(
        back_populates="creature"
    )
    interactions: Mapped[list[Interaction]] = relationship(
        back_populates="creature",
        cascade="all, delete-orphan",
    )


class Interaction(Base):
    __tablename__ = "interactions"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    event_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )
    mood: Mapped[str] = mapped_column(
        String(20), nullable=False
    )
    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    creature_id: Mapped[int] = mapped_column(
        ForeignKey("creatures.id"),
        nullable=False,
        index=True,
    )

    creature: Mapped[Creature] = relationship(
        back_populates="interactions"
    )
