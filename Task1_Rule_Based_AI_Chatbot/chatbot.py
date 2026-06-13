print("=" * 40)
print("      AI Assistant ChatBot")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Welcome to AI ChatBot.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is AI Assistant.")

    elif user == "python":
        print("Bot: Python is a popular programming language.")

    elif user == "ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "machine learning":
        print("Bot: Machine Learning is a subset of AI.")

    elif user == "college":
        print("Bot: I don't know your college yet.")

    elif user == "time":
        from datetime import datetime
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Thank you for using AI ChatBot. Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")