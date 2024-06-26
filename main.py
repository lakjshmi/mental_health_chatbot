import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#defining a function to send user reply to openai
def get_chatbot_response(user_input):
    
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )

        response = completion['choices'][0]['message']['content']
        return response
    # exceptions handling and provide an error message
    except Exception as e:
        
        return f"Sorry, an error occurred: {str(e)}"

#main function to run the command line interface to talk to the bot
def main():
    
    print("Welcome to the Mental Health Chatbot. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for reaching out. Take car!")
            break
        
        response = get_chatbot_response(user_input)
        print("Mr Bot:", response)

if __name__ == "__main__":
    main()
