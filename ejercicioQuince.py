x = 0
x = int(input("Ingrese un número entero: "))
print("El número ", x ," es divisible por:")
if x % 2 == 0:
    print("2")
if ((x // 10) + (x % 10)) % 3 == 0:
    print("3")
if x % 10 == 0 or x % 10 == 5:
    print("5")
if x % 2 == 0 and ((x // 10) + (x % 10)) % 3 == 0:
    print("6")
if ((x // 10) + (x % 10)) % 9 == 0:
    print("9")
if x % 10 == 0:
    print("10")