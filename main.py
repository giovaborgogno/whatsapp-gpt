from flask import Flask, request
from twilio_whatsapp import send_message

app = Flask(__name__)

@app.route("/", methods=['POST'])
def handle_message():
    # Get the message from the incoming request
    message = request.get_json().get('Body', '')
    from_number = request.get_json().get('From', '')

    response = send_message(from_number, message)

    return response, 200

if __name__ == "__main__":
    app.run()
