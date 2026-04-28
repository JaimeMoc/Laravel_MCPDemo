from app.config.settings import settings
from app.llm.gemini_client import GeminiClient
from app.llm.ollama_client import OllamaClient

def get_llm():
    """
    Factory to return selected LLM.
    """

    provider = settings.llm_provider.lower()

    if provider == "gemini":
        return GeminiClient()

    elif provider == "ollama":
        return OllamaClient()

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )