matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

if transpuesta == matriz:
    print("La matriz es igual a su transpuesta")
else:
    print("La matriz no es igual a su transpuesta")