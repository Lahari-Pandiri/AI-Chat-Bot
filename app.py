from chatbot import chat_response

print("Chatbot: Hello! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chat_response(user_input)
    print("Chatbot:", response)
