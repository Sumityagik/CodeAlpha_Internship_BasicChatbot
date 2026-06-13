def response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "how are you?" in user_input:
        return "I'm fine, thanks!"
    elif "whatsapp" in user_input:
        return "I'm doing great! thanks"
    elif "bye" in user_input or "goodboy" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. You can say 'Hello', 'How are you?' , or 'Bye'."

def chatbot():
    print("=== Welcome to CodeAlpha Rule-Based Chatbot ===")
    print("Type 'bye' to exit the conversation.\n")

    while True:
        user_message = input("you: ")
        bot_message = response(user_message)

        print(f"Bot: {bot_message}")

        if "Goodbye" in bot_message.lower() or "bye" in bot_message.lower():
            break

if __name__ == "__main__":
    chatbot()