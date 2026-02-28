from faker import Faker
import os

fake = Faker()

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("🧑‍💼 FAKE USER PROFILE (FOR TESTING ONLY)\n")

for i in range(3):
    print(f"Name: {fake.name()}")
    print(f"Job: {fake.job()}")
    print(f"Company: {fake.company()}")
    print(f"Email: {fake.email()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"Address: {fake.address()}")
    print(f"Bio: {fake.text(max_nb_chars=80)}")
    print("-" * 40)
