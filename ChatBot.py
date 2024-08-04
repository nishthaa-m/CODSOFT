#CHATBOT

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Defining responses based on predefined rules
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How can I assist you?"
    elif "your name" in user_input:
        return "I'm ChatBot, created to assist you."
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, I can help with a few things. \n You can ask me about my name, how I'm doing, or just say hello."
    else:
        return "I'm not sure how to respond to that. Can you please ask something else?"

def main():
    print("Welcome to the simple chatbot! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot: " + response)
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
