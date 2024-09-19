class OperacionMatematica:
    def sumarNumeros(self,valor1,valor2):
        return valor1 + valor2
    def restarNumeros(self,valor1,valor2):
        return valor1 - valor2
    def multiplicarNumeros(self,valor1,valor2):
        return valor1 * valor2
    def dividirNumeros(self, valor1, valor2):
        if valor2 != 0:
            return valor1 / valor2
        else:
            return "Error: División por cero"
    def aplicaroperacion(self,operacion,valor1, valor2):
        if operacion == "+":
            return self.sumarNumeros(valor1, valor2)
        elif operacion == "-":
            return self.restarNumeros(valor1,valor2)
        elif operacion == "*":
            return self.multiplicarNumeros(valor1,valor2)
        elif operacion == "/":
            return self.dividirNumeros(valor1, valor2)
        else:
            return "Operacion no valida"
def main():
    operacionMatematica = OperacionMatematica()
    valor1 = int(input("Ingrese un numero: "))
    valor2 = int(input("Ingrese otro numero: "))
    operacion = input("Ingrese: (+), (-), (*), (/): ")
    resultado = operacionMatematica.aplicaroperacion(operacion, valor1, valor2)
    print(f"El resultado de la operación es: {resultado}")

if True:
    main()