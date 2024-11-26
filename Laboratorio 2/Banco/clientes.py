# clientes.py
from cuentas import consultar_saldo, depositar, retirar  # Importa las funciones necesarias

def agregar_cliente(clientes):
    """Agrega un cliente a la cola de clientes."""
    cliente = input("Ingrese el nombre del cliente a agregar a la cola: ")
    clientes.append(cliente)
    print(f"{cliente} ha sido agregado a la cola.")
    return clientes

def procesar_cliente(clientes, numeros_cuentas, titulares, saldos):
    """Simula el procesamiento de un cliente de la cola."""
    if len(clientes) > 0:
        cliente = clientes.pop(0)  # Eliminar el primer cliente de la cola
        print(f"\nAtendiendo a {cliente}")
        
        # Realizar operaciones bancarias
        consultar_saldo(numeros_cuentas, titulares, saldos)
        depositar(numeros_cuentas, saldos)
        retirar(numeros_cuentas, saldos)
        consultar_saldo(numeros_cuentas, titulares, saldos)
    else:
        print("No hay clientes en la cola.")
    return clientes


