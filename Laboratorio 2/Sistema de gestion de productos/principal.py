from gestionar_inventario import mostrar_inventario, realizar_compra, realizar_venta
from producto import Producto

def inicializar_inventario():
    producto1 = Producto("Pan", 1.50, 100)
    producto2 = Producto("Leche", 0.90, 50)
    producto3 = Producto("Mantequilla", 2.00, 30)
    return [producto1, producto2, producto3]

def gestionar_inventario():
    inventario = inicializar_inventario()

    mostrar_inventario(inventario)

    realizar_compra(inventario, "Pan", 20)
    mostrar_inventario(inventario)

    realizar_venta(inventario, "Leche", 10)
    mostrar_inventario(inventario)

    realizar_venta(inventario, "Mantequilla", 40)
    mostrar_inventario(inventario)

if __name__ == "__main__":
    gestionar_inventario()
