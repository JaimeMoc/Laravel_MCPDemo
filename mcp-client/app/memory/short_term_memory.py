class ShortTermMemory:
    """
    In-memory short-term memory.

    Stores recent conversation messages.
    """

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages = []

    def add(self, role: str, content: str):
        """
        Add message to memory.

        Args:
            role (str): user or assistant
            content (str): message text
        """

        self.messages.append({
            "role": role,
            "content": content
        })

        self._trim()

    def get_all(self):
        """
        Return all messages.
        """
        return self.messages

    def clear(self):
        """
        Clear memory.
        """
        self.messages = []

    def _trim(self):
        """
        Keep memory size within limits.
        """

        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def size(self):
        """
        Return number of messages.
        """

        return len(self.messages)