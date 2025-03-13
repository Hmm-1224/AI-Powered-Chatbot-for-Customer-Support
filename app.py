from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.form['message']

        if not user_message:
            return jsonify({"response": "No message provided."})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_response = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
