class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    @staticmethod
    def sumar_fracciones(f1, f2):
        nuevo_num = f1.num * f2.den + f2.num * f1.den
        nuevo_den = f1.den * f2.den
        return Fraccion(nuevo_num, nuevo_den)

    @staticmethod
    def restar_fracciones(f1, f2):
        nuevo_num = f1.num * f2.den - f2.num * f1.den
        nuevo_den = f1.den * f2.den
        return Fraccion(nuevo_num, nuevo_den)

    @staticmethod
    def multiplicar_fracciones(f1, f2):
        nuevo_num = f1.num * f2.num
        nuevo_den = f1.den * f2.den
        return Fraccion(nuevo_num, nuevo_den)

    @staticmethod
    def dividir_fracciones(f1, f2):
        nuevo_num = f1.num * f2.den
        nuevo_den = f1.den * f2.num
        return Fraccion(nuevo_num, nuevo_den)


def main():
    num1 = int(input("Ingrese el numerador de la primera fracción:"))
    den1 = int(input("Ingrese el denominador de la primera fracción:"))
    f1 = Fraccion(num1, den1)

    num2 = int(input("Ingrese el numerador de la segunda fracción:"))
    den2 = int(input("Ingrese el denominador de la segunda fracción:"))
    f2 = Fraccion(num2, den2)

    suma = Fraccion.sumar_fracciones(f1, f2)
    resta = Fraccion.restar_fracciones(f1, f2)
    multiplicacion = Fraccion.multiplicar_fracciones(f1, f2)
    division = Fraccion.dividir_fracciones(f1, f2)

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")


if __name__ == "__main__":
    main()