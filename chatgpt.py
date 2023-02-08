import os
import openai
from decouple import config as env


class ChatGPT:
    openai.api_key = env("OPENAI_API_KEY")

    start_prompt = '\nHuman: '
    restart_prompt = '\nGPT3: '

    def send_prompt(self, user, prompt, context=''):
        prompt = context + self.start_prompt + prompt + self.restart_prompt

        if len(prompt)>4000:
            prompt = prompt[-4000:]

        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=prompt, 
            temperature=0, 
            max_tokens=2500,
            user=user)

        response_text = response.choices[0].text
        # limit caracters in whatsapp message is 1600
        if len(response_text)>1599:
            response_text = response_text[:1599]

        context = prompt + response_text
        Response = {'response' : response_text , 'context' : context}
        return Response
