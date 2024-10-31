array = []
contador = 0
a = int(input("Ingrese la cantidad de números que quiere ingresar: "))
for i in range(a):
    array.append(int(input(f"Número {i+1}: ")))

b = int(input("Ingrese un numero para saber cuantas veces aparece: "))
for i in range(a):
    if b == array[i]:
        contador += 1
print(f'El numero {b} aparece {contador} en la lista', array)
