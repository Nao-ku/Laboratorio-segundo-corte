from entrada import generar_matriz
from procesamiento import detectar_criticos
from salida import mostrar_matriz, mostrar_criticos

def main():
    n = int(input("Ingrese el número de filas (n): "))
    m = int(input("Ingrese el número de columnas (m): "))

    matriz = generar_matriz(n, m)
    mostrar_matriz(matriz)

    criticos = detectar_criticos(matriz)
    mostrar_criticos(criticos)

if __name__ == "__main__":
    main()
