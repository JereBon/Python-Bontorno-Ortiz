array = []

a = int(input("Ingrese la cantidad de números que quiere ingresar: "))
for i in range(a):
    array.append(int(input(f"Número {i+1}: ")))
print('Lista: ', array)

b = int(input("Ingrese el indice del numero que quiere eliminar: "))
for i in range(a):
    if b-1 == i:
        array.pop(i)
print('Lista con el elemento eliminado:', array)
