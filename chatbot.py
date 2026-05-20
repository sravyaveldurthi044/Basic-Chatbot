# Advanced Basic Chatbot Program

print("===================================")
print("     Welcome to Simple Chatbot     ")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "hi":
        print("Bot: Hello there!")

    elif user_input == "good morning":
        print("Bot: Good Morning!")

    elif user_input == "good evening":
        print("Bot: Good Evening!")

    # Basic Questions
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "what is your name":
        print("Bot: My name is Simple Bot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python.")

    elif user_input == "what can you do":
        print("Bot: I can chat with you and answer simple questions.")

    # Date and Time
    elif user_input == "time":
        print("Bot: Sorry, I cannot show real time now.")

    elif user_input == "date":
        print("Bot: Sorry, I cannot show today's date now.")

    # Fun Replies
    elif user_input == "tell me a joke":
        print("Bot: Why did the computer go to school? Because it wanted to improve its bytes!")

    elif user_input == "i am sad":
        print("Bot: Don't worry, everything will be okay!")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I don't understand that.")
