import requests
from typing import Dict, Any
from app.tools.base_tool import BaseTool
from app.config.settings import settings

# Clase que representa una herramienta que se conecta al servidor Laravel MCP.
class LaravelTool(BaseTool):
    """
    Tool that connects to Laravel MCP server.
    """

    # Método constructor que inicializa el nombre, la descripción, la URL base y el tiempo de espera de la herramienta.
    def __init__(
        self,
        name: str,
        description: str
    ):
        super().__init__(name, description)

        self.base_url = settings.mcp_server_url
        self.timeout = settings.mcp_timeout

    # Método para ejecutar la herramienta, que realiza una solicitud POST al servidor Laravel MCP con los datos de entrada y maneja las posibles excepciones.
    def execute(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute Laravel MCP tool.

        Args:
            payload (dict): Tool input

        Returns:
            dict: Tool response
        """

        url = f"{self.base_url}/api/tools/{self.name}"

        # Realiza una solicitud POST al servidor Laravel MCP con los datos de entrada y maneja las posibles excepciones.
        try:
            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            return {
                "success": True,
                "data": response.json()
            }

        # Maneja diferentes tipos de excepciones que pueden ocurrir durante la solicitud HTTP y devuelve un diccionario con el estado de éxito y el mensaje de error correspondiente.
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timeout"
            }

        # Maneja la excepción de conexión y devuelve un mensaje de error indicando que no se puede conectar al servidor Laravel MCP.
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Cannot connect to Laravel MCP server"
            }

        # Maneja la excepción HTTP y devuelve un mensaje de error con el código de estado y el mensaje de error proporcionado por el servidor Laravel MCP.
        except requests.exceptions.HTTPError as e:
            return {
                "success": False,
                "error": f"HTTP error: {str(e)}"
            }

        # Maneja cualquier otra excepción general y devuelve un mensaje de error.
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }