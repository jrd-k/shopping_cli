# lib/debug.py
from .helpers import init_db, SessionLocal
from .models.model_1 import Category, Item, ShoppingList
from .cli import main_menu

def run_debug():
    init_db()  # Create tables
    session = SessionLocal()

    # Quick test
    print("Categories:", session.query(Category).all())
    print("Items:", session.query(Item).all())
    print("Shopping Lists:", session.query(ShoppingList).all())

    # Launch CLI
    main_menu()

if __name__ == "__main__":
    run_debug()
