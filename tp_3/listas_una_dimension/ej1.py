numeros = input("Ingrese elementos para sumar separados por espacios: ")
arreglo = [float(num) for num in numeros.split()]
print(f"El resultado de la suma es: {sum(arreglo)}")