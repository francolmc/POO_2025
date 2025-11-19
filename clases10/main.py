from database.ConnectionSQLite import ConnectionSQLite
from database.ConnectionMySQL import ConnectionMySQL
from repositories.ProductRepository import ProductRepository

conn = ConnectionSQLite()
conn2 = ConnectionMySQL()
repository = ProductRepository(conn2)