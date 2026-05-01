from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Definición de la clase de configuración global usando Pydantic. Permite configurar el MCP Server, LLM (Gemini u Ollama), memoria, y opciones de depuración.
class Settings(BaseModel):
    """
    Global application settings.
    Supports Gemini (cloud) and Ollama (local LLM).
    """

    # Configuración del MCP SERVER
    mcp_server_url: str = Field(
        default=os.getenv("MCP_SERVER_URL", "http://localhost:8000"),
        description="URL of the MCP server"
    )

    mcp_timeout: int = Field(
        default=int(os.getenv("MCP_TIMEOUT", "30")),
        description="Timeout for MCP requests"
    )

    # CONFIGURACIÓN DE LLM
    llm_provider: str = Field(
        default=os.getenv("LLM_PROVIDER", "gemini"),
        description="LLM provider: gemini or ollama"
    )

    # GEMINI CONFIG (Cloud)
    gemini_api_key: str = Field(
        default=os.getenv("GEMINI_API_KEY", ""),
        description="Gemini API Key"
    )

    gemini_model: str = Field(
        default=os.getenv("GEMINI_MODEL", "gemini-1.5-pro"),
        description="Gemini model name"
    )

    # OLLAMA CONFIG (Local)
    ollama_base_url: str = Field(
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        description="Ollama base URL"
    )

    ollama_model: str = Field(
        default=os.getenv("OLLAMA_MODEL", "deepseek-coder:6.7b"),
        description="Ollama model name"
    )

    # MEMORY CONFIG
    memory_backend: str = Field(
        default=os.getenv("MEMORY_BACKEND", "inmemory"),
        description="Memory backend"
    )

    memory_path: str = Field(
        default=os.getenv("MEMORY_PATH", "./memory_data"),
        description="Memory path"
    )

    # APP CONFIG
    debug: bool = Field(
        default=os.getenv("DEBUG", "true").lower() == "true",
        description="Debug mode"
    )

    log_level: str = Field(
        default=os.getenv("LOG_LEVEL", "INFO"),
        description="Logging level"
    )

# Instancia global
settings = Settings()