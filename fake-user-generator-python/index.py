from faker import Faker  #Install the package:pip install faker
import os

fake = Faker()

# Clear terminal (Windows/Mac/Linux)
os.system("cls" if os.name == "nt" else "clear")

for i in range(5):
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Phone number: {fake.phone_number()}")
    print(f"Address: {fake.address()}")
    print("-" * 30)
