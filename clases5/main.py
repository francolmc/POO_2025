from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def open_connection(self, port: int, user: str, password: str):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def ejcutar_sql(self, sql: str):
        pass

class MySQL(BaseDatos):
    def open_connection(self, port, user, password):
        # Me conectare a un base de datos mysql
        return port, user, password
    
    def ejcutar_sql(self, sql):
        return sql
    
    def close_connection(self):
        # Cerrare la conexion de MySQL
        pass

class Oracle(BaseDatos):
    def open_connection(self, port, user, password):
        # Me conectare a un base de datos Oracle
        return port, user, password
    
    def ejcutar_sql(self, sql):
        return sql
    
    def close_connection(self):
        # Cerrare la conexion de Oracle
        pass

mysql: BaseDatos = MySQL()

mysql.op