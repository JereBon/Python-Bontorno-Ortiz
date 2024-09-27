num = int(input("Ingrese el tamaño de la matriz identidad invertida: "))

matriz = []

for i in range(num):
    fila = []
    for j in range(num):
        if i + j == num - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)