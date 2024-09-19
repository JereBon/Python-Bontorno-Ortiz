cadena = str(input("Ingrese una cadena de texto:"))

print(f"Tamaño de la cadena:{len(cadena)}")

vocal = cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u")
print(f"Vocales de la cadena:{vocal}")