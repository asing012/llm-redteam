import ollama
from .base import LLMProvider

class OllamaProvider(LLMProvider):
    def __init__(self, model="llama3.2"):
        self.model = model

    def send(self, prompt):
        response = ollama.chat(self.model, messages=[
            {
                "role": 'user',
                "content": prompt
            },
        ])
        return response.message.content
    