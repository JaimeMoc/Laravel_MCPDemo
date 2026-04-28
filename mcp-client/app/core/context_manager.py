class ContextManager:
    """
    Handles conversation context and history.
    """

    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.history = []

    def add_user_message(self, message: str):
        """
        Add user message to history.
        """
        self.history.append({
            "role": "user",
            "content": message
        })

        self._trim_history()

    def add_assistant_message(self, message: str):
        """
        Add assistant response to history.
        """
        self.history.append({
            "role": "assistant",
            "content": message
        })

        self._trim_history()

    def get_context(self):
        """
        Return conversation context.
        """
        return self.history

    def clear(self):
        """
        Clear conversation history.
        """
        self.history = []

    def _trim_history(self):
        """
        Keep history size under limit.
        """
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]