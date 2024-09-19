import ctypes
#ctypes es un módulo en Python que proporciona tipos de datos compatibles con C.

valorDecimal = float(input("ingrese un numero decimal:"))

valorFloat = float(valorDecimal)

valorInt = int(valorDecimal)

valorShort = ctypes.c_short(int(valorDecimal)).value
# Al usar .value, convertimos el objeto c_short de vuelta a un entero de Python.
#c_short es un tipo de datos en ctypes que representa un short int en C.

valorLong = ctypes.c_long(int(valorDecimal)).value

print(f"Valor original (float): {valorDecimal}")
print(f"Convertido a float: {valorFloat}")
print(f"Convertido a int: {valorInt}")
print(f"Convertido a short: {valorShort}")
print(f"Convertido a long: {valorLong}")