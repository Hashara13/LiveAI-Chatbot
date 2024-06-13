from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

LIVECHAT_API_URL = "https://api.livechatinc.com/v3.4/agent/action/send_event"
ACCESS_TOKEN = "TOKEN" 
def send_message_to_livechat(message):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "chat_id": "chat_id_placeholder",  
        "event": {
            "type": "message",
            "text": message,
            "visibility": "all",
        }
    }
    response = requests.post(LIVECHAT_API_URL, headers=headers, json=data)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get("message")
    response = send_message_to_livechat(user_message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
