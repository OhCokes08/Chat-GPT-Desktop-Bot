import openai
import threading

class ChatBot:
    def __init__(self):
        openai.api_key = "API Key"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens = 3000,
            temperature = 0.5
        ).choices[0].text
        return response

