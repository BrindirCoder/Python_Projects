from faker import Faker   #pip install faker
import os

fake = Faker()

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("💳 FAKE CREDIT CARDS (FOR TESTING ONLY)\n")

for i in range(5):
    print(f"Name: {fake.name()}")
    print(f"Card Provider: {fake.credit_card_provider()}")
    print(f"Card Number: {fake.credit_card_number()}")
    print(f"Expiry Date: {fake.credit_card_expire()}")
    print(f"Security Code (CVV): {fake.credit_card_security_code()}")
    print("-" * 40)
