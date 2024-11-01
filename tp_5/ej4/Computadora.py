from ComponenteCPU import ComponenteCPU

class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente, marca, cantidad, precio):
        nuevo_componente = ComponenteCPU(componente, marca, cantidad, precio)
        self.componentes.append(nuevo_componente)

    def calcular_costo_total(self):
        return sum(componente.calcular_subtotal() for componente in self.componentes)

    def calcular_precio_sugerido(self):
        costo_total = self.calcular_costo_total()
        if costo_total < 50000:
            return costo_total * 1.4
        else:
            return costo_total * 1.3
