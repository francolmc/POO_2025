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
    def delete_product(self, product_id: int) -> None:
        query = f'''
            DELETE FROM products
            WHERE id = '{product_id}'
        '''
        self.database_connection.execute_query(query)
    
    # TODO: Modificar producto
    def update_product(self, product: Product) -> None:
        query = f'''
            UPDATE products
            SET name = '{product.name}', price = '{product.price}', quantity = '{product.quantity}'
            WHERE id = '{product.id}'
        '''
        self.database_connection.execute_query(query)

    # TODO: Buscar productos por nombre
    def find_products_by_name(self, name: str) -> list[Product]:
        query = f'''
            SELECT id, name, price, quantity
            FROM products
            WHERE name LIKE '%{name}%'
        '''
        products_data = self.database_connection.fetch_all(query)
        products = []
        for product_data in products_data:
            product = Product()
            product.id = product_data[0]
            product.name = product_data[1]
            product.price = product_data[2]
            product.quantity = product_data[3]
            products.append(product)
            
        return products