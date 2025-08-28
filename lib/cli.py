from helpers import (
    view_all_categories, add_category, view_all_items, add_item,
    create_shopping_list, view_shopping_lists, exit_program
)

def main():
    while True:
        print("\n📋 Shopping List CLI")
        print("1. View categories")
        print("2. Add category")
        print("3. View items")
        print("4. Add item")
        print("5. Create shopping list")
        print("6. View shopping lists")
        print("0. Exit")

        choice = input("> ")

        if choice == "1": view_all_categories()
        elif choice == "2": add_category()
        elif choice == "3": view_all_items()
        elif choice == "4": add_item()
        elif choice == "5": create_shopping_list()
        elif choice == "6": view_shopping_lists()
        elif choice == "0": exit_program()
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
