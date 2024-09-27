numeros = input("Ingrese una lista de numeros separados por espacios para multiplicarlos: ")
multi = int(input("Ingrese el numero al cual multiplicar todos los anteriores: "))
arreglo = [int(num) for num in numeros.split()]
resultado = [num * multi for num in arreglo]
print(resultado)