def recursion(cadena, index=0):
    if index == len(cadena):
        return
    else:
        print(cadena[index])
        recursion(cadena, index + 1)

texto = str(input("Ingrese una cadena de texto: "))
recursion(texto)