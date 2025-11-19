from abc import ABC, abstractmethod

class Connection(ABC):
    # TODO: Creacion de la conexion
    @abstractmethod
    def connect(self, host: str, port: int = 0, user: str = "", password: str = ""):
        pass

    # TODO: Cierre de la conexion
    @abstractmethod
    def close_connection(self):
        pass

    # TODO: Obtener varios registros
    @abstractmethod
    def fetch_all(self, query: str):
        pass
    
    # TODO: Obtener un solo registro
    @abstractmethod
    def fetch_one(self, query: str):
        pass
    
    # TODO: Modificar registros
    @abstractmethod
    def execute_query(self, query: str):
        pass
