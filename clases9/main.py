import sqlite3

# Crear conexion a la base de datos SQLite
connection = sqlite3.connect("shopping_cart.db")

# Crear un cursor
cursor = connection.cursor()

# Este caso es para obtener muchos registros
cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(f"ID: {product[0]}, Nombre: {product[1]}, Precio: {product[2]}, Cantidad: {product[3]}")

# Este caso es para obtener un registro
cursor.execute("SELECT * FROM products WHERE id = '1'")

product = cursor.fetchone()

print(product)

connection.close()