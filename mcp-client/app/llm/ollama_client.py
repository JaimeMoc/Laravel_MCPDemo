import requests

from app.llm.base_llm import BaseLLM
from app.config.settings import settings

class OllamaClient(BaseLLM):
    """
    Ollama LLM client implementation.
    """

    def __init__(self):
        """
        Initialize Ollama client.
        """

        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_model

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

        try:
            response = requests.post(
                url,
                json=payload
            )

            response.raise_for_status()
            data = response.json()

            return data.get("response", "")

        except requests.RequestException as e:
            return f"Ollama error: {str(e)}"