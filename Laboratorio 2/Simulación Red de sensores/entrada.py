def generar_matriz(n, m):
    """
    Genera una matriz de tamaño n x m con valores ingresados por el usuario.
    """
    matriz = []
    print("Ingrese los valores de los sensores:")
    for i in range(n):
        fila = []
        for j in range(m):
            valor = int(input(f"Sensor en posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
