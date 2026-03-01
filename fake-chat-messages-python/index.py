from faker import Faker
import random
import time
import os

fake = Faker()

users = ["Alex", "Jamie", "Taylor", "Sam"]
emojis = ["😂", "😅", "🔥", "👀", "💀", "😎"]

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("💬 FAKE CHAT MESSAGES (FOR DEMO ONLY)\n")

for _ in range(10):
    sender = random.choice(users)
    message = fake.sentence(nb_words=random.randint(4, 10))
    emoji = random.choice(emojis)

    print(f"{sender}: {message} {emoji}")
    time.sleep(0.6)
