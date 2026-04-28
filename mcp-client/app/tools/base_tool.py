from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseTool(ABC):
    """
    Abstract base class for all tools.

    Every tool must implement the execute method.
    """

    def __init__(
        self,
        name: str,
        description: str
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute the tool.

        Args:
            payload (dict): Input data for the tool

        Returns:
            dict: Tool response
        """
        pass

    def info(self) -> Dict[str, str]:
        """
        Return tool metadata.
        """

        return {
            "name": self.name,
            "description": self.description
        }