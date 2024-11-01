from Computadora import Computadora

class CostoComputadora:
    def __init__(self):
        self.computadoras = []

    def ejecutar(self):
        while True:
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo de la computadora: ")
            computadora = Computadora(marca, modelo)

            while True:
                componente = input("Ingrese el componente (ej. Memoria RAM 2Gb): ")
                marca_componente = input("Ingrese la marca del componente: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio por unidad: "))
                computadora.agregar_componente(componente, marca_componente, cantidad, precio)

                salir_componentes = input("¿Desea salir de la carga de componentes? (SI/NO): ")
                if salir_componentes.upper() == 'SI':
                    break

            self.computadoras.append(computadora)
            self.mostrar_informacion(computadora)

            nueva_cotizacion = input("¿Desea cotizar una nueva computadora? (SI/NO): ")
            if nueva_cotizacion.upper() == 'NO':
                break

    def mostrar_informacion(self, computadora):
        print(f"\n-----------Computadora----------------")
        print(f"Marca: {computadora.marca}")
        print(f"Modelo: {computadora.modelo}")
        print("Componentes:")
        for componente in computadora.componentes:
            subtotal = componente.calcular_subtotal()
            print(f"{componente.componente} {componente.marca} {componente.cantidad} unidades - ${componente.precio} c/u - Subtotal: ${subtotal}")
        costo_total = computadora.calcular_costo_total()
        precio_sugerido = computadora.calcular_precio_sugerido()
        print(f"Costo Total: ${costo_total}")
        print(f"Precio sugerido de venta: ${precio_sugerido}")
        print("--------------------------------------")
