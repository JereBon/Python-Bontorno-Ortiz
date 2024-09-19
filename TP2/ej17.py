dias = {
    1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
    11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince", 16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve", 20: "Veinte",
    21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco", 26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta", 31: "Treinta y uno"
}

meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']


class FuncionesPrograma:

    @staticmethod 
    def getFechaString(fecha):
        dia , mes , año = fecha.split("/")
        dia = dia.lstrip("0")
        mes = mes.lstrip("0")
        año = año.lstrip("0")
        
        dia = int(dia)
        mes = int(mes)
        año = int(año)

        def numero_a_palabras(numero):
            if numero == 2000:
                return "dos mil"
            elif numero == 1000:
                return "mil"
            elif numero > 2000:
                return "dos mil " + numero_a_palabras(numero - 2000)
            elif numero > 1000:
                return "mil " + numero_a_palabras(numero - 1000)
            elif numero > 100:
                return centenas[numero // 100] + ' ' + numero_a_palabras(numero % 100)
            elif numero > 10:
                return decenas[numero // 10] + ' ' + numero_a_palabras(numero % 10)
            else:
                return unidades[numero]

        diaLiteral = dias[dia]
        mesLiteral = meses[mes]
        añoLiteral = numero_a_palabras(int(año))
        
        return f"{diaLiteral} de {mesLiteral} de {añoLiteral}".capitalize()
    
while True:
    print("FECHAS DE NÚMERO A CADENA LITERAL")
    fecha = str(input("Ingrese una fecha en el formato dd/mm/aaaa : ").strip())
    if len(fecha) == 10:
        print(FuncionesPrograma.getFechaString(fecha))
        break