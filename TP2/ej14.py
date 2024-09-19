#Python no tiene una distinción explícita entre variables de tipo valor y tipo referencia como Java, el concepto 
# de inmutabilidad vs mutabilidad proporciona un comportamiento similar en muchos casos.
#Ejemplo:

a = 5
b = a
a = 10
# Objetos inmutables (similar a "tipo valor")
print(a, b)

list1 = [1, 2, 3]
list2 = list1
list1.append(4)
# Objetos mutables (similar a "tipo referencia")
print(list1, list2)