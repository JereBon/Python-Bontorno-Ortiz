matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz original:")
print(matriz)

escalar = float(input("Ingresa un valor escalar: "))

matrizEscalar = [
    
]

for fila in matriz:
    nuevaFila = []
    for elemento in fila:
        nuevaFila.append(elemento * escalar)
    matrizEscalar.append(nuevaFila)

    

print(matrizEscalar)