import random

print("🎲 Dice Game – Best of 3 🎲")

player_score = 0
computer_score = 0
round_number = 1

while player_score < 2 and computer_score < 2:
    print(f"\nRound {round_number}")

    input("Press Enter to roll the dice...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print("✅ You win this round!")
        player_score += 1
    elif computer_roll > player_roll:
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("⚖️ It's a tie!")

    print(f"Score → You: {player_score} | Computer: {computer_score}")
    round_number += 1

print("\n🏁 Game Over")

if player_score > computer_score:
    print("🎉 You won the game!")
else:
    print("💀 Computer won the game!")
