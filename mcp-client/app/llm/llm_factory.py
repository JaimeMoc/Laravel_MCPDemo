from app.config.settings import settings
from app.llm.gemini_client import GeminiClient
from app.llm.ollama_client import OllamaClient

# Clase de fábrica para obtener la instancia del LLM seleccionado según la configuración
def get_llm():
    """
    Factory to return selected LLM.
    """

    # Obtiene el proveedor de LLM de la configuración y devuelve la instancia correspondiente
    provider = settings.llm_provider.lower()

    # Verifica el proveedor y devuelve la instancia del cliente correspondiente, o lanza un error si el proveedor no es soportado
    if provider == "gemini":
        return GeminiClient()

    # Si el proveedor es "ollama", devuelve una instancia de OllamaClient
    elif provider == "ollama":
        return OllamaClient()

    # Si el proveedor no es reconocido, lanza un error indicando que el proveedor de LLM no es soportado
    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )