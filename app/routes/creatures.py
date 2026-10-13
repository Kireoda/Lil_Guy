from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import Creature
from app.schemas import (
    CreatureCreate,
    CreatureUpdate,
    CreatureResponse,
)


router = APIRouter(
    prefix="/creatures",
    tags=["Creatures"],
)
