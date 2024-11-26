def consultar_saldo(numeros_cuentas, titulares, saldos):
    """Consulta el saldo de una cuenta específica."""
    numero = input("Ingrese el número de la cuenta: ")
    
    # Buscar la cuenta
    for i in range(len(numeros_cuentas)):
        if numeros_cuentas[i] == numero:
            print(f"Saldo actual de la cuenta {numero} ({titulares[i]}): ${saldos[i]:.2f}")
            return
    print("Cuenta no encontrada.")

def depositar(numeros_cuentas, saldos):
    """Permite realizar un depósito en una cuenta."""
    numero = input("Ingrese el número de la cuenta: ")
    
    # Buscar la cuenta
    for i in range(len(numeros_cuentas)):
        if numeros_cuentas[i] == numero:
            monto = float(input("Ingrese el monto a depositar: "))
            saldos[i] += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldos[i]:.2f}")
            return numeros_cuentas, saldos
    print("Cuenta no encontrada.")
    return numeros_cuentas, saldos

def retirar(numeros_cuentas, saldos):
    """Permite realizar un retiro de una cuenta."""
    numero = input("Ingrese el número de la cuenta: ")
    
    # Buscar la cuenta
    for i in range(len(numeros_cuentas)):
        if numeros_cuentas[i] == numero:
            monto = float(input("Ingrese el monto a retirar: "))
            
            if monto <= saldos[i]:
                saldos[i] -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldos[i]:.2f}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
            return numeros_cuentas, saldos
    print("Cuenta no encontrada.")
    return numeros_cuentas, saldos



