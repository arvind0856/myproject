from fastapi import FastAPI
from .database import engine, Base
from app.routers import user

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI SQLAlchemy CRUD API",
    description="Production-ready CRUD API using FastAPI + SQLAlchemy + SQLite",
    version="1.0.0",
)

# Include routers
app.include_router(user.router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI SQLAlchemy CRUD API is running successfully"}
