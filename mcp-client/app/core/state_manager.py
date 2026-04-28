class StateManager:
    """
    Manages global application state.
    """

    def __init__(self):
        self.state = {}

    def set(self, key: str, value):
        """
        Set state value.
        """
        self.state[key] = value

    def get(self, key: str, default=None):
        """
        Get state value.
        """
        return self.state.get(key, default)

    def clear(self):
        """
        Clear state.
        """
        self.state = {}

    def all(self):
        """
        Return all state.
        """
        return self.state