from datetime import datetime
from app.database import get_db
import bcrypt 

class Usuario:
    def __init__(self, id_usuario=None, apellido=None, nombre=None, fecha_nacimiento=None, documento=None, telefono=None, email=None, pais_origen=None, password=None):
        self.id_usuario = id_usuario
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento  # Esperamos un string en formato 'YYYY-MM-DD'
        self.documento = documento
        self.telefono = telefono
        self.email = email
        self.pais_origen = pais_origen
        self.password = password

    # Método para borrar un usuario
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (self.id_usuario,))
        db.commit()
        cursor.close()

    # Método para buscar un usuario por id
    @staticmethod
    def get_by_id(usuario_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (usuario_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], fecha_nacimiento=row[3], documento=row[4], telefono=row[5], email=row[6], pais_origen=row[7], password=row[8])
        return None
    
    # Método para buscar un usuario por nombre
    @staticmethod
    def get_by_nombre(nombre):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", (f'%{nombre}%',))
        rows = cursor.fetchall()
        cursor.close()
        usuarios = []
        for row in rows:
            usuarios.append(Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], fecha_nacimiento=row[3], documento=row[4], telefono=row[5], email=row[6], pais_origen=row[7], password=row[8]))
        return usuarios

    # Método para listar todos los usuarios
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], fecha_nacimiento=row[3], documento=row[4], telefono=row[5], email=row[6], pais_origen=row[7], password=row[8]) for row in rows]
        cursor.close()
        return usuarios

    # Método para guardar (crear/actualizar) un usuario
    def save(self):
        db = get_db()
        cursor = db.cursor()
        try:
            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
            if self.id_usuario:
                cursor.execute("""
                    UPDATE usuarios SET apellido = %s, nombre = %s, fecha_nacimiento = %s, documento = %s, telefono = %s, email = %s, pais_origen = %s, password = %s
                    WHERE id_usuario = %s
                """, (self.apellido, self.nombre, self.fecha_nacimiento, self.documento, self.telefono, self.email, self.pais_origen, hashed_password, self.id_usuario))
            else:
                cursor.execute("""
                    INSERT INTO usuarios (apellido, nombre, fecha_nacimiento, documento, telefono, email, pais_origen, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (self.apellido, self.nombre, self.fecha_nacimiento, self.documento, self.telefono, self.email, self.pais_origen, hashed_password))
                self.id_usuario = cursor.lastrowid
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()

    # Método para serializar el objeto Usuario a un diccionario
    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'apellido': self.apellido,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'documento': self.documento,
            'telefono': self.telefono,
            'email': self.email,
            'pais_origen': self.pais_origen,
            'password': self.password
        }
    
    # Función para buscar por documento y contraseña
    @staticmethod
    def get_by_documento_and_password(documento, password):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE documento = %s", (documento,))
        row = cursor.fetchone()
        cursor.close()
        if row and bcrypt.checkpw(password.encode('utf-8'), row[8].encode('utf-8')):
            return Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], fecha_nacimiento=row[3], documento=row[4], telefono=row[5], email=row[6], pais_origen=row[7], password=row[8])
        return None
    
    # Funcion para buscar por documento y nombre
    @staticmethod
    def search(nombre=None, documento=None):
        db = get_db()
        cursor = db.cursor()
        
        # Construir la consulta SQL dinámicamente según los parámetros proporcionados
        query = "SELECT * FROM usuarios WHERE 1=1"
        params = []
        
        if nombre:
            query += " AND nombre LIKE %s"
            params.append(f'%{nombre}%')
        
        if documento:
            query += " AND documento LIKE %s"
            params.append(f'%{documento}%')

        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        
        usuarios = []
        for row in rows:
            usuarios.append(Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], fecha_nacimiento=row[3], documento=row[4], telefono=row[5], email=row[6], pais_origen=row[7], password=row[8]))
        
        return usuarios
