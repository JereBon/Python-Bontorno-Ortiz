
cadena = str((input("Ingrese una cadena de texto:")))
while True:   
    print("Opciones:")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    elecion = str(input("Elija una opcion (1 o 2): "))

    if elecion == "1":
        print(cadena.upper())
        break

    elif elecion == "2":
        print(cadena.lower())
        break

    else:
        print("Opcion no valida")