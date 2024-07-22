
from app.views import get_all_usuarios, get_usuarios_por_nombre, create_usuario, get_usuario, update_usuario, delete_usuario, search_usuarios, login
from app.database import init_app, get_db
import logging
from flask import Flask
from flask_cors import CORS  # Asegúrate de que CORS esté importado

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configura el nivel de logging
logging.basicConfig(level=logging.DEBUG)

# Creación de la instancia de Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Habilitar CORS para todas las rutas
CORS(app)

# Inicialización de la aplicación con manejo de base de datos
init_app(app)

# Asegúrate de que el código que necesita el contexto de la aplicación esté dentro de app.app_context()
with app.app_context():
    try:
        db_connection = get_db()  # Conectar a la base de datos
        logging.debug('Conexión exitosa a la base de datos')
    except Exception as e:
        logging.error(f'Error al conectar a la base de datos: {str(e)}')

# Asociación de rutas con vistas usando decoradores
@app.route('/api/usuarios/', methods=['GET'])
def route_get_all_usuarios():
    return get_all_usuarios()

@app.route('/api/usuarios/', methods=['POST'])
def route_create_usuario():
    return create_usuario()

@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def route_get_usuario(usuario_id):
    return get_usuario(usuario_id)

@app.route('/api/usuarios/nombre', methods=['GET'])
def route_get_usuarios_por_nombre():
    return get_usuarios_por_nombre()

@app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def route_update_usuario(usuario_id):
    return update_usuario(usuario_id)

@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def route_delete_usuario(usuario_id):
    return delete_usuario(usuario_id)

@app.route('/usuarios/search', methods=['GET'])
def search_for_usuarios():
    return search_usuarios()

# Ruta para login
@app.route('/usuarios/login', methods=['POST'])
def route_login():
    return login()

# Ruta de prueba para asegurar que la aplicación está corriendo
@app.route('/')
def index():
    return 'Hello, Flask!'

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)