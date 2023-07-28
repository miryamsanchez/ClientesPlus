# -*- coding: utf-8 -*-

import csv

class Cliente:
    objetos = [] # Lista para almacenar las instancias del cliente, las instancias te permiten trabajar individualmente con cada cliente

    def __init__(self, **kwargs): #kwargs es un diccionario que contiene los argumentos con nombre proporcionados al crear una instancia cliente. 
        self.id = int(kwargs['id'])#Inicializa el atributo "id" con el valor proporcinado en kwargs id convirtiendolo a entero
        self.nombre = kwargs['nombre']
        self.apellidos = kwargs['apellidos']
        self.sexo = kwargs['sexo']
        self.email = kwargs['email']
        self.telefono = kwargs['telefono']
        self.direccion = kwargs['direccion']
        self.ciudad = kwargs['ciudad']
        self.pais = kwargs['pais']
        Cliente.objetos.append(self) #Agrega la instancia actual de Cliente a la lista de 'objetos'

    def __repr__(self):
        return f'Cliente(id={repr(self.id)}, nombre={repr(self.nombre)}, apellidos={repr(self.nombre)})'

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    @classmethod
    def cargar_datos(cls, archivo):
        with open(archivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Cliente(**row)

    @classmethod
    def todos(cls):
        for cliente in cls.objetos:
            yield cliente
    
    @classmethod
    def buscar(cls, id):
        for cliente in cls.objetos:
            if cliente.id == id:
                return cliente
        return None

    @classmethod
    def filtrar(cls, **kwargs):
        resultado = []
        for cliente in cls.objetos:
            if all(getattr(cliente, k) == v for k, v in kwargs.items()):
                yield cliente
    
      
                
    