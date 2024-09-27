num = int(input("Ingrese el tamaño de la matriz identidad: "))

matriz = []

for i in range(num):
    fila = []
    for j in range(num):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)