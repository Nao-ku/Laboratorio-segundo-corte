
def generar_matriz(n, m):
    matriz = []
    print("Ingrese los valores de los sensores:")
    for i in range(n):
        fila = []
        for j in range(m):
            valor = int(input(f"Sensor en posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def detectar_criticos(matriz):
    criticos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 80:
                criticos.append((i, j, matriz[i][j]))  # Guardar fila, columna, valor
    return criticos


n = int(input("Ingrese el número de filas (n): "))
m = int(input("Ingrese el número de columnas (m): "))


matriz = generar_matriz(n, m)


print("\nMatriz generada:")
for fila in matriz:
    print(fila)


criticos = detectar_criticos(matriz)
print("\nValores críticos detectados (posición y valor):")
for i, j, valor in criticos:
    print(f"Posición ({i}, {j}): {valor}°C")


