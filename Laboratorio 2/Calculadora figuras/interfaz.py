# función del menú principal
def menu():
    """
    Muestra el menú de las figuras geométricas y retorna la opción seleccionada.
    """
    print("\nBienvenido a la calculadora de figuras geométricas")
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
            op = int(input("Digite una opción del menú: "))
            return op
        except ValueError:
            print("Error: Debes ingresar un número.")

# Solicitudes con manejo de errores para valores numéricos
def solicitar_valor(mensaje):
    """
    Solicita un valor numérico al usuario con un mensaje dado.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número.")

def solicitud_cuadrado():
    return solicitar_valor("Digite el lado (en cm): ")

def solicitud_triangulo():
    base = solicitar_valor("Digite la base (en cm): ")
    altura = solicitar_valor("Digite la altura (en cm): ")
    return base, altura

def solicitud_circulo():
    return solicitar_valor("Digite el radio (en cm): ")

def solicitud_rectangulo():
    base = solicitar_valor("Digite la base (en cm): ")
    altura = solicitar_valor("Digite la altura (en cm): ")
    return base, altura

def solicitud_pentagono():
    perimetro = solicitar_valor("Digite el perímetro (en cm): ")
    apotema = solicitar_valor("Digite la apotema (en cm): ")
    return perimetro, apotema

def solicitud_trapecio():
    base1 = solicitar_valor("Digite la base 1 (en cm): ")
    base2 = solicitar_valor("Digite la base 2 (en cm): ")
    altura = solicitar_valor("Digite la altura (en cm): ")
    return base1, base2, altura

def solicitud_rombo():
    diagonal_mayor = solicitar_valor("Digite la diagonal mayor (en cm): ")
    diagonal_menor = solicitar_valor("Digite la diagonal menor (en cm): ")
    return diagonal_mayor, diagonal_menor

def solicitud_romboide():
    base = solicitar_valor("Digite la base (en cm): ")
    altura = solicitar_valor("Digite la altura (en cm): ")
    return base, altura

# Mostrar áreas con la unidad "cm²"
def mostrar_area(figura, area):
    print(f"El área del {figura} es: {area:.2f} cm².\n")











