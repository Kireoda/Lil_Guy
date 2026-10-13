from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import Interaction
from app.schemas import InteractionResponse


router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)
