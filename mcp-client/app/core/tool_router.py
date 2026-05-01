import requests
from app.config.settings import settings

# Clase encargada de manejar la ejecución de herramientas MCP.
class ToolRouter:
    """
    Handles MCP tool execution.
    """

    # Inicialización que establece la URL base y el tiempo de espera para las solicitudes a las herramientas MCP.
    def __init__(self):
        self.base_url = settings.mcp_server_url
        self.timeout = settings.mcp_timeout

    # Método principal para ejecutar una herramienta MCP específica con una carga útil opcional.
    def execute(self, tool_name: str, payload=None):
        """
        Execute MCP tool.
        """

        # Si no se proporciona una carga útil, se inicializa como un diccionario vacío.
        if payload is None:
            payload = {}

        url = f"{self.base_url}/tools/{tool_name}"

        # Se intenta enviar una solicitud POST a la URL de la herramienta con la carga útil y el tiempo de espera configurados. Si la solicitud es exitosa, se devuelve la respuesta JSON. Si ocurre un error durante la solicitud, se captura la excepción y se devuelve un diccionario con el mensaje de error.
        try:
            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response.json()

        # Captura de excepciones relacionadas con las solicitudes HTTP, devolviendo un diccionario con el mensaje de error en caso de que ocurra una excepción.
        except requests.RequestException as e:
            return {
                "error": str(e)
            }