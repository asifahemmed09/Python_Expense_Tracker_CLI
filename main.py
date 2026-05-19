from datetime import date
from csv import DictWriter, DictReader
import os


def main():
    print("""
    -----------------------------
    |Expense Tracker Application|
    -----------------------------
    """)
    user_input()


def user_input():
    while True:
        choice = input(
            "Please select an option:\n"
            "1. Add an expense\n"
            "2. View all expenses\n"
            "3. View total expenses\n"
            "4. Exit\n> "
        )
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


def add_expense():
    category = input("Enter expense category: ").strip().lower()
    if not category:
        print("Category cannot be empty.\n")
        return
    
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    expense_date = date.today()
    expense = {"category": category, "amount": amount, "date": expense_date}

    file_exists = os.path.isfile("expenses.csv") and os.path.getsize("expenses.csv") > 0

    with open("expenses.csv", "a", newline="") as f:
        writer = DictWriter(f, fieldnames=["category", "amount", "date"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)

    print("Expense added successfully!\n")


def view_expenses():
    try:
        choice = int(
            input(
                "Please select an option:\n"
                "1. View all expenses\n"
                "2. View expenses for a specific category\n> "
            )
        )
    except ValueError:
        print("Invalid choice. Please try again.\n")
        return

    if choice == 1:
        try:
            with open("expenses.csv", "r") as f:
                reader = DictReader(f)
                rows = list(reader)
                if not rows:
                    print("No expenses found.\n")
                    return
                for row in rows:
                    print(
                        f"Category: {row['category']}\n"
                        f"Amount: {float(row['amount']):.2f}\n"
                        f"Date: {row['date']}\n"
                    )
        except FileNotFoundError:
            print("No expenses found.\n")

    elif choice == 2:
        category = input("Enter expense category: ").strip().lower()
        try:
            with open("expenses.csv", "r") as f:
                reader = DictReader(f)
                matched = [
                    row for row in reader
                    if row["category"].lower() == category
                ]

            if not matched:
                print(f"No expenses found for category '{category}'.\n")
            else:
                for row in matched:
                    print(
                        f"Category: {row['category']}\n"
                        f"Amount: {float(row['amount']):.2f}\n"
                        f"Date: {row['date']}\n"
                    )
        except FileNotFoundError:
            print("No expenses found.\n")

    else:
        print("Invalid choice. Please try again.\n")


def view_total_expenses():
  
    try:
        choice = int(
            input(
                "Please select an option:\n"
                "1. View total of all expenses\n"
                "2. View total for a specific category\n> "
            )
        )
    except ValueError:
        print("Invalid choice. Please try again.\n")
        return

    if choice == 1:
        try:
            with open("expenses.csv", "r") as f:
                reader = DictReader(f)
                rows = list(reader)
                if not rows:
                    print("No expenses found.\n")
                    return
                total = sum(float(row["amount"]) for row in rows)
                print(f"Total expenses: {total:.2f}\n")
        except FileNotFoundError:
            print("No expenses found.\n")

    elif choice == 2:
        category = input("Enter expense category: ").strip().lower()
        try:
            with open("expenses.csv", "r") as f:
                reader = DictReader(f)
                matched = [
                    row for row in reader
                    if row["category"].lower() == category
                ]
            if not matched:
                print(f"No expenses found for category '{category}'.\n")
            else:
                total = sum(float(row["amount"]) for row in matched)
                print(f"Total expenses for '{category}': {total:.2f}\n")
        except FileNotFoundError:
            print("No expenses found.\n")

    else:
        print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()