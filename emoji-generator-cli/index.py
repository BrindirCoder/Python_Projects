import random

emojis = {
    "happy": ["😄", "😊", "😁", "🥳", "😎"],
    "sad": ["😢", "😭", "😞", "😔", "💔"],
    "angry": ["😡", "🤬", "😠", "🔥"],
    "love": ["❤️", "😍", "😘", "💖"],
    "cool": ["😎", "🧊", "🤙"]
}

print("🎭 Random Emoji Generator 🎭")
print("Choose a mood:")

for mood in emojis:
    print("-", mood)

user_mood = input("\nEnter your mood: ").lower().strip()

if user_mood in emojis:
    emoji = random.choice(emojis[user_mood])
    print("\nYour emoji:")
    print(emoji)
else:
    print("\n❌ Mood not found.")
