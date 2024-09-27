numeros = input("Ingrese numeros separados por espacios para encontrar el menor y el mayor: ")
arreglo = [float(num) for num in numeros.split()]
print(f"El número menor es el {min(arreglo)} y el mayor el {max(arreglo)}")