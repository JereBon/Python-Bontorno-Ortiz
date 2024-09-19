def recursion(num):
    if num == 1:
        return 1
    else:
        return num + recursion(num - 1)

num = int(input("Ingrese un numero para sumarlo con todos sus anteriores: "))
print(recursion(num))
