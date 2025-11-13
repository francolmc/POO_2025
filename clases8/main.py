import sqlite3

# Crear conexion a la base de datos SQLite
connection = sqlite3.connect("shopping_cart.db")

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Ejecutar una consulta para crear una tabla de productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

# Insertar un producto
cursor.execute('''
    INSERT INTO products (name, price, quantity)
    VALUES ('Laptop Maquintoch 🍏', 999.99, 10)
''')

connection.commit()

connection.close()