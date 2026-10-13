from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

# User schemas
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=12, max_length=128)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    created_at: datetime


# Creature schemas
Personality = Literal["Curious", "Grumpy", "Affectionate"]


class CreatureCreate(BaseModel):
    name: str = Field(default="Lil_Guy", min_length=1, max_length=30)
    personality: Personality = "Curious"


class CreatureUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=30)
    personality: Personality | None = None


class CreatureResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    personality: Personality
    current_mood: str
    is_sleeping: bool
    created_at: datetime


# Interaction schemas

class InteractionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    event_type: str
    mood: str
    occurred_at: datetime
