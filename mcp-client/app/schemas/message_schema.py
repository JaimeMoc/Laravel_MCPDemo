from pydantic import BaseModel, Field
from typing import Optional, List

# Clase que representa un mensaje en una conversación.
class Message(BaseModel):
    """
    Represents a single message in a conversation.
    """

    # El rol del remitente del mensaje (usuario, asistente, sistema, herramienta).
    role: str = Field(
        ...,
        description="Role of the message sender (user, assistant, system, tool)"
    )

    # El contenido del mensaje.
    content: str = Field(
        ...,
        description="Message content"
    )

    # El nombre del remitente del mensaje (opcional).
    name: Optional[str] = Field(
        default=None,
        description="Optional sender name"
    )

# Clase que representa una conversación compuesta por una lista de mensajes.
class Conversation(BaseModel):
    """
    Represents a list of messages forming a conversation.
    """

    messages: List[Message] = Field(
        default_factory=list,
        description="List of conversation messages"
    )

    # Método para agregar un mensaje a la conversación.
    def add_message(self, role: str, content: str):
        """
        Add message to conversation.
        """

        # Crea un nuevo mensaje
        message = Message(
            role=role,
            content=content
        )

        self.messages.append(message)

    # Método para obtener todos los mensajes de la conversación.
    def get_messages(self) -> List[Message]:
        """
        Return all messages.
        """

        return self.messages

    # Método para limpiar la conversación.
    def clear(self):
        """
        Clear conversation.
        """

        self.messages = []