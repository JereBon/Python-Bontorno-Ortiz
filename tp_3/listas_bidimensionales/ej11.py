matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotada90 = [[matriz[len(matriz) - 1 - j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(rotada90)

print("Matriz rotada 90 grados en el sentido de las agujas del reloj:")
for fila in rotada90:
    print(fila)