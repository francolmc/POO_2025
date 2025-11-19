class Product:
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__price = 0.0
        self.__quantity = 0

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__price = value

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__quantity = value
        