def numero_primo(x):
    if x > 1:
        es_primo = True
        for n in range(2, x):
            if x % n == 0:
                es_primo = False
                break
        if es_primo:
            return x
    return None


array = []
a = int(input("Ingrese la cantidad de números que quiere ingresar: "))
for i in range(a):
    array.append(int(input(f"Número {i+1}: ")))
primos = [x for x in array if numero_primo(x)]
print("Números primos en la lista:", primos)
