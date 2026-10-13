from fastapi import FastAPI
from sqlalchemy import inspect, text

from app.database import Base, engine
from app.models.entities import Creature, Interaction, User

app = FastAPI(title="Lil_Guy")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Lil Guy API is running."}


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
