from Celda import Celda

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                print("La celda ya existe.")
                return
        nueva_celda = Celda(fila, columna, valor)
        self.celdasMatriz.append(nueva_celda)

    def mostrar_celdas(self):
        for celda in self.celdasMatriz:
            print(f"Fila: {celda.fila}, Columna: {celda.columna}, Valor: {celda.valor}")

    def obtener_valor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"