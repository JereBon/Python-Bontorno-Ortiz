while True:
    dia = int(input("Ingrese un dia de la semana en número (1-7): "))
    if 1 <= dia <= 7:
        match dia:
            case x if 1 <= x <= 5:
                print("Día laboral")
                break
            case 6 | 7:
                print("Día no laboral")
                break