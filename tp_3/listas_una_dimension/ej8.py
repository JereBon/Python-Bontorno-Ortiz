def numeros_repetidos(lista):
    visto = set()
    no_visto = set()

    for elemento in lista:
        if elemento in no_visto:
            visto.add(elemento)
        else:
            no_visto.add(elemento)
    return list(visto)


array = []
a = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
for i in range(a):
    array.append(int(input(f"Numero {i+1}:")))
repetidos = numeros_repetidos(array)
print("Elementos Repetidos: ", repetidos)
