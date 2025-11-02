from datetime import datetime
import time
import os
import sys
import csv
import json

Tasks_File = "tasks.csv"
Expenses_File = "expenses.csv"
Json_File = "notes.json"


def Add_Task():

    Tasks_Name = input("Enter the name of the task you want to add: ")
    Tasks_Due_date = input("Enter the due date of the task: ")
    while True:
        Tasks_Priority = input("Enter task priority (high, medium, low): ").lower()
        if Tasks_Priority in ["high", "medium", "low"]:
            break
        print("Invalid priority, try again.")
    while True:
        Tasks_Status = input(
            "Enter status (not started, in progress, completed): "
        ).lower()
        if Tasks_Status in ["not started", "in progress", "completed"]:
            break
        print("Invalid status, try again.")

    Exists_File = os.path.exists(Tasks_File)
    Fields = ["Task name", "Due date", "Priority", "Status"]

    with open(Tasks_File, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not Exists_File:
            writer.writerow(Fields)

        writer.writerow([Tasks_Name, Tasks_Due_date, Tasks_Priority, Tasks_Status])
    print(f"Task has been added ✅ {Tasks_Name} , {Tasks_Priority} , {Tasks_Status}")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def View_Tasks():
    if not os.path.exists(Tasks_File):
        print("There are no tasks recorded yet")
        input("\nPress Enter to return to menu...")
        return

    with open(Tasks_File, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        if not headers:
            print("⚠️ The tasks file is empty.")
            input("\nPress Enter to return to menu...")
            return

        print("|".join(headers))
        print("-" * 60)

        has_rows = False

        for row in reader:
            if any(row):  # Skip completely empty lines
                print(" | ".join(row))
                print("-" * 60)
                has_rows = True

        if not has_rows:
            print("⚠️ No task records found.")

        print("\n----------------------------------------")
        input("\nPress Enter to return to menu...")


def Add_Expense():
    Expenses_Name = input("Enter the name of the expense: ")
    while True:
        Expenses_Amount = input("Enter the amount of the expense: ")
        try:
            Expenses_Amount = float(Expenses_Amount)
            break
        except ValueError:
            print("Please enter a valid number for the amount.")

    Expenses_Category = input("Enter the category of the expense: ")
    Expenses_Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    Exists_File = os.path.exists(Expenses_File)
    Fields = ["Name", "Amount", "Category", "Date"]

    with open(Expenses_File, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if not Exists_File:
            writer.writerow(Fields)

        writer.writerow(
            [Expenses_Name, Expenses_Amount, Expenses_Category, Expenses_Date]
        )

        print(
            f"✅ Expense added: {Expenses_Name} - ${Expenses_Amount} ({Expenses_Category}) on {Expenses_Date}"
        )

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def View_Expenses():
    if not os.path.exists(Expenses_File):
        print("⚠️ There are no expenses recorded yet: ")
        input("\nPress Enter to return to menu...")
        return

    with open(Expenses_File, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        if not headers:
            print("⚠️ The expenses file is empty.")
            input("\nPress Enter to return to menu...")
            return
        print(" | ".join(headers))
        print("-" * 60)

        has_rows = False
        for row in reader:
            if any(row):  # Skip empty lines
                print(" | ".join(row))
                print("-" * 60)
                has_rows = True
        if not has_rows:
            print("⚠️ No expense records found.")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")



def Add_Note():
    user_note = input("Write your note: ")
    Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes = []

    if os.path.exists(Json_File):
        with open(Json_File, mode="r", encoding="utf-8") as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []

    # Add New Note

    notes.append({"Note": user_note, "Date": Date})

    # Save To Json File

    with open(Json_File, mode="w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

    print(f"📝 Note saved on {Date}")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def View_Notes():

    try:
        with open(Json_File, mode="r") as file:
            data = json.load(file)
            if not data:
                print("There are no notes yet 🗒️")
                return

            print("Your Notes:")
            print("--------------------------------")

            for note in data:

                print(f"🗒️ {note['Note']} (Added on: {note['Date']})")
            print("--------------------------------")

    except FileNotFoundError:
        print(f"Error: The file {Json_File} was not found.")
    except json.JSONDecodeError:
        print("Error: The notes file is empty or corrupted.")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def Search():
    category = input("Search in (tasks/expenses/notes): ").strip().lower()
    search_data = input("Enter keyword to search for: ").strip().lower()

    def search_csv(file_name, keyword):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                found = False
                for row in reader:
                    if any(keyword in str(value).lower() for value in row.values()):
                        print(
                            " | ".join(f"{key}: {value}" for key, value in row.items())
                        )
                        found = True
                if not found:
                    print("No matches found.")
        except FileNotFoundError:
            print(f"⚠️ No file found: {file_name}")

    def search_json(file_name, keyword):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                found = False
                for note in data:
                    if keyword in note["Note"].lower():
                        print(f"🗒️ {note['Note']} (Added on: {note['Date']})")
                        found = True
                if not found:
                    print("No matching notes found.")
        except FileNotFoundError:
            print(f"⚠️ No notes file found.")
        except json.JSONDecodeError:
            print("⚠️ Notes file is empty or corrupted.")

    # Handle categories
    if category == "tasks":
        search_csv(Tasks_File, search_data)
    elif category == "expenses":
        search_csv(Expenses_File, search_data)
    elif category == "notes":
        search_json(Json_File, search_data)
    else:
        print("Please type one of: tasks, expenses, or notes.")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def Export_Data():
    convert = input("Do you want to export your data? (yes/no): ").strip().lower()

    try:
        with open(Json_File, "r", encoding="utf-8") as file:
            notes = json.load(file)
    except json.JSONDecodeError:
        notes = []

    if convert == "yes":
        try:
            tasks = []
            expenses = []
            notes = []

            if os.path.exists(Tasks_File):
                with open(Tasks_File, "r", encoding="utf-8") as file:
                    tasks = list(csv.DictReader(file))

            if os.path.exists(Expenses_File):
                with open(Expenses_File, "r", encoding="utf-8") as file:
                    expenses = list(csv.DictReader(file))

            if os.path.exists(Json_File):
                with open(Json_File, "r", encoding="utf-8") as file:
                    notes = json.load(file)

            all_data = {
                "Tasks": tasks,
                "Expenses": expenses,
                "Notes": notes,
            }

            with open("backup.json", "w", encoding="utf-8") as file:
                json.dump(all_data, file, indent=4, ensure_ascii=False)

            print("✅ All data exported successfully to backup.json")
            time.sleep(1.5)

        except Exception as e:
            print(f"❌ Error exporting data: {e}")
    else:
        print("Export cancelled.")

    print("\n----------------------------------------")
    input("\nPress Enter to return to menu...")


def Exit():
    sys.exit("GoodBye👋")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    while True:
        clear_screen()

        print("==================================")
        print("    Personal Productivity System  ")
        print("==================================")
        print("")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Expense")
        print("4. View Expenses")
        print("5. Add Note")
        print("6. View Notes")
        print("7. Search")
        print("8. Export Data")
        print("9. Exit")
        print("")

        Choice = input("Please enter your choice: ")

        if Choice == "1":
            Add_Task()
        elif Choice == "2":
            View_Tasks()
        elif Choice == "3":
            Add_Expense()
        elif Choice == "4":
            View_Expenses()
        elif Choice == "5":
            Add_Note()
        elif Choice == "6":
            View_Notes()
        elif Choice == "7":
            Search()
        elif Choice == "8":
            Export_Data()
        elif Choice == "9":
            Exit()
        else:
            print("❌ Invalid choice. Please try again.")
            input("Press Enter to continue...")


menu()
