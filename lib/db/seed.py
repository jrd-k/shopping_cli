from faker import Faker
from datetime import datetime, timedelta
from .models import Base, engine, Session, Category, Item, ShoppingList

fake = Faker()
session = Session()

def seed():
    print("🌱 Seeding database...")

    # Drop and recreate tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Create categories
    categories = [
        Category(name="Groceries", description="Daily essentials"),
        Category(name="Household", description="Cleaning & home supplies"),
        Category(name="Electronics", description="Gadgets & appliances")
    ]
    session.add_all(categories)
    session.commit()

    # Create items
    items = []
    for _ in range(10):
        item = Item(
            name=fake.word(),
            quantity=fake.random_int(min=1, max=10),
            unit="pcs",
            expiration_date=fake.date_between(start_date="today", end_date="+30d"),
            location=fake.word(),
            note=fake.sentence(),
            category=fake.random_element(categories)
        )
        items.append(item)
    session.add_all(items)
    session.commit()

    # Create shopping list
    sl = ShoppingList(name="Weekly Shopping", owner="Admin")
    sl.items.extend(items[:5])
    session.add(sl)
    session.commit()

    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed()

