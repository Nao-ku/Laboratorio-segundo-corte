def mostrar_matriz(matriz):
  
    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

def mostrar_criticos(criticos):
    print("\nValores críticos detectados (posición y valor):")
    for i, j, valor in criticos:
        print(f"Posición ({i}, {j}): {valor}°C")
