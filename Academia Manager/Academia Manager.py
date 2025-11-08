from datetime import datetime
import time
import os
import csv


Students_Fields = ["ID", "Name", "Age", "Grade", "Subjects", "Registration date"]
Student_File = "students.csv"


class Students:

    def Add_Students(self):
        while True:
            Student_Id = input("Please enter your Student ID: ")
            try:
                Student_Id = int(Student_Id)
                break
            except ValueError:
                print("Please enter a valid number for the ID.")

        Student_Name = input("Please enter the student’s name: ")

        while True:
            Student_Age = input("Please enter the student’s age: ")

            try:
                Student_Age = int(Student_Age)
                break
            except ValueError:
                print("Please enter a valid number for the age.")
        while True:

            Student_Grade = input("Please enter the student’s grade: ")
            try:
                Student_Grade = float(Student_Grade)
                break
            except ValueError:
                print("Please enter a valid number for the grade.")

        Student_Subject = input("Please enter the student’s subject: ")
        Registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Exists_File = os.path.exists(Student_File)

        with open(Student_File, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            if not Exists_File:
                writer.writerow(Students_Fields)
            writer.writerow(
                [
                    Student_Id,
                    Student_Name,
                    Student_Age,
                    Student_Grade,
                    Student_Subject,
                    Registration_date,
                ]
            )

    def View_Students(self):
        if not os.path.exists(Student_File):
            print("No student records found yet.")
            return

        with open(Student_File, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if not headers:
                print("the file is empty")
                return

            print("|".join(headers))
            print("-" * 60)
            has_row = False
            for row in reader:
                if any(row):
                    print("|".join(row))
                    print("-" * 60)
                    has_row = True
            if not has_row:
                print("No Data Found ")

    def Update_Information(self):

        actions = (
            input("Do you want to update student information? (yes/no): ")
            .strip()
            .lower()
        )

        if actions != "yes":
            print("Update canceled.")
            return

        old_id = input("Enter the ID of the student to update: ")
        updated_rows = []
        found = False
        with open(Student_File, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            updated_rows.append(header)

            for row in reader:
                if row[0] == old_id:
                    print("Student found. Enter new information:")
                    new_name = input(f"New Name ({row[1]}) To : ") or row[1]
                    while True:
                        new_age = input(f"New Age ({row[2]}) To : ") or row[2]
                        try:
                            new_age = int(new_age)
                            break
                        except ValueError:
                            print("Please enter a valid number for the age.")
                    while True:
                        new_grade = input(f"New Grade ({row[3]}) To : ") or row[3]
                        try:
                            new_grade = float(new_grade)
                            break
                        except ValueError:
                            print("Please enter a valid number for the grade.")
                    new_subject = input(f"New Subject ({row[4]}) To : ") or row[4]
                    row = [old_id, new_name, new_age, new_grade, new_subject, row[5]]
                    found = True
                updated_rows.append(row)
        if not found:
            print("❌ No student found with that ID.")
            return

        with open(Student_File, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("✅ Student information updated successfully!")

    def Search_Student_by_ID(self):
        search_action = input("Enter the ID you want to search: ")

        with open(Student_File, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if not headers:
                print("the file is empty")
                return
            has_row = False
            for row in reader:
                if row[0] == search_action:
                    print("|".join(headers))
                    print("-" * 60)
                    print("|".join(row))
                    print("-" * 60)
                    has_row = True

            if not has_row:
                print("❌ No student found with that ID. ")

    def Remove_Student(self):

        remove_item = input("Enter the Student ID you want to remove: ")

        if not os.path.exists(Student_File):
            print("No student records found yet.")
            return

        updated_rows = []
        found = False

        with open(Student_File, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            updated_rows.append(headers)

            for row in reader:
                if row[0] == remove_item:
                    found = True
                    print(f"🗑️ Student with ID {remove_item} removed.")
                else:
                    updated_rows.append(row)

        if not found:
            print("❌ No student found with that ID.")
            return

        with open(Student_File, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

    def Display_Statistics(self):
        if not os.path.exists(Student_File):
            print("⚠️ No student records found yet.")
            return

        total_student = 0
        total_grade = 0
        highest_grade = None
        lowest_grade = None
        subjects_count = {}

        with open(Student_File, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_student += 1

                # Grade statistics

                try:
                    grade = float(row["Grade"])
                    total_grade += grade
                    if highest_grade is None or grade > highest_grade:
                        highest_grade = grade
                    if lowest_grade is None or grade < lowest_grade:
                        lowest_grade = grade

                except:
                    continue

                # Subject statistics

                subject = row["Subjects"]
                subjects_count[subject] = subjects_count.get(subject, 0) + 1

        if total_student == 0:
            print("No student data available.")
            return

        average_grade = total_grade / total_student

        print("📊 Student Statistics")
        print(f"Total students: {total_student}")
        print(f"Average grade: {average_grade:.2f}")
        print(f"Highest grade: {highest_grade}")
        print(f"Lowest grade: {lowest_grade}")
        print("Students per subject:")
        for subject, count in sorted(
            subjects_count.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {subject}: {count}")

    def Exit(self):
        exit("Goodbye👋")


def menu(students):
    os.system("cls" if os.name == "nt" else "clear")

    print("--------------------------------")
    print("    Student Management System   ")
    print("--------------------------------")
    print("1. Add new students")
    print("2. View all students")
    print("3. Update a student’s information")
    print("4. Search for a student by ID")
    print("5. Remove a student")
    print("6. Display statistics")
    print("7. Exit")

    Choice = input("Enter your choice: ")

    if Choice == "1":
        students.Add_Students()
    elif Choice == "2":
        students.View_Students()
    elif Choice == "3":
        students.Update_Information()
    elif Choice == "4":
        students.Search_Student_by_ID()
    elif Choice == "5":
        students.Remove_Student()
    elif Choice == "6":
        students.Display_Statistics()
    elif Choice == "7":
        students.Exit()
    else:
        print("❌ Invalid choice. Please try again.")


students = Students()

while True:
    menu(students)
    time.sleep(0.5)
    again = input("\nPress Enter to return to menu...").lower()
