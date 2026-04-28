class DecisionEngine:
    """
    Decides how to process user input.
    """

    def __init__(self):
        pass

    def decide(self, user_input: str) -> dict:
        """
        Decide what action to take.

        Returns:
            dict:
                {
                    "use_tool": bool,
                    "tool_name": str | None,
                    "use_llm": bool
                }
        """

        user_input_lower = user_input.lower()

        # Simple heuristics
        if "tool:" in user_input_lower:
            tool_name = user_input_lower.split("tool:")[1].strip()

            return {
                "use_tool": True,
                "tool_name": tool_name,
                "use_llm": False
            }

        return {
            "use_tool": False,
            "tool_name": None,
            "use_llm": True
        }