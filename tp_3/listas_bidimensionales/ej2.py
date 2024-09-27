matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma = sum(sum(fila) for fila in matriz)
print(suma)