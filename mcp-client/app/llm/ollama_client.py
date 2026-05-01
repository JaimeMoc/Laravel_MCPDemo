import requests

from app.llm.base_llm import BaseLLM
from app.config.settings import settings

# Clase que implementa el cliente para Ollama LLM, heredando de BaseLLM
class OllamaClient(BaseLLM):
    """
    Ollama LLM client implementation.
    """

    # Inicializa el cliente de Ollama, configurando la URL base y el modelo a utilizar
    def __init__(self):
        """
        Initialize Ollama client.
        """

        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_model

    # Implementa el método generate, que genera una respuesta utilizando Ollama
    def generate(self, prompt: str) -> str:
        """
        Generate response using Ollama.
        """

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        # Intenta generar una respuesta utilizando el modelo de Ollama, manejando cualquier excepción que pueda ocurrir
        try:
            response = requests.post(
                url,
                json=payload
            )

            response.raise_for_status()
            data = response.json()

            return data.get("response", "")

        # Si ocurre una excepción relacionada con la solicitud HTTP, devuelve un mensaje de error con la información de la excepción
        except requests.RequestException as e:
            return f"Ollama error: {str(e)}"