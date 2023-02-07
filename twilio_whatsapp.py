from twilio.rest import Client
from decouple import config as env
from chatgpt import ChatGPT

chatgpt = ChatGPT()

# Twilio Account SID and Auth Token
account_sid = env('YOUR_TWILIO_ACCOUNT_SID')
auth_token = env('YOUR_TWILIO_AUTH_TOKEN')

# WhatsApp Sandbox Number
whatsapp_number = env('WHATSAPP_NUMBER_TWILIO')

# Create a Twilio Client
client = Client(account_sid, auth_token)

# Define the chatbot function
def chatbot(user, message, context=''):
  # Implement your ChatGPT logic here
  response = chatgpt.send_prompt(user, message, context)
  return response

# Send a message and receive a response
def send_message(to, message):
  response = chatbot(to, message)
  message = client.messages.create(
      to=to,
      from_=whatsapp_number,
      body=response['response']
  )
  return response

