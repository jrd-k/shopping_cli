# lib/cli.py
from .helpers import SessionLocal
from .models.model_1 import Category, Item, ShoppingList

session = SessionLocal()

def view_all_categories():
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
    for c in categories:
        print(f"{c.id}. {c.name} - {c.description}")

def add_category():
    name = input("Enter category name: ")
    desc = input("Enter description: ")
    c = Category(name=name, description=desc)
    session.add(c)
    session.commit()
    print(f"Category '{name}' added!")

def view_all_items():
    items = session.query(Item).all()
    if not items:
        print("No items found.")
    for i in items:
        print(f"{i.id}. {i.name} ({i.quantity} {i.unit or ''}) - Category: {i.category.name if i.category else 'None'}")

def add_item():
    name = input("Item name: ")
    qty = float(input("Quantity: "))
    unit = input("Unit: ")
    view_all_categories()
    cat_id = int(input("Category ID: "))
    category = session.query(Category).get(cat_id)
    if not category:
        print("Invalid category ID")
        return
    item = Item(name=name, quantity=qty, unit=unit, category=category)
    session.add(item)
    session.commit()
    print(f"Item '{name}' added!")

def create_shopping_list():
    name = input("Shopping list name: ")
    owner = input("Owner name: ")
    sl = ShoppingList(name=name, owner=owner)
    session.add(sl)
    session.commit()
    print(f"Shopping list '{name}' created!")

def view_shopping_lists():
    lists = session.query(ShoppingList).all()
    if not lists:
        print("No shopping lists.")
    for sl in lists:
        print(f"{sl.id}. {sl.name} ({len(sl.items)} items) - Status: {sl.status}")

def exit_program():
    print("Goodbye!")
    exit()

def main_menu():
    while True:
        print("\nSmart Pantry Manager CLI")
        print("1. View Categories")
        print("2. Add Category")
        print("3. View Items")
        print("4. Add Item")
        print("5. View Shopping Lists")
        print("6. Create Shopping List")
        print("7. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            view_all_categories()
        elif choice == "2":
            add_category()
        elif choice == "3":
            view_all_items()
        elif choice == "4":
            add_item()
        elif choice == "5":
            view_shopping_lists()
        elif choice == "6":
            create_shopping_list()
        elif choice == "7":
            exit_program()
        else:
            print("Invalid choice, please try again.")
