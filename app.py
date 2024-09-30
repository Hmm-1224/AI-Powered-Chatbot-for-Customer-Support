import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    
    # Send the user input to OpenAI's GPT-3 model
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': user_input}
        ]
    )
    
    # Extract the response from the OpenAI API
    bot_reply = response.choices[0].message['content']
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)

