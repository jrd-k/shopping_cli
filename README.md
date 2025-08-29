#  Shopping List CLI (Phase 3 Project)

## Overview
This is a Python **Command Line Interface (CLI)** app for managing shopping categories, items, and shopping lists.  
It uses **SQLAlchemy ORM** with **SQLite** as the database and includes **Alembic migrations** for schema management.  
You can add/view categories, items, and create shopping lists right from the terminal.  

---

## 🚀 Features
- Add & view **categories**  
- Add & view **items** (with categories)  
- Create and view **shopping lists**  
- Database managed with **Alembic migrations**  
- Seed data using **Faker**  

---

## 🛠️ Tech Stack
- [Python 3.8+](https://www.python.org/) 🐍  
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)  
- [SQLite](https://www.sqlite.org/)  
- [Alembic](https://alembic.sqlalchemy.org/) (migrations)  
- [Faker](https://faker.readthedocs.io/) (seeding data)  

---

## 📂 Project Structure


shopping_cli/
│── lib/
│ ├── init.py
│ ├── cli.py # Main CLI logic
│ ├── debug.py # Debug helper
│ ├── helpers.py # DB session and utility functions
│ └── models/ # ORM models
│ ├── init.py
│ └── model_1.py # Category, Item, ShoppingList models
│
│── Pipfile # Dependencies
│── README.md # Documentation


---

##  Setup Instructions

###  Clone the repo
```bash
git clone git@github.com:jrd-k/shopping_cli.git
cd shopping_cli

 Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

 Install dependencies
pipenv install
pipenv shell

 Run Alembic migrations
alembic upgrade head

 Seed the database (optional)
python -m lib.debug

 Usage

Run the CLI:

python -m lib.cli

Example Flow:

Choose an option from the menu (e.g., add category, add item, view shopping lists).

Enter details when prompted (e.g., category name, item name).

See results printed in the terminal.

Example:

Welcome to Shopping CLI!  
1. Add Category  
2. View Categories  
3. Add Item  
4. View Items  
5. Create Shopping List  
6. View Shopping Lists  
Enter choice: 1  

Enter category name: Groceries  
 Category 'Groceries' added!

 Testing / Debugging

To explore the database interactively:

python -m lib.debug


You’ll get a Python shell with models and session preloaded.

 License

This project is for educational purposes.