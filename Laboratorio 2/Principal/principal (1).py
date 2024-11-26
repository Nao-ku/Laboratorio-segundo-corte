from cuentas import consultar_saldo, depositar, retirar
from clientes import agregar_cliente, procesar_cliente

# Listas para almacenar la información de las cuentas
numeros_cuentas = []
titulares = []
saldos = []

# Cola de clientes
clientes = []

# Menú principal
while True:
    print("\nMenú del sistema bancario")
    print("1. Crear una nueva cuenta")
    print("2. Depositar en una cuenta")
    print("3. Retirar de una cuenta")
    print("4. Consultar saldo de una cuenta")
    print("5. Mostrar todas las cuentas")
    print("6. Agregar un cliente a la cola")
    print("7. Procesar el siguiente cliente")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # Crear una nueva cuenta
        numero = input("Ingrese el número de la cuenta: ")
        titular = input("Ingrese el nombre del titular: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        
        # Agregar los datos a las listas
        numeros_cuentas = numeros_cuentas + [numero]
        titulares = titulares + [titular]
        saldos = saldos + [saldo_inicial]
        print("Cuenta creada exitosamente.")
    
    elif opcion == "2":
        # Depositar en una cuenta
        numeros_cuentas, saldos = depositar(numeros_cuentas, saldos)
    
    elif opcion == "3":
        # Retirar de una cuenta
        numeros_cuentas, saldos = retirar(numeros_cuentas, saldos)
    
    elif opcion == "4":
        # Consultar saldo de una cuenta
        consultar_saldo(numeros_cuentas, titulares, saldos)
    
    elif opcion == "5":
        # Mostrar todas las cuentas
        print("\nEstado de todas las cuentas:")
        for i in range(len(numeros_cuentas)):
            print(f"Cuenta {numeros_cuentas[i]} - Titular: {titulares[i]} - Saldo: ${saldos[i]:.2f}")
    
    elif opcion == "6":
        # Agregar un cliente a la cola
        clientes = agregar_cliente(clientes)
    
    elif opcion == "7":
        # Procesar el siguiente cliente
        clientes = procesar_cliente(clientes, numeros_cuentas, titulares, saldos)
    
    elif opcion == "8":
        print("Gracias por usar el sistema bancario. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")


