from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Association table (many-to-many)
shopping_list_items = Table(
    "shopping_list_items",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("shopping_list_id", Integer, ForeignKey("shopping_lists.id")),
    Column("item_id", Integer, ForeignKey("items.id"))
)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, default="")
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    unit = Column(String)
    expiration_date = Column(Date)
    location = Column(String)
    note = Column(String)
    needed_quantity = Column(Integer, default=1)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="items")
    shopping_lists = relationship("ShoppingList", secondary=shopping_list_items, back_populates="items")

    def __repr__(self):
        return f"<Item {self.name} ({self.quantity}{self.unit or ''})>"

class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String, default="pending")
    owner = Column(String, default="Anonymous")
    total = Column(Float, default=0.0)

    items = relationship("Item", secondary=shopping_list_items, back_populates="shopping_lists")

    def __repr__(self):
        return f"<ShoppingList {self.name} ({len(self.items)} items)>"

# --- Database setup ---
engine = create_engine("sqlite:///shopping.db")
Session = sessionmaker(bind=engine)
