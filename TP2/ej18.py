from datetime import date

class FuncionesPrograma:
    @staticmethod 
    def getFechaDate(año , mes , dia):
        return date(año , mes , dia)
    
dia = int(input("Ingrese el dia : "))
mes = int(input("Ingrese el mes : "))
año = int(input("Ingrese el año : "))
print(FuncionesPrograma.getFechaDate(año , mes , dia))