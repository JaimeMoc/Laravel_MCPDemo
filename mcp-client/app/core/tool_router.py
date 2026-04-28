import requests
from app.config.settings import settings

class ToolRouter:
    """
    Handles MCP tool execution.
    """

    def __init__(self):
        self.base_url = settings.mcp_server_url
        self.timeout = settings.mcp_timeout

    def execute(self, tool_name: str, payload=None):
        """
        Execute MCP tool.
        """

        if payload is None:
            payload = {}

        url = f"{self.base_url}/tools/{tool_name}"

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            return {
                "error": str(e)
            }