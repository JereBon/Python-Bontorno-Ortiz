from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresa_constructora):
        self.nombre = nombre
        self.empresa_constructora = empresa_constructora
        self.viviendas = []

    def agregar_vivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def get_superficie_total_terreno(self):
        return sum(v.superficie_terreno for v in self.viviendas)

    def get_superficie_total_terreno_x_manzana(self, manzana):
        return sum(v.superficie_terreno for v in self.viviendas if v.manzana == manzana)

    def get_superficie_total_cubierta(self):
        return sum(v.get_metros_cuadrados_cubiertos() for v in self.viviendas)
