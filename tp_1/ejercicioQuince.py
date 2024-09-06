def suma_cifras(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma


x = 0
x = int(input("Ingrese un número entero: "))
print("El número ", x, " es divisible por:")

if x % 2 == 0:
    print("2")
if suma_cifras(x) % 3 == 0:
    print("3")
if x % 10 == 0 or x % 10 == 5:
    print("5")
if x % 2 == 0 and suma_cifras(x) % 3 == 0:
    print("6")
if suma_cifras(x) % 9 == 0:
    print("9")
if x % 10 == 0:
    print("10")
