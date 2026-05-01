from app.config.settings import settings
from app.llm.llm_factory import get_llm

# Clase que envía solicitudes a un modelo de lenguaje específico.
class LLMRouter:
    """
    Routes requests to selected LLM.
    """

    # Llamada directa al modelo configurado. 
    def __init__(self):
        self.llm = get_llm()

    # Método principal para generar respuestas a partir de un prompt. 
    def generate(self, prompt: str, context=None) -> str:
        """
        Generate LLM response.
        """

        if context:
            full_prompt = self._build_prompt(prompt, context)
        else:
            full_prompt = prompt

        response = self.llm.generate(full_prompt)

        return response

    # Método privado para construir el prompt combinando el contexto y el prompt del usuario.
    def _build_prompt(self, prompt: str, context):
        """
        Combine context and prompt.
        """

        # Inicialización de la lista de mensajes.
        messages = []

        for msg in context:
            role = msg["role"]
            content = msg["content"]
            messages.append(f"{role}: {content}")

        messages.append(f"user: {prompt}")

        return "\n".join(messages)