from database.Connection import Connection
from repositories.ProductRepository import ProductRepository
from models.Product import Product

class ProductService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.repository = ProductRepository(self.connection)

    def create_product(self, name: str, price: float, quantity: int):
        new_product = Product()
        new_product.name = name
        new_product.price = price
        new_product.quantity = quantity
        self.repository.create_product(new_product)

    def get_all_products(self) -> list[Product]:
        return self.repository.find_products_by_name("")