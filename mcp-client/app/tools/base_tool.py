from abc import ABC, abstractmethod
from typing import Dict, Any

# Clase base abstracta para todas las herramientas.
class BaseTool(ABC):
    """
    Abstract base class for all tools.

    Every tool must implement the execute method.
    """

    # Método constructor que inicializa el nombre y la descripción de la herramienta.
    def __init__(
        self,
        name: str,
        description: str
    ):
        self.name = name
        self.description = description

    # Método abstracto que debe ser implementado por cada herramienta específica.
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

    # Método para obtener la información de la herramienta.
    def info(self) -> Dict[str, str]:
        """
        Return tool metadata.
        """

        return {
            "name": self.name,
            "description": self.description
        }