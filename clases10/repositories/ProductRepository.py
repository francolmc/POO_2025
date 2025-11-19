from database.Connection import Connection
from models.Product import Product

class ProductRepository:
    def __init__(self, connection: Connection):
        self.database_connection: Connection = connection
        self.database_connection.connect()

    def create_product(self, product: Product):
        query = f'''
            INSERT INTO products (name, price, quantity)
            VALUES ('{product.name}', {product.price}, {product.quantity})
        '''
        self.database_connection.execute_query(query)

    def get_product_by_id(self, product_id: int) -> Product | None:
        query = f'''
            SELECT id, name, price, quantity
            FROM products
            WHERE id = '{product_id}'
        '''
        product = self.database_connection.fetch_one(query)
        if product:
            product_finded = Product()
            product_finded.id = product[0]
            product_finded.name = product[1]
            product_finded.price = product[2]
            product_finded.quantity = product[3]
            return product_finded
        return None
    
    # TODO: ELiminar producto
    # TODO: Modificar producto
    # TODO: Buscar productos por nombre