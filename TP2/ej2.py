#Si asignas un valor a una variable que está fuera de un rango esperado, en términos de código no ocurre un error, ya que Python no impone límites en las variables numéricas, como lo haría un lenguaje con tipos más rígidos como C o Java.
#Ejemplo:
edad = 200  # Valor fuera de lo esperado para la edad de una persona
print(f"La edad asignada es: {edad}")

#Solucion:
edad = 200
if 0 <= edad <= 120:
    print(f"La edad asignada es: {edad}")
else:
    print("Error: La edad está fuera de rango.")