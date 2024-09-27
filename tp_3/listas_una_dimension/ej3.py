numeros = input("Ingrese una lista de numeros separados por espacios para invertir su orden: ")
arreglo = [float(num) for num in numeros.split()]
arreglo.reverse()
print(arreglo)