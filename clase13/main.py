import sqlite3
import bcrypt

# Funcion para crear la tabla de usuarios
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(email:str, password:str):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Encriptar la contraseña
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute('INSERT INTO usuarios (email, password_hash) VALUES (?, ?)', (email, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print("El usuario ya existe.")
    finally:
        conn.close()

def login_user(email:str, password:str) -> bool:
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('SELECT password_hash FROM usuarios WHERE email = ?', (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        db_password_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), db_password_hash):
            return True
        return False
    return False


print("Inicializando la base de datos...")
init_db()
print("Registrar un usuario")
email = input("Ingrese su email: ")
password = input("Ingrese su contraseña: ")
register_user(email, password)
print("Iniciar sesión")
email = input("Ingrese su email: ")
password = input("Ingrese su contraseña: ")
if login_user(email, password):
    print("Inicio de sesión exitoso.")
else:
    print("Error en el inicio de sesión.")
