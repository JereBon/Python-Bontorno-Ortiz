texto = "La lluvia en Mendoza es escasa"
codigos_ascii = " ".join(str(ord(caracter)) for caracter in texto)
# La función ord() toma un carácter como entrada y devuelve su código ASCII 
print(codigos_ascii)