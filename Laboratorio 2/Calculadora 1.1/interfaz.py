def menu():
    print("Calculadora de áreas - Elige una figura:")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Rectángulo")
    print("5. Pentágono")
    print("6. Trapecio")
    print("7. Rombo")
    print("8. Romboide")
    print("9. Salir")
    while True:
        try:
            opcion = int(input("Introduce tu opción: "))
            return opcion
        except ValueError:
            print("Error: Debes ingresar un número.")

def mostrar_area(figura, area):
    print(f"El área del {figura} es {area:.2f} cm².\n")

def solicitar_valores(*parametros):
    valores = []
    for parametro in parametros:
        while True:
            try:
                valor = float(input(f"Introduce el valor de {parametro} (en cm): "))
                valores.append(valor)
                break
            except ValueError:
                print(f"Error: {parametro} debe ser un número.")
    return valores

