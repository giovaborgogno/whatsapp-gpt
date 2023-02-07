from flask import Flask, request
from twilio_whatsapp import send_message
from db_config import engine, Session, Base, User

app = Flask(__name__)

# inicializa la base de datos
session = Session()
Base.metadata.create_all(engine)

@app.route("/", methods=['POST'])
def handle_message():
    # Get the message from the incoming request
    message = request.values.get('Body', '')
    from_number = request.values.get('From', '')

    response = send_message(from_number, message)

    return response, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
