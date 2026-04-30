from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """This defines what every provider must do and what methos it can access"""
    
    @abstractmethod
    def send(self, prompt) -> str:
        pass