import random

number = random.randint(1, 100)
attempts = 0

print("Guess the Number Game")
print("I'm thinking between 1 and 100")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Plase enter a number")
        continue

    guess = int(guess)

    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct You guessed it in {attempts} attempts")
        break
