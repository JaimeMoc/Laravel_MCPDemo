from app.config.settings import settings
from app.llm.llm_factory import get_llm

class LLMRouter:
    """
    Routes requests to selected LLM.
    """

    def __init__(self):
        self.llm = get_llm()

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

    def _build_prompt(self, prompt: str, context):
        """
        Combine context and prompt.
        """

        messages = []

        for msg in context:
            role = msg["role"]
            content = msg["content"]
            messages.append(f"{role}: {content}")

        messages.append(f"user: {prompt}")

        return "\n".join(messages)