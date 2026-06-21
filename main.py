print("🤖 AI Chatbot is running... Type 'exit' to stop")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("Bot: I'm just a program, but I'm doing great! 😊")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "help":
        print("Bot: You can say hello, ask questions, or type exit.")

    elif user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")