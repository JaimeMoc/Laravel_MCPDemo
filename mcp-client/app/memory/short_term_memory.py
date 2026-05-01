# Clase que implementa la memoria a corto plazo en memoria.
class ShortTermMemory:
    """
    In-memory short-term memory.

    Stores recent conversation messages.
    """

    # Inicializa la memoria con un límite de mensajes.
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages = []

    # Método para agregar un mensaje a la memoria.
    def add(self, role: str, content: str):
        """
        Add message to memory.

        Args:
            role (str): user or assistant
            content (str): message text
        """

        # Agrega el mensaje a la lista de mensajes.
        self.messages.append({
            "role": role,
            "content": content
        })

        self._trim()

    # Método para obtener todos los mensajes almacenados.
    def get_all(self):
        """
        Return all messages.
        """
        return self.messages

    # Método para limpiar la memoria.
    def clear(self):
        """
        Clear memory.
        """
        self.messages = []

    # Método privado para mantener el tamaño de la memoria dentro de los límites establecidos.
    def _trim(self):
        """
        Keep memory size within limits.
        """

        # Si el número de mensajes excede el límite, se eliminan los mensajes más antiguos.
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    # Método para obtener el número de mensajes almacenados.
    def size(self):
        """
        Return number of messages.
        """

        return len(self.messages)