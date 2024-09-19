x = None print(x) 
#Al ejecutar sucede: "SyntaxError: invalid syntax"
#None en Python:
#Objeto único que representa ausencia de valor.
#Singleton (solo existe una instancia en todo el programa) inmutable de tipo NoneType.
#Se evalúa como falso en contextos booleanos.

#USOS:
#a) Valor por defecto para parámetros de funciones:

def saludar(nombre=None):
    if nombre is None:
        print("Hola, invitado!")
    else:
        print(f"Hola, {nombre}!")

saludar()
saludar("Jere")

#b) Representar la ausencia de un valor de retorno:
def buscar_elemento(lista, elemento):
    for item in lista:
        if item == elemento:
            return item
    return None

resultado = buscar_elemento([1, 2, 3], 4)
if resultado == None:
    print("Elemento no encontrado")

#c)None en contextos booleanos:
x = None
if not x:
    print("None se evalúa como False en contextos booleanos")