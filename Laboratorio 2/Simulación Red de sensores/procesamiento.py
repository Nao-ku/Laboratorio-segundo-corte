def detectar_criticos(matriz):
    criticos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 80:
                criticos.append((i, j, matriz[i][j]))  # Guardar fila, columna, valor
    return criticos
