# -*- coding: utf-8 -*-

import mysql.connector
import random

class Cliente:
    objetos = []

    def __init__(self, **kwargs):
        self.id = int(kwargs['id'])
        self.nombre = kwargs['nombre']
        self.apellidos = kwargs['apellidos']
        self.sexo = kwargs['sexo']
        self.email = kwargs['email']
        self.telefono = kwargs['telefono']
        self.direccion = kwargs['direccion']
        self.ciudad = kwargs['ciudad']
        self.pais = kwargs['pais']
        Cliente.objetos.append(self)

    def __repr__(self):
        return f'Cliente(id={repr(self.id)}, nombre={repr(self.nombre)}, apellidos={repr(self.apellidos)})'

    # Métodos de clase

    @classmethod
    def cargar_datos(cls):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()

        for row in rows:
            Cliente(**{
                'id': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'sexo': row[3],
                'email': row[4],
                'telefono': row[5],
                'direccion': row[6],
                'ciudad': row[7],
                'pais': row[8]
            })

        cursor.close()
        connection.close()

    @classmethod
    def todos(cls):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        for row in rows:
            yield Cliente(**{
                'id': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'sexo': row[3],
                'email': row[4],
                'telefono': row[5],
                'direccion': row[6],
                'ciudad': row[7],
                'pais': row[8]
            })

    @classmethod
    def buscar(cls, id):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        select_query = "SELECT * FROM clientes WHERE id = %s"
        values = (id,)

        cursor.execute(select_query, values)
        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:
            return Cliente(**{
                'id': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'sexo': row[3],
                'email': row[4],
                'telefono': row[5],
                'direccion': row[6],
                'ciudad': row[7],
                'pais': row[8]
            })
        else:
            return None

    @classmethod
    def filtrar(cls, **kwargs):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        select_query = "SELECT * FROM clientes WHERE "
        conditions = []
        values = []

        for key, value in kwargs.items():
            conditions.append(f"{key} = %s")
            values.append(value)

        select_query += " AND ".join(conditions)

        cursor.execute(select_query, values)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        for row in rows:
            yield Cliente(**{
                'id': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'sexo': row[3],
                'email': row[4],
                'telefono': row[5],
                'direccion': row[6],
                'ciudad': row[7],
                'pais': row[8]
            })

    @classmethod
    def nuevo(cls, **kwargs):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO clientes (nombre, apellidos, sexo, email, telefono, direccion, ciudad, pais) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            kwargs['nombre'],
            kwargs['apellidos'],
            kwargs['sexo'],
            kwargs['email'],
            kwargs['telefono'],
            kwargs['direccion'],
            kwargs['ciudad'],
            kwargs['pais']
        )

        cursor.execute(insert_query, values)
        connection.commit()

        cursor.close()
        connection.close()

    @classmethod
    def eliminar(cls, id):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        delete_query = "DELETE FROM clientes WHERE id = %s"
        values = (id,)

        cursor.execute(delete_query, values)
        connection.commit()

        cursor.close()
        connection.close()

    @classmethod
    def editar(cls, id, **kwargs):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        update_query = "UPDATE clientes SET nombre = %s, apellidos = %s, sexo = %s, email = %s, telefono = %s, direccion = %s, ciudad = %s, pais = %s WHERE id = %s"
        values = (
            kwargs['nombre'],
            kwargs['apellidos'],
            kwargs['sexo'],
            kwargs['email'],
            kwargs['telefono'],
            kwargs['direccion'],
            kwargs['ciudad'],
            kwargs['pais'],
            id
        )

        cursor.execute(update_query, values)
        connection.commit()

        cursor.close()
        connection.close()

# Configuración de conexión a la base de datos
db_config = {
    'host': '127.0.0.1',
    'user': 'afd',
    'password': 'afd',
    'database': 'clientes'
}

# Cargar datos al iniciar la aplicación
Cliente.cargar_datos()
