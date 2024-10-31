texto = "manzana naranja manzana pera pera pera naranja manzana"
resultado = {}

modificado = texto.split()

for palabra in modificado:
    if palabra in resultado:
        resultado[palabra] += 1
    else:
        resultado[palabra] = 1

print(resultado)