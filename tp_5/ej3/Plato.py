from Ingrediente import Ingrediente

class Plato:
    def __init__(self, nombre_completo, precio, es_bebida):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, nombre, cantidad, unidad):
        ingrediente = Ingrediente(nombre, cantidad, unidad)
        self.ingredientes.append(ingrediente)