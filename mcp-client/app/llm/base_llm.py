from abc import ABC, abstractmethod

# Clase que define la interfaz para los clientes de LLM (Language Model)
class BaseLLM(ABC):
    """
    Abstract base class for all LLM clients.
    """

    # Método abstracto que debe ser implementado por todas las clases que hereden de BaseLLM
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