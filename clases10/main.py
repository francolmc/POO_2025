from database.ConnectionSQLite import ConnectionSQLite
from services.ProductService import ProductService


connection = ConnectionSQLite("shopping_cart.db")
connection.connect()

product_service = ProductService(connection)
# Crear un nuevo producto
product_service.create_product("Laptop", 1200000, 6)

product_list = product_service.get_all_products()

for product in product_list:
    print(f"Nomre: {product.name}, Precio: {product.price}, Cantidad: {product.quantity}")

connection.close_connection()