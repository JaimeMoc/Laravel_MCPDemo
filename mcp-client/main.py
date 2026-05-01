import sys
from app.config.settings import settings
from app.core.context_manager import ContextManager
from app.core.decision_engine import DecisionEngine
from app.core.llm_router import LLMRouter
from app.core.tool_router import ToolRouter
from app.core.state_manager import StateManager
from app.memory.short_term_memory import ShortTermMemory
from app.memory.long_term_memory import LongTermMemory

# Muestra información de arranque de la aplicación.
def print_startup_info():
    """
    Print application startup configuration.
    """

    print("\n===== MCP CLIENT STARTED =====")

    print(f"MCP Server URL: {settings.mcp_server_url}")
    print(f"LLM Provider: {settings.llm_provider}")

    if settings.llm_provider == "gemini":
        print(f"Gemini Model: {settings.gemini_model}")

    elif settings.llm_provider == "ollama":
        print(f"Ollama Model: {settings.ollama_model}")

    print("===============================\n")

# Inicializa todos los componentes del sistema.
def create_system_components():
    """
    Initialize all system components.
    """

    context_manager = ContextManager()
    decision_engine = DecisionEngine()
    llm_router = LLMRouter()
    tool_router = ToolRouter()
    state_manager = StateManager()
    short_memory = ShortTermMemory()
    long_memory = LongTermMemory()

    return {
        "context": context_manager,
        "decision": decision_engine,
        "llm": llm_router,
        "tool": tool_router,
        "state": state_manager,
        "short_memory": short_memory,
        "long_memory": long_memory
    }

# Núcleo del flujo conversacional: procesa la entrada del usuario, decide acciones, ejecuta herramientas o LLM, y actualiza el contexto y memoria.
def process_user_input(user_input, components):
    """
    Process a single user input.
    """

    context_manager = components["context"]
    decision_engine = components["decision"]
    llm_router = components["llm"]
    tool_router = components["tool"]
    short_memory = components["short_memory"]
    long_memory = components["long_memory"]

    # Agregar el mensaje del usuario a la memoria y contexto
    short_memory.add("user", user_input)
    long_memory.add("user", user_input)
    context_manager.add_user_message(user_input)

    # Decide la acción a tomar (usar herramienta o LLM)
    decision = decision_engine.decide(user_input)
    tool_result = None

    # Ejecutar herramienta o LLM según la decisión
    if decision["use_tool"]:

        tool_name = decision["tool_name"]

        print(f"[Tool Execution] → {tool_name}")

        tool_result = tool_router.execute(
            tool_name=tool_name,
            payload={}
        )

        assistant_message = str(tool_result)

    else:

        # Usar el LLM para generar la respuesta, proporcionando el contexto actual
        context = context_manager.get_context()

        assistant_message = llm_router.generate(
            prompt=user_input,
            context=context
        )

    # Guardar la respuesta del asistente en la memoria y contexto
    short_memory.add("assistant", assistant_message)
    long_memory.add("assistant", assistant_message)

    context_manager.add_assistant_message(
        assistant_message
    )

    return assistant_message

# Bucle interactivo principal para la CLI. Permite al usuario ingresar mensajes, procesa la entrada, y muestra las respuestas del LLM o herramientas
def interactive_loop(components):
    """
    Interactive CLI loop.
    """

    print("Type 'exit' to quit.")
    print("Type 'clear' to reset memory.\n")

    while True:

        try:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting MCP Client.")
                break

            if user_input.lower() == "clear":
                components["short_memory"].clear()
                components["context"].clear()

                print("Memory cleared.\n")
                continue

            if not user_input.strip():
                continue

            response = process_user_input(
                user_input,
                components
            )

            print(f"LLM: {response}\n")

        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break

        except Exception as e:
            print(f"Error: {str(e)}")

# Punto de entrada principal de la aplicación.
def main():
    """
    Main application entry point.
    """

    try:
        print_startup_info()
        components = create_system_components()
        interactive_loop(components)

    except Exception as e:

        print("Fatal error starting MCP Client:")
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()