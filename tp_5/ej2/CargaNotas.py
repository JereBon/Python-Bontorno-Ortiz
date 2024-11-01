from Alumno import Alumno

class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def ejecutar(self):
        while True:
            nombre_completo = input("Ingrese nombre completo del alumno: ")
            legajo = int(input("Ingrese legajo del alumno: "))
            alumno = Alumno(nombre_completo, legajo)
            
            while True:
                catedra = input("Ingrese nombre de la cátedra: ")
                nota_examen = float(input("Ingrese nota: "))
                alumno.agregar_nota(catedra, nota_examen)
                
                salir_notas = input("¿Desea salir de la carga de notas? (SI/NO): ")
                if salir_notas.upper() == 'SI':
                    break

            self.alumnos.append(alumno)
            salir_alumnos = input("¿Desea salir de la carga de alumnos? (SI/NO): ")
            if salir_alumnos.upper() == 'SI':
                break

        self.mostrar_informacion()

    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre_completo}, Legajo: {alumno.legajo}")
            for nota in alumno.notas:
                print(f" - Cátedra: {nota.catedra}, Nota: {nota.nota_examen}")
            print(f"Promedio: {alumno.calcular_promedio()}")