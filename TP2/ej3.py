while True:
    num = int(input("Ingrese un número de 3 digitos:"))
    if 100 <= num <= 999:
        num1 = num // 100
        num2 = (num // 10) % 10
        num3 = num % 10
        suma = num1 + num2 + num3
        print(f"La suma de sus dígitos es: {suma}")
        break