import re
from datetime import datetime

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

class Item():
    def __init__(self) -> None:
        self.product: Product = None
        self.__quantity: int = 0

    def set_quantity(self, quantity: int) -> None:
        if quantity > 0:
            self.__quantity = quantity
            if not self.product.check_stock(quantity):
                raise ValueError("Insufficient stock for the requested quantity")
        else:
            raise ValueError("Invalid quantity. Quantity must be positive.")
        
    def get_quantity(self) -> int:
        return self.__quantity

    def total(self) -> float:
        return self.product.price * self.__quantity
    
class ShoppingCart():
    def __init__(self, id: int, customer: Customer) -> None:
        self.shopping_cart_id: int = id
        self.customer: Customer = customer
        self.__creation_date: datetime = datetime.now()
        self.__items: list[Item] = []

    def remove_item(self, product_id: str, quantity: int) -> None:
        # Buscar el item en la lista
        item_found: Item = None
        for item in self.__items:
            if item.product.product_id == product_id:
                if item.get_quantity() == quantity:
                    item_found = item

        if item_found is None:
            raise ValueError("Product not found in cart with the specified quantity")
        
        # Remover el item de la lista
        self.__items.remove(item_found)
        # TODO: Retonar la cantidad de productos removidos al stock del producto
        item_found.product.set_stock(quantity)

    def total_price(self) -> float:
        total: float = 0.0
        for item in self.__items:
            total = total + item.total()
        return total

    def add_item(self, product: Product, quantity: int) -> None:
        new_item = Item()
        new_item.product = product
        try:
            new_item.set_quantity(quantity)
        except ValueError as e:
            raise ValueError("Cannot add item to cart: " + str(e))
        self.__items.append(new_item)


    def clear_cart(self) -> None:
        self.__items.clear()

    def get_items(self) -> list[Item]:
        return self.__items

    def pay_shopping_cart(self) -> None:
        pass

# Probar las clases

arroz = Product("1", "Arroz 1K", 1500)
arroz.set_stock(10)

tallarin = Product("2", "Tallarin 1K", 1200)
tallarin.set_stock(5)

pan_pascua = Product("3", "Pan de Pascua", 3000)
pan_pascua.set_stock(2)

pedro = Customer()
pedro.name = "Pedro Perez"
pedro.email = "pedrito@sucorreo.com"
pedro.set_phone("+56912345678")
pedro.set_rut("12.345.678-9")
pedro.address = "Calle Falsa 123"

# Proceso de compra
carro = ShoppingCart(1, pedro)
carro.add_item(arroz, 2)
print(carro.total_price())
carro.clear_cart()
print(carro.get_items())
carro.add_item(pan_pascua, 5)
print(carro.total_price())



# Desarrollar una aplicacion que permita registrar varios clientes en una lista.
# que se pueda buscar port RUT y mostrar sus datos
# modificar o eliminar un cliente de la lista.
# Para hacer mas sencillo el trabajo, se puede mostrar un menu con las opciones
"""
def main() -> None:
    customer_list: list[Customer] = []
    while True:
        print ("MENU DE OPCIONES")
        print ("1. Agregar cliente")
        print ("2. Buscar cliente por RUT")
        print ("3. Modificar cliente por RUT")
        print ("4. Eliminar cliente por RUT")
        print ("5. Mostrar todos los clientes")
        print ("6. Salir")

        option = input ("Seleccione una opción: ")
        if option == "1":
            print ("Agregar cliente")
            customer = Customer()
            customer.name = input ("Ingrese nombre del cliente: ")
            customer.email = input ("Ingrese email del cliente: ")
            customer.set_phone(input ("Ingrese teléfono del cliente (+569XXXXXXXX): "))
            customer.set_rut(input ("Ingrese RUT del cliente: "))
            customer.address = input ("Ingrese dirección del cliente: ")
            customer_list.append(customer)
        elif option == "2":
            print ("Buscar cliente por RUT")
        elif option == "3":
            print ("Modificar cliente por RUT")
        elif option == "4":
            print ("Eliminar cliente por RUT")
        elif option == "5":
            print ("Mostrar todos los clientes")
            for customer in customer_list:
                print (f"Nombre: {customer.name}, Email: {customer.email}, Teléfono: {customer.get_phone()}, RUT: {customer.get_rut()}, Dirección: {customer.address}") 
        elif option == "6":
            print ("Salir")
            break
        else:
            print ("Opción inválida, intente nuevamente")

        
main()
"""

