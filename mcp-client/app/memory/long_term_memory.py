import mysql.connector
from app.config.settings import settings
import os

# Clase que implementa la memoria a largo plazo persistente.
class LongTermMemory:
    """
    Persistent long-term memory.

    Stores conversation history to disk.
    """

    def __init__(self):
        self.db_config = {
            'user': os.getenv('MYSQL_USER', 'root'),
            'password': os.getenv('MYSQL_PASSWORD', ''),
            'host': os.getenv('MYSQL_HOST', 'localhost'),
            'database': os.getenv('MYSQL_DATABASE', 'LongMemory'),
        }
        self._ensure_table()

    # Método para agregar un mensaje al historial de conversaciones, especificando el rol (por ejemplo, "user" o "assistant") y el contenido del mensaje
    def add(self, role: str, content: str):
        """
        Add message to persistent memory (MySQL).
        """
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversation_history (role, content) VALUES (%s, %s)",
            (role, content)
        )
        conn.commit()
        cursor.close()
        conn.close()

    # Método para recuperar todo el historial de conversaciones almacenado en la memoria a largo plazo
    def get_all(self):
        """
        Retrieve all stored messages from MySQL.
        """
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT role, content FROM conversation_history ORDER BY id ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    # Método para borrar todo el historial de conversaciones almacenado en la memoria a largo plazo
    def clear(self):
        """
        Clear stored memory in MySQL.
        """
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conversation_history")
        conn.commit()
        cursor.close()
        conn.close()

    # Métodos de archivo eliminados, ya no se usan con MySQL

    def _ensure_table(self):
        """
        Ensure the conversation_history table exists in MySQL.
        """
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversation_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                role VARCHAR(32) NOT NULL,
                content TEXT NOT NULL
            )
            """
        )
        conn.commit()
        cursor.close()
        conn.close()