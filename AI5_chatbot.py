# Function to get response from the chatbot
def get_response(user_query):
    # Define some basic responses
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm just a chatbot, but thanks for asking! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "screen": "The screen warranty is only 6 months.",
        "battery": "The battery warranty is 1 year.",
        "camera": "The camera warranty is 6 months.",
        "ram": "The RAM warranty is 1 year.",
        "sim": "The SIM card warranty is not provided."
    }

    # Check if user query exists in responses
    if user_query in responses:
        return responses[user_query]
    else:
        # Check if the user query contains specific keywords
        for keyword, response in responses.items():
            if keyword in user_query:
                return response
        # If no matching response found, return a default message
        return "Sorry, I didn't understand your query. Could you please rephrase?"

# Main function
def main():
    print("Welcome to Customer Care Chatbot")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_query = input("User: ")

        if user_query == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response(user_query)
        print("Chatbot:", response)

# Run the main function
if __name__ == "__main__":
    main()
'''
OUTPUT 
 
Welcome to Customer Care Chatbot 
You can start chatting. Type 'bye' to exit. 
User: hi 
Chatbot: Hello! How can I assist you today? 
User: How are you? 
Chatbot: I'm just a chatbot, but thanks for asking! How can I help you? 
User: What is the warranty for the camera? 
Chatbot: The camera warranty is 6 months. 
User: Can you tell me about the RAM? 
Chatbot: The RAM warranty is 1 year. 
User: What about the screen? 
Chatbot: The screen warranty is only 6 months. 
User: Bye 
Chatbot: Goodbye! Have a great day! 
'''