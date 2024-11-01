from Barrio import Barrio
from Vivienda import Vivienda

def main():
    nombre_barrio = input("Ingrese el nombre del barrio: ")
    empresa_constructora = input("Ingrese la empresa constructora: ")
    barrio = Barrio(nombre_barrio, empresa_constructora)

    while True:
        calle = input("Ingrese la calle de la vivienda: ")
        numero = int(input("Ingrese el número de la vivienda: "))
        manzana = input("Ingrese la manzana: ")
        nro_casa = int(input("Ingrese el número de casa: "))
        superficie_terreno = float(input("Ingrese la superficie del terreno: "))
        vivienda = Vivienda(calle, numero, manzana, nro_casa, superficie_terreno)

        while True:
            nombre_habitacion = input("Ingrese el nombre de la habitación: ")
            metros_cuadrados = float(input("Ingrese los metros cuadrados de la habitación: "))
            vivienda.agregar_habitacion(nombre_habitacion, metros_cuadrados)

            salir_habitaciones = input("¿Desea salir de la carga de habitaciones? (SI/NO): ")
            if salir_habitaciones.upper() == 'SI':
                break

        barrio.agregar_vivienda(vivienda)

        salir_viviendas = input("¿Desea salir de la carga de viviendas? (SI/NO): ")
        if salir_viviendas.upper() == 'SI':
            break

    print(f"Superficie total del terreno del barrio: {barrio.get_superficie_total_terreno()}")
    manzana_consulta = input("Ingrese la manzana para consultar la superficie: ")
    print(f"Superficie total de la manzana {manzana_consulta}: {barrio.get_superficie_total_terreno_x_manzana(manzana_consulta)}")
    print(f"Superficie total cubierta del barrio: {barrio.get_superficie_total_cubierta()}")

if __name__ == "__main__":
    main()
