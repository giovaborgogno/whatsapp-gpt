from twilio.rest import Client
from decouple import config as env
from chatgpt import ChatGPT
from db_config import get_user_context, edit_user_context

chatgpt = ChatGPT()

# Twilio Account SID and Auth Token
account_sid = env('YOUR_TWILIO_ACCOUNT_SID')
auth_token = env('YOUR_TWILIO_AUTH_TOKEN')
# WhatsApp Sandbox Number
whatsapp_number = env('WHATSAPP_NUMBER_TWILIO')
# Create a Twilio Client
client = Client(account_sid, auth_token)


def chatbot(user, message, context=''):
  response = chatgpt.send_prompt(user, message, context)
  return response


def send_message(to, message):
  # get and edit context
  context = get_user_context(to)
  response = chatbot(to, message, context)
  edit_user_context(to, response['context'])
  
  # send whatsapp
  message = client.messages.create(
      to=to,
      from_=whatsapp_number,
      body=response['response']
  )
  return response

