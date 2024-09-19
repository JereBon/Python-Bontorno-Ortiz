def recursion(cadena):
    if len(cadena) == 0:
        return cadena  # Caso base
    else:
        return recursion(cadena[1:]) + cadena[0]  # Concatenar el primer carácter al final

cadena = input("Ingrese una cadena de texto para invertirla: ")
cadena_invertida = recursion(cadena)  # Obtener la cadena invertida
print(cadena_invertida)  # Imprimir la cadena invertida