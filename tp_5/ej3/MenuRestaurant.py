from Plato import Plato

class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def ejecutar(self):
        while True:
            nombre_plato = input("Ingrese el nombre del plato: ")
            precio = float(input("Ingrese el precio del plato: "))
            es_bebida = input("¿Es bebida? (SI/NO): ").upper() == "SI"
            plato = Plato(nombre_plato, precio, es_bebida)

            if not es_bebida:
                while True:
                    nombre_ing = input("Ingrese nombre del ingrediente: ")
                    cantidad = float(input("Ingrese cantidad del ingrediente: "))
                    unidad = input("Ingrese unidad de medida: ")
                    plato.agregar_ingrediente(nombre_ing, cantidad, unidad)

                    salir_ing = input("¿Desea salir de la carga de ingredientes? (SI/NO): ")
                    if salir_ing.upper() == 'SI':
                        break

            self.platos_menu.append(plato)
            salir_platos = input("¿Desea salir de la carga de platos? (SI/NO): ")
            if salir_platos.upper() == 'SI':
                break

        self.mostrar_menu()

    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platos_menu:
            print(f"{plato.nombre_completo}")
            print(f"Precio: $ {plato.precio}")
            if not plato.es_bebida:
                print("Ingredientes:")
                for ingrediente in plato.ingredientes:
                    print(f"{ingrediente.nombre} {ingrediente.cantidad} {ingrediente.unidad}")
            print("----------------------------------")
