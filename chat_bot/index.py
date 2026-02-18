import time

def type_effect(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

print("ChatBot: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        type_effect("ChatBot: Bye! See you soon 👋")
        break
    elif "hello" in user.lower():
        type_effect("ChatBot: Hey there! 👋")
    elif "how are you" in user.lower():
        type_effect("ChatBot: I'm just code, but I'm vibing 😎")
    else:
        type_effect("ChatBot: I’m still learning. Try saying hello!")
