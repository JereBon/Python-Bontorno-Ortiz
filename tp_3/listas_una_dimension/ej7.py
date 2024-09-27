lista = []
suma = 0
a = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
for i in range(a):
    lista.append(int(input(f"Numero {i+1}:")))
    suma += lista[i]
promedio = suma / a
print("El promedio de la suma de los elementos de la lista es: ", promedio)
