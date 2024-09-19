def recursion(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return recursion(cadena[1:]) + cadena[0]
  
cadena = input("Ingrese una cadena de texto para invertirla: ")
cadenaInv = recursion(cadena)
print(cadenaInv)