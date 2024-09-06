x = int(input("Ingrese un número: "))

if x > 1:
    es_primo = True
    for n in range(2, x):
        if x % n == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo")
    else:
        print("No es un número primo")
else:
    print("No es un número primo")
