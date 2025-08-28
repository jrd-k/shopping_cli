from db.models import Session, Category, Item, ShoppingList

session = Session()

# Quick test
print(session.query(Category).all())
print(session.query(Item).all())
print(session.query(ShoppingList).all())
