# Clase para gestionar el estado global de la aplicación.
class StateManager:
    """
    Manages global application state.
    """

   # Método de inicialización que crea un diccionario vacío para almacenar el estado. 
    def __init__(self):
        self.state = {}

    # Método para establecer un valor en el estado utilizando una clave.
    def set(self, key: str, value):
        """
        Set state value.
        """
        self.state[key] = value

    # Método para obtener un valor del estado utilizando una clave, con la opción de proporcionar un valor predeterminado si la clave no existe.
    def get(self, key: str, default=None):
        """
        Get state value.
        """
        return self.state.get(key, default)

    # Método para borrar un valor del estado utilizando una clave.
    def clear(self):
        """
        Clear state.
        """
        self.state = {}

    # Método para devolver todo el estado actual como un diccionario.
    def all(self):
        """
        Return all state.
        """
        return self.state