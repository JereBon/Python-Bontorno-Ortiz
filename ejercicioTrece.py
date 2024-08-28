i = 2
x = int(input("Introduzca un número: "))
if i in range(x-1):
    if x % i == 0 or x <= 1:
        print("No es número primo")
    else:
        print("Es número primo")
else:
    print("Es número primo")