import re

class Product():
    def __init__(self, id: str, name: str, price: float) -> None:
        self.product_id: str = id
        self.barcode: str = ""
        self.name: str = name
        self.description: str = ""
        self.price: float = price
        self.__stock: int = 0

    def set_stock(self, stock: int) -> None:
        if stock != 0:
            # Esto acepta tanto aumentos como disminuciones de stock
            if self.__stock + stock >= 0:
                self.__stock = self.__stock + stock
            else:
                raise ValueError("Insufficient stock")
        else:
            raise ValueError("Stock cannot be zero")
    
    def get_stock(self) -> int:
        return self.__stock
    
    def check_stock(self, quantity: int) -> bool:
        if quantity <= self.__stock:
            return True
        else:
            return False
        
class Customer():
    def __init__(self) -> None:
        self.name: str = ""
        self.email: str = ""
        self.__phone: str = ""
        self.__rut: str = ""
        self.address: str = ""

    def is_valid_phone(self, phone: str) -> bool:
        pattern = r'^\+569\d{8}$'
        if re.fullmatch(pattern, phone):
            return True
        else:
            return False

    def set_phone(self, phone: str) -> None:
        if self.is_valid_phone(phone):
            self.__phone = phone
        else:
            raise ValueError("Invalid phone number format. Expected format: +569XXXXXXXX")

    def get_phone(self) -> str:
        return self.__phone

    def set_rut(self, rut: str) -> None:
        self.__rut = rut

    def get_rut(self) -> str:
        return self.__rut
