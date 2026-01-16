from datetime import date

today = date.today()

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

birthday = date(year, month, day)

age = today.year - birthday.year

if (today.month, today.day) < (birthday.month, birthday.day):
    age -= 1

print(f"your age is {age} years old")
