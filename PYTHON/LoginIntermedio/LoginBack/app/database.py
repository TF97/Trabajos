import os
import mysql.connector
from flask import g
from dotenv import load_dotenv


# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Configuración de la base de datos
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'port': os.getenv('DB_PORT')
}

# Función para obtener la conexión a la base de datos
#def get_db():
      #if 'db' not in g:
           #g.db=mysql.connector.connect(**DATABASE_CONFIG)
    
      #return g.db

def get_db():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(**DATABASE_CONFIG)
            cursor = g.db.cursor()
            cursor.execute("USE basica")
            print("Conexión a la base de datos y selección de base de datos exitosa")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
    return g.db


# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Eliminar la conexión de 'g' si existe
    db = g.pop('db', None)
    # Si había una conexión, cerrarla
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de datos
def init_app(app):
    # Registrar la función 'close_db' para ser llamada al final del contexto de la aplicación
    app.teardown_appcontext(close_db)
