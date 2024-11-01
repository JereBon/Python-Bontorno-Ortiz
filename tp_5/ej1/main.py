from Matriz import Matriz

def main():
    matriz = Matriz()
    while True:
        valor = input("Ingrese un valor para la celda (o 'FIN' para terminar): ")
        if valor.upper() == 'FIN':
            break
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        matriz.agregar_celda(fila, columna, valor)

    matriz.mostrar_celdas()

if __name__ == "__main__":
    main()