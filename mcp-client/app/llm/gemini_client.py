import google.generativeai as genai

from app.llm.base_llm import BaseLLM
from app.config.settings import settings

class GeminiClient(BaseLLM):
    """
    Gemini LLM client implementation.
    """

    def __init__(self):
        """
        Initialize Gemini client.
        """

        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment.")

        # Configure API
        genai.configure(api_key=settings.gemini_api_key)

        # Load model
        self.model = genai.GenerativeModel(
            settings.gemini_model
        )

    def generate(self, prompt: str) -> str:
        """
        Generate response using Gemini.
        """

        try:
            response = self.model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:
            return f"Gemini error: {str(e)}"