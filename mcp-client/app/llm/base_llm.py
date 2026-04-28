from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """
    Abstract base class for all LLM clients.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt (str): Input prompt

        Returns:
            str: Generated response
        """
        pass