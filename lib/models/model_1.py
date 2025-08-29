# lib/models/model_1.py
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..helpers import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="category")

    def __repr__(self):
        return f"<Category(name={self.name})>"

class ShoppingList(Base):
    __tablename__ = "shopping_lists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String, default="pending")
    owner = Column(String)
    items = relationship("Item", back_populates="shopping_list")

    def __repr__(self):
        return f"<ShoppingList(name={self.name})>"

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, default=0)
    unit = Column(String)
    expiration_date = Column(Date)
    location = Column(String)
    note = Column(String)
    needed_quantity = Column(Float, default=1)
    category_id = Column(Integer, ForeignKey("categories.id"))
    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id"))

    category = relationship("Category", back_populates="items")
    shopping_list = relationship("ShoppingList", back_populates="items")

    def __repr__(self):
        return f"<Item(name={self.name}, quantity={self.quantity})>"

