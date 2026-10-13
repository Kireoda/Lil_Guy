
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import inspect, text

from app.database import Base, engine
from app.models.entities import Creature, Interaction, User
from app.routes import users, creatures, interactions

app = FastAPI(title="Lil_Guy")

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

# Dashboard page
@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={},
    )

# Interaction history page
@app.get("/interactions")
def interactions_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="interactions.html",
        context={},
    )

# Settings page
@app.get("/settings")
def settings_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={},
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
