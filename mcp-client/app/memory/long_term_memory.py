import json
import os
from app.config.settings import settings

# Clase que implementa la memoria a largo plazo persistente.
class LongTermMemory:
    """
    Persistent long-term memory.

    Stores conversation history to disk.
    """

    # Inicializa la memoria a largo plazo, configurando la ruta del archivo donde se almacenará el historial de conversaciones
    def __init__(self, filename: str = "conversation_history.json"):

        self.memory_path = settings.memory_path
        self.filepath = os.path.join(
            self.memory_path,
            filename
        )

        self._ensure_directory()
        self._ensure_file()

    # Método para agregar un mensaje al historial de conversaciones, especificando el rol (por ejemplo, "user" o "assistant") y el contenido del mensaje
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

    # Método para recuperar todo el historial de conversaciones almacenado en la memoria a largo plazo
    def get_all(self):
        """
        Retrieve all stored messages.
        """

        return self._load()

    # Método para borrar todo el historial de conversaciones almacenado en la memoria a largo plazo
    def clear(self):
        """
        Clear stored memory.
        """

        self._save([])

    # Método privado para cargar el historial de conversaciones desde el archivo, devolviendo una lista de mensajes.
    def _load(self):
        """
        Load memory from file.
        """

        try:
            with open(self.filepath, "r") as f:
                return json.load(f)

        except Exception:
            return []

    # Método privado para guardar el historial de conversaciones en el archivo, recibiendo una lista de mensajes como argumento
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

    # Método privado para asegurar que el directorio donde se almacenará el historial de conversaciones exista, y si no existe, lo crea
    def _ensure_directory(self):
        """
        Ensure memory directory exists.
        """

        if not os.path.exists(self.memory_path):
            os.makedirs(self.memory_path)

    # Método privado para asegurar que el archivo donde se almacenará el historial de conversaciones exista, y si no existe, lo crea con un contenido inicial de una lista vacía
    def _ensure_file(self):
        """
        Ensure memory file exists.
        """

        # Verifica si el archivo de memoria existe, y si no existe, lo crea con una lista vacía como contenido inicial
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)