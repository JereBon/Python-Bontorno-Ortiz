cadena = str(input("Ingrese una cadena de texto:"))
contador = 0
for i in cadena:
    contador += 1
print(f"Tamaño de la cadena:{contador}")

vocal = cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u")
print(f"Vocales de la cadena:{vocal}")