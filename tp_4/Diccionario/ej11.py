inventario = {
    "A001": ("Laptop", 1500),
    "A002": ("Mouse", 25),
    "A003": ("Teclado", 45),
    "A004": ("Monitor", 300),
    "A005": ("Impresora", 120)
}

def mostrar_inventario(inventario):
    print("Inventario de productos:")
    for items in inventario.items():
        print(items)

def buscar_producto(inventario, codigo):
    if codigo in inventario:
        descripcion, precio = inventario[codigo]
        print(f"Producto encontrado: {descripcion}, Precio: ${precio}")
    else:
        print("Producto no encontrado.")

def modificar_precio(inventario, codigo, nuevo_precio):
    if codigo in inventario:
        descripcion, _ = inventario[codigo]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"El precio del producto con código {codigo} ha sido actualizado a ${nuevo_precio}")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo]
        print(f"El producto con código {codigo} ha sido eliminado del inventario.")
    else:
        print("Producto no encontrado.")

def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}:")
    encontrados = False
    for codigo, (descripcion, precio) in inventario.items():
        if min_precio <= precio <= max_precio:
            print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")
            encontrados = True
    if not encontrados:
        print("No hay productos en ese rango de precio.")

mostrar_inventario(inventario)
buscar_producto(inventario, "A003")
modificar_precio(inventario, "A004", 350)
eliminar_producto(inventario, "A002")
productos_por_rango_de_precio(inventario, 100, 500)