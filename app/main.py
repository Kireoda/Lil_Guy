
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import inspect, text, select
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models.entities import Creature, Interaction, User
from app.routes import users, creatures, interactions
import os
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
from app.dependencies import get_current_user

load_dotenv()

app = FastAPI(title="Lil_Guy")

session_secret = os.getenv("SESSION_SECRET")

if not session_secret:
    raise RuntimeError("SESSION_SECRET is missing from environment variables.")

app.add_middleware(
    SessionMiddleware,
    secret_key=session_secret,
    session_cookie="lil_guy_session",
    max_age=60 * 60 * 24,
    same_site="lax",
    https_only=os.getenv("ENVIRONMENT") == "production",
)

# Create DT tables
Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

templates = Jinja2Templates(directory="app/templates")

app.include_router(users.router)
app.include_router(creatures.router)
app.include_router(interactions.router)


# Landing page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )

@app.get("/dashboard")
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    creature = db.scalar(
        select(Creature).where(Creature.owner_id == current_user.id)
    )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "current_user": current_user,
            "creature": creature,
        },
    )

# Interaction history page
@app.get("/interactions")
def interactions_page(
    request: Request,
    current_user: User = Depends(get_current_user),
):
    return templates.TemplateResponse(
        request=request,
        name="interactions.html",
        context={"current_user": current_user},
    )

# Settings page
@app.get("/settings")
def settings_page(
    request: Request,
    current_user: User = Depends(get_current_user),
):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={"current_user": current_user},
    )

# Database health check
@app.get("/health/database")
def check_database():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    tables = inspect(engine).get_table_names()

    return {
        "status": "healthy",
        "database": "connected",
        "tables": tables,
    }

# Login page
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={},
    )


# Registration page
@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={},
    )