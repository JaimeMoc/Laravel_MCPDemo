import sys
from app.config.settings import settings
from app.core.context_manager import ContextManager
from app.core.decision_engine import DecisionEngine
from app.core.llm_router import LLMRouter
from app.core.tool_router import ToolRouter
from app.core.state_manager import StateManager
from app.memory.short_term_memory import ShortTermMemory
from app.memory.long_term_memory import LongTermMemory


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

    # Add user message to memory
    short_memory.add("user", user_input)
    long_memory.add("user", user_input)
    context_manager.add_user_message(user_input)

    # Decide action
    decision = decision_engine.decide(user_input)
    tool_result = None

    # Execute tool if needed
    if decision["use_tool"]:

        tool_name = decision["tool_name"]

        print(f"[Tool Execution] → {tool_name}")

        tool_result = tool_router.execute(
            tool_name=tool_name,
            payload={}
        )

        assistant_message = str(tool_result)

    else:

        # Use LLM
        context = context_manager.get_context()

        assistant_message = llm_router.generate(
            prompt=user_input,
            context=context
        )

    # Save assistant message
    short_memory.add("assistant", assistant_message)
    long_memory.add("assistant", assistant_message)

    context_manager.add_assistant_message(
        assistant_message
    )

    return assistant_message

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