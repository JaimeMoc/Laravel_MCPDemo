from pydantic import BaseModel, Field
from typing import Optional, List


class Message(BaseModel):
    """
    Represents a single message in a conversation.
    """

    role: str = Field(
        ...,
        description="Role of the message sender (user, assistant, system, tool)"
    )

    content: str = Field(
        ...,
        description="Message content"
    )

    name: Optional[str] = Field(
        default=None,
        description="Optional sender name"
    )

class Conversation(BaseModel):
    """
    Represents a list of messages forming a conversation.
    """

    messages: List[Message] = Field(
        default_factory=list,
        description="List of conversation messages"
    )

    def add_message(self, role: str, content: str):
        """
        Add message to conversation.
        """

        message = Message(
            role=role,
            content=content
        )

        self.messages.append(message)

    def get_messages(self) -> List[Message]:
        """
        Return all messages.
        """

        return self.messages

    def clear(self):
        """
        Clear conversation.
        """

        self.messages = []