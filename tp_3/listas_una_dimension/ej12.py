def crea_lista(x):
    lista = []
    for i in range(a):
        lista.append(int(input(f"Número {i+1}: ")))
    return lista


array_suma = []
a = int(input("Ingrese la cantidad de números que quiere ingresar para sumar dos listas: "))

print('Primera lista')
array_uno = crea_lista(a)
print('Segunda lista')
array_dos = crea_lista(a)

for i in range(a):
    array_suma.append(array_uno[i] + array_dos[i])
print('La suma de elemento por elemento', array_suma)
