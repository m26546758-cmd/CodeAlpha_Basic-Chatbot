def get_reply(message):
    message = message.strip().lower()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I don't understand. Try saying hello, asking how I am, or saying bye."


def main():
    print("Chatbot: Hello! Say 'hello', 'how are you', or 'bye' to exit.")

    while True:
        message = input("You: ")
        reply = get_reply(message)
        print(f"Chatbot: {reply}")

        if message.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()
