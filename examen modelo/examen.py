golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "CCCDDD", "2020")

golosinasPedidas = []

def pedir_golosina():
    legajo = int(input("Ingrese su legajo: "))
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return
    
    codigo = int(input("Ingrese el código de la golosina: "))
    for golosina in golosinas:
        if golosina[0] == codigo:
            if golosina[2] <= 0:
                print(f"Lo sentimos la golosina {golosina[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir")
                return
            golosina[2] -= 1
            
            encontrado = False
            for pedido in golosinasPedidas:
                if pedido[0] == codigo:
                    pedido[2] += 1
                    encontrado = True
                    break
            if not encontrado:
                golosinasPedidas.append([codigo, golosina[1], 1])
            break

def mostrar_golosinas():
    for golosina in golosinas:
        print(f"Código: {golosina[0]}, {golosina[1]}, Stock: {golosina[2]}")

def rellenar_golosinas():
    clave1 = input("Ingrese primera clave: ")
    clave2 = input("Ingrese segunda clave: ")
    clave3 = input("Ingrese tercera clave: ")
    
    if (clave1, clave2, clave3) == clavesTecnico:
        codigo = int(input("Ingrese el código de la golosina: "))
        cantidad = int(input("Ingrese la cantidad a recargar: "))
        
        if cantidad > 0:
            for golosina in golosinas:
                if golosina[0] == codigo:
                    golosina[2] += cantidad
                    break
    else:
        print("No tiene permiso para ejecutar la función de recarga")

def apagar_maquina():
    print("\nGolosinas pedidas:")
    total = 0
    for pedido in golosinasPedidas:
        print(f"Código: {pedido[0]}, {pedido[1]}, Cantidad: {pedido[2]}")
        total += pedido[2]
    print(f"Total de golosinas pedidas: {total}")
    return True

def mostrar_menu():
    print("\nMenú:")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar máquina")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            pedir_golosina()
        elif opcion == "b":
            mostrar_golosinas()
        elif opcion == "c":
            rellenar_golosinas()
        elif opcion == "d":
            if apagar_maquina():
                break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()