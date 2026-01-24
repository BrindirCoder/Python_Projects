import random

motivational_quotes = [
    "Discipline beats motivation every single time.",
    "Your future self is watching. Don’t disappoint.",
    "Dreams don’t work unless you do.",
    "Stay consistent. Results will come.",
    "No excuses. Just results.",
]

savage_quotes = [
    "You said you would start yesterday. Interesting.",
    "Stop waiting for motivation. It’s not coming.",
    "If laziness was a sport, you’d be undefeated.",
    "You’re not tired. You’re just unmotivated.",
    "Same habits, same results. Shocking.",
]

print("🔥 Random Quprinote Generator 🔥")
print("1️⃣ Motivational")
print("2️⃣ Savage")

choice = input("Choose a mode (1 or 2):")

if choice == "1":
    quote = random.choice(motivational_quotes)
    print("\n Quote: ")
    print(quote)

elif choice == "2":
    quote = random.choice(savage_quotes)
    print("\nQuote: ")
    print(quote)

else:
    print("\n Invalid choice . Run again")
    
