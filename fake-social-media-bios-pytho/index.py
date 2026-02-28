from faker import Faker
import random
import os

fake = Faker()

usernames = ["vibe.master", "code.ninja", "digital.ghost", "late.night.dev", "404.me"]
emojis = ["✨", "🔥", "😎", "💻", "🚀", "🎯", "🌙"]

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("📱 FAKE SOCIAL MEDIA BIOS (FOR TESTING ONLY)\n")

for i in range(5):
    username = random.choice(usernames) + str(random.randint(1, 999))
    bio = fake.sentence(nb_words=8)
    followers = random.randint(100, 50000)

    print(f"Username: @{username}")
    print(f"Bio: {bio} {random.choice(emojis)}")
    print(f"Followers: {followers}")
    print("-" * 40)
