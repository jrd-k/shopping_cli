  Shopping List CLI (Phase 3 Project)
  Overview

A Python Command Line Interface (CLI) app for managing shopping categories, items, and shopping lists using SQLAlchemy ORM and SQLite.

This project demonstrates:

Python OOP design

ORM models with relationships

CLI-based CRUD operations

 Features

 Add & view categories

 Add & view items (with category support)

 Create shopping lists

 View shopping lists with item counts and status

 Data stored persistently in SQLite

 Tech Stack

Python 3.8+

SQLAlchemy ORM

SQLite (local DB)

Faker (for seeding demo data)

Setup
1. Clone the repo
git clone git@github.com:jrd-k/shopping_cli.git
cd shopping_cli

2. Install dependencies

Using Pipenv:

pipenv install sqlalchemy alembic faker ipython
pipenv shell


Or using venv + pip:

python3 -m venv venv
source venv/bin/activate
pip install sqlalchemy alembic faker ipython

Usage
1. Initialize the database
python -m lib.seed

2. Run the CLI
python -m lib.debug


You will see a CLI menu to manage categories, items, and shopping lists.

 Project Structure
 shopping_cli
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py

 Example CLI Flow
Welcome to Shopping List CLI!
1. View Categories
2. Add Category
3. View Items
4. Add Item
5. Create Shopping List
6. View Shopping Lists
7. Exit

 License

This project is licensed under the MIT License.