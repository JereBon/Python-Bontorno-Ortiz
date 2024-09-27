matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i, fila in enumerate(matriz):
    suma = sum(fila)
    print(f"La suma de la fila número {i+1} es {suma}")