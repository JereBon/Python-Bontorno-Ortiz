from Nota import Nota

class Alumno:
    def __init__(self, nombre_completo, legajo):
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, catedra, nota_examen):
        nueva_nota = Nota(catedra, nota_examen)
        self.notas.append(nueva_nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.nota_examen for nota in self.notas)
        return total / len(self.notas)
    