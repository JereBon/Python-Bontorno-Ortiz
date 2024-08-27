i = "admin"
error = 0
while error < 3:
    x = input("Introduzca la contraseña: ")
    if x == i:
        print("Acceso correcto")
        break
    else:
        error = error + 1
        if error == 3:
            print("El acceso se ha bloqueado despues de los 3 intentos")
            break
