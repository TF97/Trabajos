import bcrypt
from app.models import Usuario
from flask import jsonify, request
import logging
def index():
    response = {}
    return jsonify(response)

# Traer todos los usuarios
def get_all_usuarios():
    usuarios = Usuario.get_all()
    return jsonify([usuario.serialize() for usuario in usuarios])

# Traer un usuario por id
def get_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    return jsonify(usuario.serialize())

# Traer un usuario por nombre
def get_usuarios_por_nombre():
    nombre = request.args.get('nombre', '')
    if not nombre:
        return jsonify({'message': 'Nombre is required'}), 400

    usuarios = Usuario.get_by_nombre(nombre)
    if not usuarios:
        return jsonify({'message': 'No users found'}), 404

    return jsonify([usuario.serialize() for usuario in usuarios])

# Crear un usuario
def create_usuario():
    data = request.json
    new_usuario = Usuario(
        apellido=data['apellido'], nombre=data['nombre'],
        fecha_nacimiento=data['fecha_nacimiento'], documento=data['documento'],
        telefono=data['telefono'], email=data['email'], pais_origen=data['pais_origen'],
        password=data['password']
    )
    new_usuario.save()
    return jsonify({'message': 'Usuario created successfully'}), 201

# Actualizar usuario
def update_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    data = request.json
    usuario.apellido = data['apellido']
    usuario.nombre = data['nombre']
    usuario.fecha_nacimiento = data['fecha_nacimiento']
    usuario.documento = data['documento']
    usuario.telefono = data['telefono']
    usuario.email = data['email']
    usuario.pais_origen = data['pais_origen']
    usuario.password = data['password']
    usuario.save()
    return jsonify({'message': 'Usuario updated successfully'})

# Eliminar un usuario
def delete_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    usuario.delete()
    return jsonify({'message': 'Usuario deleted successfully'})

# Buscar usuarios por nombre y/o documento
def search_usuarios():
    nombre = request.args.get('nombre', '')
    documento = request.args.get('documento', '')

    usuarios = []
    if nombre:
        usuarios += Usuario.get_by_nombre(nombre)
    if documento:
        usuarios += Usuario.get_by_documento(documento)

    # Eliminar duplicados si ambos criterios devolvieron resultados
    usuarios = list({usuario.id_usuario: usuario for usuario in usuarios}.values())

    if not usuarios:
        return jsonify({'message': 'No users found'}), 404

    return jsonify([usuario.serialize() for usuario in usuarios])

def login():
    try:
        data = request.get_json()
        documento = data.get('documento')
        password = data.get('password')
        
        if not documento or not password:
            return jsonify({"message": "Documento y contraseña son requeridos"}), 400
        
        usuario = Usuario.query.filter_by(documento=documento).first()
        
        if usuario and bcrypt.check_password_hash(usuario.password, password):
            return jsonify({"message": f"Bienvenido al sistema, {usuario.nombre}"}), 200
        else:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401
    except Exception as e:
        logging.error(f"Error en el login: {str(e)}")
        return jsonify({"message": "Internal Server Error"}), 500