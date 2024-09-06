import random
i = random.randint(0, 100)
print(i)
q = 0
while True:
    q = q + 1
    x = int(input("Adivine el numero que esta en el rango entre 0 y 100: "))
    if x < i:
        print("Es muy bajo")
    elif x > i:
        print("Es muy alto")
    else:
        print("Correcto, número encontrado, cantidad de intentos: ", q)
        break
