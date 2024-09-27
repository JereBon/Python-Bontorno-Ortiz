matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mayor = 0
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento
            
print(f"El mayor valor encontrado es: {mayor}")