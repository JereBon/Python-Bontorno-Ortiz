numeros = input("Ingrese una lista de numeros separados por espacios para eliminar los duplicados: ")
arreglo = [int(num) for num in numeros.split()]
arreglo = set(arreglo)
print(arreglo)