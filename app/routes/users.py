
from fastapi import APIRouter, Depends, HTTPException, status, Request
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.entities import User
from app.schemas import UserCreate, UserLogin, UserResponse
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

password_hash = PasswordHash.recommended()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    # Check whether the username already exists
    existing_user = db.scalar(
        select(User).where(User.username == user_data.username)
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )

    # Hash the password
    hashed_password = password_hash.hash(user_data.password)

    # Create the user
    new_user = User(
        username=user_data.username,
        password_hash=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=UserResponse)
def login_user(
    user_data: UserLogin,
    request: Request,
    db: Session = Depends(get_db),
):
    # Find the user
    user = db.scalar(
        select(User).where(User.username == user_data.username)
    )

    # Verify username and password
    if user is None or not password_hash.verify(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    # Clear any previous session
    request.session.clear()

    # Store the authenticated user's ID
    request.session["user_id"] = user.id

    return user

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user

@router.post("/logout")
def logout_user(request: Request):
    request.session.clear()

    return {
        "message": "Successfully logged out"
    }