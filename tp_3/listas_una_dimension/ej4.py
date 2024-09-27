numeros = input("Ingrese una lista de numeros separados por espacios para contar cuantos pares e impares hay: ")
arreglo = [int(num) for num in numeros.split()]
pares = [num for num in arreglo if num % 2 == 0]
impares = [num for num in arreglo if num % 2 != 0]
print(f"Hay {len(pares)} números pares y {len(impares)} impares")
