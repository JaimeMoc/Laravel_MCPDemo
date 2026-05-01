import google.generativeai as genai

from app.llm.base_llm import BaseLLM
from app.config.settings import settings

# Clase que implementa el cliente para Gemini LLM, heredando de BaseLLM
class GeminiClient(BaseLLM):
    """
    Gemini LLM client implementation.
    """

    # Inicializa el cliente de Gemini, configurando la API y cargando el modelo
    def __init__(self):
        """
        Initialize Gemini client.
        """

        # Verifica que la clave de API de Gemini esté presente en las variables de entorno
        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment.")

        # Configura la API.
        genai.configure(api_key=settings.gemini_api_key)

        # Carga el modelo.
        self.model = genai.GenerativeModel(
            settings.gemini_model
        )

    # Implementa el método generate, que genera una respuesta utilizando Gemini
    def generate(self, prompt: str) -> str:
        """
        Generate response using Gemini.
        """

        # Intenta generar una respuesta utilizando el modelo de Gemini, manejando cualquier excepción que pueda ocurrir
        try:
            response = self.model.generate_content(
                prompt
            )

            # Devuelve el texto de la respuesta generada por Gemini
            return response.text

        # Si ocurre una excepción, devuelve un mensaje de error con la información de la excepción
        except Exception as e:
            return f"Gemini error: {str(e)}"