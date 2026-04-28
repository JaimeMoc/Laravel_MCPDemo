import json
import os
from app.config.settings import settings

class LongTermMemory:
    """
    Persistent long-term memory.

    Stores conversation history to disk.
    """

    def __init__(self, filename: str = "conversation_history.json"):

        self.memory_path = settings.memory_path
        self.filepath = os.path.join(
            self.memory_path,
            filename
        )

        self._ensure_directory()
        self._ensure_file()

    def add(self, role: str, content: str):
        """
        Add message to persistent memory.
        """

        data = self._load()

        data.append({
            "role": role,
            "content": content
        })

        self._save(data)

    def get_all(self):
        """
        Retrieve all stored messages.
        """

        return self._load()

    def clear(self):
        """
        Clear stored memory.
        """

        self._save([])

    def _load(self):
        """
        Load memory from file.
        """

        try:
            with open(self.filepath, "r") as f:
                return json.load(f)

        except Exception:
            return []

    def _save(self, data):
        """
        Save memory to file.
        """

        with open(self.filepath, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

    def _ensure_directory(self):
        """
        Ensure memory directory exists.
        """

        if not os.path.exists(self.memory_path):
            os.makedirs(self.memory_path)

    def _ensure_file(self):
        """
        Ensure memory file exists.
        """

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)