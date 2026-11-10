from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.dependencies import get_current_user
from app.models.entities import User

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

@router.post("/", response_model=CreatureResponse, status_code=status.HTTP_201_CREATED)
def create_creature(
    creature_data: CreatureCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check whether the user already has a creature
    existing_creature = db.scalar(
        select(Creature).where(Creature.owner_id == current_user.id)
    )

    if existing_creature:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You already have a Lil_Guy",
        )

    # Create the creature
    new_creature = Creature(
        name=creature_data.name,
        personality=creature_data.personality,
        owner_id=current_user.id,
    )

    db.add(new_creature)
    db.commit()
    db.refresh(new_creature)

    return new_creature

@router.get("/", response_model=CreatureResponse)
def get_creature(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    creature = db.scalar(
        select(Creature).where(Creature.owner_id == current_user.id)
    )

    if creature is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You don't have a Lil_Guy yet",
        )

    return creature