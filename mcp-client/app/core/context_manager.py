# Clase para manejar el contexto de la conversación y el historial. Permite agregar mensajes del usuario y del asistente, obtener el contexto actual, y limpiar el historial. También se asegura de mantener el tamaño del historial dentro de un límite definido.
class ContextManager:
    """
    Handles conversation context and history.
    """

    # Inicialización del ContextManager con un límite de mensajes en el historial. El historial se almacena como una lista de diccionarios con roles (usuario o asistente) y contenido.
    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.history = []

    # Método para agregar un mensaje del usuario al historial. Después de agregar el mensaje, se llama a un método privado para recortar el historial si excede el límite.
    def add_user_message(self, message: str):
        """
        Add user message to history.
        """
        self.history.append({
            "role": "user",
            "content": message
        })

        self._trim_history()

    # Método para agregar un mensaje del asistente al historial. Similar al método de usuario, pero con el rol de asistente.
    def add_assistant_message(self, message: str):
        """
        Add assistant response to history.
        """
        self.history.append({
            "role": "assistant",
            "content": message
        })

        self._trim_history()

    # Método para obtener el contexto actual de la conversación, que es simplemente el historial completo de mensajes. Este contexto se puede usar para proporcionar información al LLM al generar respuestas.
    def get_context(self):
        """
        Return conversation context.
        """
        return self.history

    # Método para limpiar el historial de la conversación, eliminando todos los mensajes almacenados.
    def clear(self):
        """
        Clear conversation history.
        """
        self.history = []

    # Método privado para recortar el historial si excede el límite definido. Si el número de mensajes en el historial es mayor que el límite, se mantiene solo la parte más reciente del historial.
    def _trim_history(self):
        """
        Keep history size under limit.
        """
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]