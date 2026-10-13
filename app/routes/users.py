from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import User
from app.schemas import UserCreate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)