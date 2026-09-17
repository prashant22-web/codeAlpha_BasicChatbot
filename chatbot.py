print("🤖 Hello! Main ek basic chatbot hoon.")

while True:
    user = input("You: ").lower().strip()

    if user == "hello":
        print("Bot: Hello! Kaise ho?")

    elif user == "how are you":
        print("Bot: I am fine! How are you?")

    elif user == "what is your name":
        print("Bot: My name is CodeBot.")

    elif user == "what can you do":
        print("Bot: I can chat with you and answer basic questions.")

    elif user == "thanks":
        print("Bot: You're welcome! 😊")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day ☀️")
    elif user == "good evening":
        print("Bot: Good evening! 😊")

    elif user == "good night":
        print("Bot: Good night! Sweet dreams 🌙")

    elif user == "who created you":
        print("Bot: I was created as a CodeAlpha project.")

    elif user == "help":
        print("Bot: You can ask me about my name, how I am, or say hello.")

    elif user == "bye":
        print("Bot: Bye! Have a nice day 😊")
        break 
    else:
        print("Bot :sorry ,I don't understand that.")
        