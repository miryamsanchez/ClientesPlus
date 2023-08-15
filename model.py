# -*- coding: utf-8 -*-
from flask import Flask, request
import csv
import sqlite3  # Importa la biblioteca SQLite
DB_NAME = "clientes.db"

app = Flask(__name__)

def crear_tabla():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id TEXT PRIMARY KEY,
            nombre TEXT,
            apellidos TEXT,
            email TEXT,
            telefono TEXT,
            sexo TEXT,
            direccion VARCHAR(30),
            ciudad VARCHAR(30),
            pais VARCHAR(30))
       """)
    con.commit()
    con.close()

# Llamada a la función para crear la tabla
crear_tabla()
    
def detalle_cliente(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        SELECT id, nombre, apellidos, email, telefono, sexo,
        direccion, ciudad, pais FROM clientes 
        WHERE id = ?
    """, (codigo,))
    result = cur.fetchone()#result contiene los atributos
    con.close() 
    if result:
        id, nombre, apellidos, email, telefono, sexo, direccion, ciudad, pais =result
        return {
            'id': id,
            'nombre': nombre,
            'apellidos': apellidos,
            'email': email,
            'telefono': telefono,
            'sexo': sexo,
            'direccion': direccion,
            'ciudad': ciudad,
            'pais': pais
        }
    else:
        return None

def guardar_cliente(datos):
    con = sqlite3.connect(BD_NAME)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO clientes (id, nombre, apellidos, email, telefono, sexo, direccion, ciudad, pais)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (datos['id'], datos['nombre'], datos['apellidos'], datos['email'], datos['telefono'], datos['sexo'], datos['direccion'], datos['ciudad'], datos['pais']))
    con.commit()
    con.close()

def editar_cliente(id, datos):
    con = sqlite3.connect(BD_NAME)
    cur = con.cursor()
    cur.execute("""
        UPDATE clientes SET
        nombre = ?,
        apellidos = ?,
        email = ?,
        telefono = ?,
        sexo = ?,
        direccion = ?,
        ciudad = ?,
        pais = ?
        WHERE id = ?
    """, (datos['nombre'], datos['apellidos'], datos['email'], datos['telefono'], datos['sexo'], datos['direccion'], datos['ciudad'], datos['pais'], id))
    con.commit()
    con.close()

def nuevo_cliente(datos):
    con = sqlite3.connect(BD_NAME)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO clientes (id, nombre, apellidos, email, telefono, sexo, direccion, ciudad, pais)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (datos['id'], datos['nombre'], datos['apellidos'], datos['email'], datos['telefono'], datos['sexo'], datos['direccion'], datos['ciudad'], datos['pais']))
    con.commit()
    con.close()

def eliminar_cliente(id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        DELETE FROM cliente 
        WHERE id = ?
        """, (id))
    con.commit()
    con.close()

# Aquí puedes definir tus rutas de Flask para interactuar con los métodos anteriores
# Por ejemplo, usar request para obtener datos del cliente y llamar a los métodos


# class Cliente:
#     objetos = [] # Lista para almacenar las instancias del cliente, las instancias te permiten trabajar individualmente con cada cliente

#     def __init__(self, **kwargs): #kwargs es un diccionario que contiene los argumentos con nombre proporcionados al crear una instancia cliente. 
#         self.id = int(kwargs['id'])#Inicializa el atributo "id" con el valor proporcinado en kwargs id convirtiendolo a entero
#         self.nombre = kwargs['nombre']
#         self.apellidos = kwargs['apellidos']
#         self.sexo = kwargs['sexo']
#         self.email = kwargs['email']
#         self.telefono = kwargs['telefono']
#         self.direccion = kwargs['direccion']
#         self.ciudad = kwargs['ciudad']
#         self.pais = kwargs['pais']
#         Cliente.objetos.append(self) #Agrega la instancia actual de Cliente a la lista de 'objetos'

#     def __repr__(self):
#         return f'Cliente(id={repr(self.id)}, nombre={repr(self.nombre)}, apellidos={repr(self.nombre)})'

#     def __str__(self):
#         return f'{self.nombre} {self.apellidos}'

#     @classmethod
#     def cargar_datos(cls, archivo):
#         conexion = sqlite3.connect('clientes.db')
#         with open(archivo, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 conexion.execute('''
#                     INSERT INTO clientes (nombre, apellidos, sexo, email, telefono, direccion, ciudad, pais)
#                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#                 ''', (row['nombre'], row['apellidos'], row['sexo'], row['email'], row['telefono'], row['direccion'], row['ciudad'], row['pais']))

#         conexion.commit()
#         conexion.close()

#     @classmethod
#     def todos(cls):
#         for cliente in cls.objetos:
#             yield cliente
    
#     @classmethod
#     def buscar(cls, id):
#         for cliente in cls.objetos:
#             if cliente.id == id:
#                 return cliente
#         return None

#     @classmethod
#     def filtrar(cls, **kwargs):
#         resultado = []
#         for cliente in cls.objetos:
#             if all(getattr(cliente, k) == v for k, v in kwargs.items()):
#                 yield cliente
    
#     # ... (Código existente)

#     @classmethod
#     def nuevo(cls, **kwargs):

#         # Crea una nueva instancia de Cliente con los datos proporcionados en kwargs
#         nuevo_cliente = Cliente(id=random.randint(1000,100000), **kwargs)
#         cls.objetos.append(nuevo_cliente)  # Agrega el nuevo cliente a la lista de objetos


#     @classmethod
#     def eliminar(cls, id):
#         cliente = cls.buscar(id)
#         if cliente:
#             cls.objetos.remove(cliente)
#             return True #Agregamos un retorno para indicar éxito
#         return False  #Retornamos False si el cliente no fue encontrado 
    
#     @classmethod
#     def editar(cls, id, **kwargs):
#         cliente = cls.buscar(id)
#         if cliente:
#             for key, value in kwargs.items():
#                 setattr(cliente, key, value)
      
#     # Establece la conexión con la base de datos y crea la tabla
# conexion = sqlite3.connect('clientes.db')
# conexion.execute('''
#     CREATE TABLE IF NOT EXISTS clientes (
#         id INTEGER PRIMARY KEY,
#         nombre TEXT,
#         apellidos TEXT,
#         sexo TEXT,
#         email TEXT,
#         telefono TEXT,
#         direccion TEXT,
#         ciudad TEXT,
#         pais TEXT
#     )
# ''')
# conexion.commit()
# conexion.close()

# # Ejemplo de uso
# if __name__ == '__main__':
#     Cliente.cargar_datos('datos_clientes.csv')  # Reemplaza 'datos_clientes.csv' con tu archivo CSV
#     # ... (Realiza otras operaciones con la clase Cliente)
              
