print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("ChatBot: Hey there 👋")
    elif "how are you" in user:
        print("ChatBot: I'm just code, but I'm feeling powerful 😎")
    elif "your name" in user:
        print("ChatBot: I'm PythonBot 🤖")
    elif "bye" in user:
        print("ChatBot: Goodbye! 👋")
        break
    else:
        print("ChatBot: I don't understand that yet 🤔")
