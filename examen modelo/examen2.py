from typing import List


class Factura:
    def __init__(self, fechaFactura=None, numeroFactura=None, letraFactura=None, totalFactura=0, montoIva=0, clienteFactura="Consumidor Final", detallesFactura=None):
        self.fechaFactura = fechaFactura
        self.numeroFactura = numeroFactura
        self.letraFactura = letraFactura
        self.totalFactura = totalFactura
        self.montoIva = montoIva
        self.clienteFactura = clienteFactura
        self.detallesFactura = detallesFactura if detallesFactura is not None else []

    def mostrarFactura(self):
        print(f"\nFecha: {self.fechaFactura}")
        print(f"Numero: {self.numeroFactura}")
        print(f"Letra: {self.letraFactura}")
        print(f"Cliente: {self.clienteFactura}")
        print("\nCódigo   Nombre Artículo   Cantidad   Precio Unitario   Subtotal")
        print("-------------------------------------------------------------")

        for detalle in self.detallesFactura:
            codigo, nombre, cantidad, precio_unitario, subtotal = detalle
            print(f"{codigo:<8} {nombre:<15} {cantidad:<10} {precio_unitario:<15} {subtotal:<8}")

        print("\n\t\t\t\tIVA:", f"{self.montoIva:.2f}")
        print("\t\t\t\tTotal:", f"{self.totalFactura:.2f}")

    def datosFactura(self):
        self.fechaFactura = input("Ingrese la fecha de la Factura (dd-mm-yyyy): ")
        self.numeroFactura = int(input("Ingrese el Numero de la Factura: "))

    def datosCuit(self, clientes):
        while True:
            cuit = int(input("Ingrese el CUIT del cliente: "))
            cuit_str = str(cuit)
            if (cuit_str[0] == "2" and (cuit_str[1] == "0" or cuit_str[1] == "7")) or (cuit_str[0] == "3" and (cuit_str[1] == "0" or cuit_str[1] == "3")):
                self.clienteFactura = cuit
                break
            else:
                self.clienteFactura = clientes.get(cuit, "Consumidor Final")
                break
    
    def solicitar_articulos(self, articulos):
        while True:
            codigo = input("Ingrese el código del artículo, ingrese 0000 para finalizar: ")
            if codigo == "0000":
                break

            articulo_encontrado = next((articulo for articulo in articulos if str(articulo[0]) == codigo), None)

            if articulo_encontrado is None:
                print("Código Incorrecto")
            else:
                cantidad = int(input(f"Ingrese la cantidad de {articulo_encontrado[1]} a facturar: "))
                precio_unitario = articulo_encontrado[2]
                subtotal = cantidad * precio_unitario
                self.detallesFactura.append([codigo, articulo_encontrado[1], cantidad, precio_unitario, subtotal])
                self.totalFactura += subtotal
                print(f"{articulo_encontrado[1]} agregado con éxito.")

      
    def calcularTotal(self):
        total = sum(detalle[4] for detalle in self.detallesFactura)
        return total
    
    def montoIVA(self):
        total = self.calcularTotal()
        cuit_str = str(self.clienteFactura)
        
        if (cuit_str[0] == "3" and (cuit_str[1] == "0" or cuit_str[1] == "3")):
            self.montoIva = total * 0.21 
        else:
            self.montoIva = 0  
        return self.montoIva
    
    def asignarLetraFactura(self):
        cuit_str = str(self.clienteFactura)
        
        if cuit_str.startswith("20") or cuit_str.startswith("27") or cuit_str == "Consumidor Final":
            self.letraFactura = "B"
        elif cuit_str.startswith("30") or cuit_str.startswith("33"):
            self.letraFactura = "A"
        return self.letraFactura
    
    def calcularTotalFinal(self):        
        total_base = self.calcularTotal()
        
        self.asignarLetraFactura()
        self.montoIVA()

        if self.letraFactura == "B":
            self.totalFactura = total_base + self.montoIva
        else:
            self.totalFactura = total_base
        
        return self.totalFactura

# Datos de ejemplo
articulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca", 200],
    [107, "Lavandina", 180],
    [108, "Detergente", 460],
    [109, "Jabón en Polvo", 960],
    [110, "Galletas", 600]
]

clientes = {
    20110425417: "Rodolfo Fernandez",
    30527419655: "Los Pollos Hnos",
    27289425478: "Andrea Pereira",
    33536549878: "Multimarca Repuestos",
    20291122568: "Luis Peric"
}

factura = Factura()
factura.datosFactura()
factura.datosCuit(clientes)
factura.solicitar_articulos(articulos)
total_final = factura.calcularTotal()
letra = factura.asignarLetraFactura()
monto_iva = factura.montoIVA()
total_final_factura = factura.calcularTotalFinal()
factura.mostrarFactura()