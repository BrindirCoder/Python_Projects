import random

player_hp = 100
enemy_hp = 100

print("⚔️ Simple RPG Battle Game ⚔️")

while player_hp > 0 and enemy_hp > 0:
    print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
    print("1️⃣ Attack")
    print("2️⃣ Heal")

    choice = input("Choose your action: ")

    if choice == "1":
        damage = random.randint(10, 25)
        enemy_hp -= damage
        print(f"⚔️ You attacked the enemy for {damage} damage!")

    elif choice == "2":
        heal = random.randint(10, 20)
        player_hp += heal
        print(f"💚 You healed for {heal} HP!")

    else:
        print("❌ Invalid choice. Turn skipped.")

    if enemy_hp > 0:
        enemy_damage = random.randint(5, 20)
        player_hp -= enemy_damage
        print(f"🔥 Enemy attacked you for {enemy_damage} damage!")

if player_hp > 0:
    print("\n🏆 You defeated the enemy!")
else:
    print("\n💀 You were defeated...")
