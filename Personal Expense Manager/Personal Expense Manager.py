from datetime import datetime
import os
import csv
import sys

file_name = "expenses.csv"


def Add_expense():
    print("")
    Item_Name = input("Enter Item Name: ")
    Amount = float(input("Enter Amount: "))
    Item_Category = input("Enter Item Category: ")
    date_created = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    file_exists = os.path.exists(file_name)
    fields = ["Name", "Amount", "Category", "Date Created"]

    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writter = csv.writer(file)
        if not file_exists:
            writter.writerow(fields)

        writter.writerow([Item_Name, Amount, Item_Category, date_created])

    print(
        f"✅ Expense added: {Item_Name} - ${Amount} ({Item_Category}) on {date_created}"
    )


def View_all_expenses():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("|".join(row))


def Show_total_spent():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return
    total = 0

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                total += float(row["Amount"])
            except (ValueError, KeyError):
                continue

        print(f"💰 Total spent: ${total:.2f}")


def View_expenses_by_category():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return

    category = input("Enter category to filter: ").strip().lower()
    Found = False

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Category"].strip().lower() == category:
                print(f"{row['Name']} - ${row['Amount']} ({row['Date Created']})")
                Found = True

    if not Found:
        print(f"❌ No expenses found in category '{category}'.")


def Show_monthly_total():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return

    month = input("Enter month (e.g. 10 for October): ").zfill(2)
    total = 0.0

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date = datetime.strptime(row["Date Created"], "%Y/%m/%d %H:%M:%S")
                if date.strftime("%m") == month:
                    total += float(row["Amount"])
            except Exception:
                continue
    print(f"📅 Total for month {month}: ${total:.2f}")


def Show_highest_lowest_expense():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return
    amounts = []

    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amounts.append(float(row["Amount"]))
            except (ValueError, KeyError):
                continue

    if amounts:
        print(f"💸 Highest expense: ${max(amounts):.2f}")
        print(f"🪙 Lowest expense:  ${min(amounts):.2f}")
    else:
        print("❌ No valid expenses found.")


def Edit_or_Delete():
    if not os.path.exists(file_name):
        print("⚠️ No expenses recorded yet.")
        return

    action = input("Do you want to 'edit' or 'delete' an expense? ").strip().lower()

    # Read all data
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("⚠️ No data found.")
        return

    name = input("Enter the item name: ").strip().lower()
    found = False

    if action == "delete":
        updated_expenses = [
            row for row in expenses if row["Name"].strip().lower() != name
        ]

        if len(updated_expenses) != len(expenses):
            with open(file_name, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Amount", "Category", "Date Created"]
                )
                writer.writeheader()
                writer.writerows(updated_expenses)
            print(f"🗑️ Item '{name}' deleted successfully.")
            found = True

    elif action == "edit":
        for row in expenses:
            if row["Name"].strip().lower() == name:
                found = True
                print(f"Editing {row['Name']} - ${row['Amount']} ({row['Category']})")

                new_name = input(
                    "Enter new name (press Enter to keep current): "
                ).strip()
                new_amount = input(
                    "Enter new amount (press Enter to keep current): "
                ).strip()
                new_category = input(
                    "Enter new category (press Enter to keep current): "
                ).strip()

                if new_name:
                    row["Name"] = new_name
                if new_amount:
                    try:
                        row["Amount"] = float(new_amount)
                    except ValueError:
                        print("⚠️ Invalid amount. Keeping old value.")
                if new_category:
                    row["Category"] = new_category

        if found:
            with open(file_name, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Amount", "Category", "Date Created"]
                )
                writer.writeheader()
                writer.writerows(expenses)
            print(f"✅ Item '{name}' updated successfully.")

    else:
        print("❌ Invalid action. Please type 'edit' or 'delete'.")

    if not found:
        print(f"❌ No expense found with name '{name}'.")


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("========================================")
    print("               Welcome                  ")
    print("========================================")
    print("")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total spent")
    print("4. View expenses by category")
    print("5. Show monthly total")
    print("6. Show highest and lowest expense")
    print("7. Edit or Delete Expense")
    print("8. Exit")

    Choice = input("Enter a choice: ")

    if Choice == "1":
        Add_expense()
    elif Choice == "2":
        View_all_expenses()
    elif Choice == "3":
        Show_total_spent()
    elif Choice == "4":
        View_expenses_by_category()
    elif Choice == "5":
        Show_monthly_total()
    elif Choice == "6":
        Show_highest_lowest_expense()
    elif Choice == "7":
        Edit_or_Delete()
    elif Choice == "8":
        sys.exit("GoodBye")
    else:
        print("❌ Invalid choice. Try again.")
    input("\nPress Enter to continue...")
