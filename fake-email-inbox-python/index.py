from faker import Faker
import random
import os
import time

fake = Faker()

senders = ["Google", "GitHub", "Netflix", "Amazon", "LinkedIn", "Bank"]
subjects = [
    "Security Alert",
    "Welcome to our platform",
    "Your invoice is ready",
    "New login detected",
    "Action required",
    "Weekly newsletter"
]

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("📧 FAKE EMAIL INBOX (DEMO ONLY)\n")

for i in range(10):
    sender = random.choice(senders)
    subject = random.choice(subjects)
    preview = fake.sentence(nb_words=6)
    status = random.choice(["📩 Unread", "📨 Read"])
    time_received = fake.time()

    print(f"From: {sender}")
    print(f"Subject: {subject}")
    print(f"Preview: {preview}")
    print(f"Time: {time_received} | Status: {status}")
    print("-" * 45)

    time.sleep(0.4)
