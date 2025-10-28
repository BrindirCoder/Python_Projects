from datetime import datetime
from cryptography.fernet import Fernet
import csv
import string
import random
import os


file_name = "password.csv"

if not os.path.exists("key.key"):
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("key.key", "rb") as key_file:
    encryption_key = key_file.read()

encryption_proccess = Fernet(encryption_key)

print("1. Add new password")
print("2. View all passwords")
print("3. Search password")

print("")

Choice = input("Enter a Choice: ")

if Choice == "1":
    username = input("Enter Your UserName: ")
    length = int(input("How long do you want your password to be?: "))
    char = string.ascii_letters + string.digits + string.punctuation
    passowrd = []
    for i in range(length):
        x = random.choice(char)
        passowrd.append(x)

    finall_password = "".join(passowrd)
    encryption_password = encryption_proccess.encrypt(finall_password.encode())

    current_datetime = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    str_Current_DateTime = str(current_datetime)
    write_header = not os.path.exists(file_name)

    with open(file_name, "a", encoding="utf-8", newline="") as file:
        writter = csv.writer(file)
        if write_header:
            writter.writerow(["UserName", "Password", "Date Created"])
        writter.writerow([username, encryption_password.decode(), str_Current_DateTime])

    print("\n✅ Password Saved Successfully!")
    print(f"User: {username}")
    print(f"Password: {finall_password}")
    print(f"Date: {current_datetime}")


elif Choice == "2":

    if not os.path.exists(file_name):
        print("⚠️ Nothing yet.")
    else:

        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader, None)  # // Skip Header
            print("\n📜 Saved Passwords:")

            for lines in reader:
                if not lines:
                    continue  # // Skip Empty Lines
                try:
                    decrypted_password = encryption_proccess.decrypt(
                        lines[1].encode()
                    ).decode()
                except Exception as a:
                    decrypted_password = "<decryption error>"
                    print(
                        f"User: {lines[0]} | Password: {decrypted_password} | Date: {lines[2]}"
                    )

elif Choice == "3":
    Search = input("Enter Data To Search: ")
    Found = False
    if not os.path.exists(file_name):
        print("⚠️ No saved passwords yet.")
    else:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # // Skip Header

            for line in reader:
                if Search in line:
                    decrypted_password = encryption_proccess.decrypt(
                        line[1].encode()
                    ).decode()
                    print("\n🔍 Found")
                    print(
                        f"User: {line[0]} | Password: {decrypted_password} | Date: {line[2]}"
                    )
                    Found = True
                    break

        if not Found:
            print("❌ Not Found.")
