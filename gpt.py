from auth import *
from pprint import pprint

class GPTConversation:
    def __init__(self, message="You are a helpful assistant."):
        set_openai_key()
        self.messages = self._initialize_messages(message)

    def _initialize_messages(self, message):
        return [{"role": "system", "content": message}]

    def chat(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages
        )
        # Append the response to the messages
        self.messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        # Print the response
        print(response['choices'][0]['message']['content'])
        #pprint(self.messages)
