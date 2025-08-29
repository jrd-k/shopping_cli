# lib/helpers.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///pantry.db"

# Engine
engine = create_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Base class
Base = declarative_base()

# Initialize DB (create tables)
def init_db():
    # Import models here to avoid circular import
    from .models.model_1 import Category, Item, ShoppingList
    Base.metadata.create_all(bind=engine)
