print("===================================")
print("      Welcome to this program      ")
print("===================================\n")

score = 0

while True:

    def Question1():
        global score
        print("Question 1: What is the capital of France?")
        print("A) Berlin")
        print("B) Madrid")
        print("C) Paris")
        print("D) Rome")
        answer = input("Enter Your Answer: ")

        if answer.upper() == "C":
            print(f"Your answer:{answer}")
            print("✅ Correct!")
            score += 1
        else:
            print(f"Your answer:{answer}")
            print("Not correct. ❌")

        print("")

    def Question2():
        global score
        print("Question 2: Who created Python?")
        print("A) Linus Torvalds")
        print("B) Guido van Rossum")
        print("C) Elon Musk")
        print("D) Bill Gates")
        answer = input("Enter Your Answer: ")

        if answer.upper() == "B":
            print(f"Your answer:{answer}")
            print("✅ Correct!")
            score += 1
        else:
            print(f"Your answer:{answer}")
            print("Not correct. ❌")
        print("")

    def Question3():
        global score
        print("Question 3: What does HTML stand for?")
        print("A) HyperText Makeup Language")
        print("B) HyperText Markup Language")
        print("C) Hyper Tool Multi Language")
        print("D) Home Tool Markup Language")
        answer = input("Enter Your Answer: ")

        if answer.upper() == "B":
            print(f"Your answer:{answer}")
            print("✅ Correct!")
            score += 1
        else:
            print(f"Your answer:{answer}")
            print("Not correct. ❌")
        print("")

    def Question4():
        global score
        print("Question 4: Which data structure uses First In First Out (FIFO)?")
        print("A) Stack")
        print("B) Queue")
        print("C) Array")
        print("D) Tree")
        answer = input("Enter Your Answer: ")

        if answer.upper() == "B":
            print(f"Your answer:{answer}")
            print("✅ Correct!")
            score += 1
        else:
            print(f"Your answer:{answer}")
            print("Not correct. ❌")
        print("")

    def Question5():
        global score
        print("Question 5: Which company developed the Java programming language?")
        print("A) Microsoft")
        print("B) Sun Microsystems")
        print("C) Google")
        print("D) Apple")
        answer = input("Enter Your Answer: ")

        if answer.upper() == "B":
            print(f"Your answer:{answer}")
            print("✅ Correct!")
            score += 1
        else:
            print(f"Your answer:{answer}")
            print("Not correct. ❌")
        print("")

    Question1()
    Question2()
    Question3()
    Question4()
    Question5()

    print(f"Your total score is: {score}/5")

    if score == 5:
        print("🌟 Genius! Perfect score! 💪")
    elif score == 4:
        print("👏 Excellent work!")
    elif score == 3:
        print("👍 Good job")
    elif score == 1 or score == 2:
        print("🙂 Not bad, but you can do better!")
    else:
        print("😅 Try again, you'll get it next time!")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        break
    else:
        score = 0
