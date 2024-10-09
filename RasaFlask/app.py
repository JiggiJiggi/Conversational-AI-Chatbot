from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define the Rasa server URL
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    # Send the user's message to the Rasa chatbot server
    response = requests.post(
        RASA_SERVER_URL,
        json={"sender": "user", "message": user_message}
    )

    # Retrieve the bot's response
    chatbot_reply = response.json()

    # Check if there is a valid response
    if chatbot_reply:
        bot_message = chatbot_reply[0]["text"]
    else:
        bot_message = "I couldn't understand that. Can you please rephrase?"

    # Return the bot's response
    return jsonify({"message": bot_message})


if __name__ == "__main__":
    app.run(debug=True)
