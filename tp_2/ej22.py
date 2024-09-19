def recursion(num):
    if num < 10:
        return num
    else:
        digito = num % 10
        num = num // 10
        return digito + recursion(num)

num = int(input("Ingrese un numero para conocer la suma de sus caracteres: "))
if num < 0:
    print("Por favor, ingrese un número positivo.")

else:
    resultado = recursion(num)
    print(resultado)