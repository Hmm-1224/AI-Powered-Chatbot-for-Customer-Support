from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if the API key is loaded properly
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("API Key not found!")
else:
    print("API Key loaded successfully.")

# Set OpenAI API key from environment variable
openai.api_key = api_key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Get the user's message from the request JSON (instead of form data)
        user_message = request.json.get('message')  # Using JSON data

        if not user_message:
            return jsonify({"response": "No message received."})

        # OpenAI API call with gpt-3.5-turbo or gpt-4 using the chat-based format
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )

        # Extract the response from OpenAI
        bot_response = response['choices'][0]['message']['content'].strip()

        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
