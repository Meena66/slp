import random

# Define a simple set of responses for the chatbot
def get_chatbot_response(user_input):
    responses = {
        "symptom": "Sleep apnea symptoms include snoring, gasping for air during sleep, and feeling tired during the day.",
        "treatment": "Treatment options for sleep apnea include CPAP therapy, surgery, and lifestyle changes such as weight loss and avoiding alcohol.",
        "help": "I am here to help! You can ask about symptoms, treatments, or other sleep apnea-related topics.",
    }
    
    # Detect keywords in user input and respond accordingly
    if "symptom" in user_input:
        return responses["symptom"]
    elif "treatment" in user_input:
        return responses["treatment"]
    elif "help" in user_input:
        return responses["help"]
    else:
        return "I'm not sure about that. Can you please ask something else?"

# Example usage
def chatbot_conversation():
    print("Chatbot: Hi! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = get_chatbot_response(user_input.lower())
        print(f"Chatbot: {response}")

# Start chatbot conversation
chatbot_conversation()
