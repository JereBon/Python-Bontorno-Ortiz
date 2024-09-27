matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz original:")
print(matriz)

diagonal = []

for i in range(len(matriz)):
    diagonal.append(matriz[i][i])

print(diagonal)