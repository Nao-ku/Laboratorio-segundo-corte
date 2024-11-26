from producto import Producto

def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for producto in inventario:
        print(producto)

def buscar_producto(inventario, nombre_producto):
    for producto in inventario:
        if producto.nombre == nombre_producto:
            return producto
    return None

def realizar_compra(inventario, nombre_producto, cantidad):
    producto = buscar_producto(inventario, nombre_producto)
    if producto:
        producto.aumentar_stock(cantidad)
        print(f"Compra exitosa: {cantidad} unidades de {nombre_producto} agregadas al inventario.")
    else:
        print(f"Producto {nombre_producto} no encontrado en el inventario.")

def realizar_venta(inventario, nombre_producto, cantidad):
    producto = buscar_producto(inventario, nombre_producto)
    if producto:
        producto.disminuir_stock(cantidad)
    else:
        print(f"Producto {nombre_producto} no encontrado en el inventario.")
