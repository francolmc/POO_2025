# importar la clase abstracta Connection
from .Connection import Connection
import sqlite3

# Crear clase connectionSQLite que herede de Connection
class ConnectionSQLite(Connection):
    def __init__(self):
        self.connection = None

    def connect(self, host: str, port: int = 0, user: str = "", password: str = ""):
        self.connection = sqlite3.connect(host)

    def close_connection(self):
        self.connection.close()

    def fetch_all(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def fetch_one(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()
    
    def execute_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()