import requests
from typing import Dict, Any
from app.tools.base_tool import BaseTool
from app.config.settings import settings

class LaravelTool(BaseTool):
    """
    Tool that connects to Laravel MCP server.
    """

    def __init__(
        self,
        name: str,
        description: str
    ):
        super().__init__(name, description)

        self.base_url = settings.mcp_server_url
        self.timeout = settings.mcp_timeout

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

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timeout"
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Cannot connect to Laravel MCP server"
            }

        except requests.exceptions.HTTPError as e:
            return {
                "success": False,
                "error": f"HTTP error: {str(e)}"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }