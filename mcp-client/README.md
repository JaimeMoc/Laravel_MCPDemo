# MCP Client

Este proyecto es un cliente de línea de comandos (CLI) para interactuar con un servidor MCP (Model Context Protocol), diseñado para flujos conversacionales inteligentes y ejecución de herramientas automatizadas.

## Características principales
- Interfaz interactiva por consola.
- Soporte para múltiples proveedores de LLM (por ejemplo, Gemini, Ollama).
- Enrutamiento automático entre herramientas y modelos de lenguaje según la entrada del usuario.
- Gestión de contexto y memoria (corto y largo plazo) para mantener el estado de la conversación.
- Modularidad y fácil extensión de componentes.

## Estructura del proyecto
- `main.py`: Punto de entrada principal. Maneja el ciclo de vida del cliente y el bucle interactivo.
- `app/`: Lógica principal y componentes del sistema.
  - `config/`: Configuración global y parámetros.
  - `core/`: Motores de decisión, contexto, enrutadores y gestores de estado.
  - `llm/`: Integración con modelos de lenguaje.
  - `memory/`: Implementaciones de memoria a corto y largo plazo.
  - `schemas/`: Esquemas de datos.
  - `tools/`: Herramientas ejecutables por el agente.
- `memory_data/`: Almacenamiento de historial y datos persistentes.
- `tests/`: Pruebas unitarias y de integración.
- `requirements.txt`: Dependencias del proyecto.

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura los parámetros en `app/config/settings.py` según tu entorno.

## Uso
Ejecuta el cliente con:
```bash
python main.py
```

Sigue las instrucciones en pantalla. Puedes escribir mensajes, usar comandos especiales como `exit` para salir o `clear` para limpiar la memoria.

## Extensión y personalización
- Agrega nuevas herramientas en `app/tools/`.
- Implementa nuevos proveedores LLM en `app/llm/`.
- Ajusta la lógica de decisión en `app/core/decision_engine.py`.

## Licencia
MIT

---

Desarrollado para facilitar la interacción avanzada con servidores MCP y flujos conversacionales inteligentes.