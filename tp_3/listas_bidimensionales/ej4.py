matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(transpuesta)