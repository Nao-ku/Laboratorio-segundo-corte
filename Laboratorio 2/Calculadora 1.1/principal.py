from interfaz import menu, mostrar_area, solicitar_valores
from figuras import (
    area_cuadrado, area_triangulo, area_circulo, area_rectangulo,
    area_pentagono, area_trapecio, area_rombo, area_romboide
)

opciones = {
    1: ("cuadrado", area_cuadrado, ["lado"]),
    2: ("triángulo", area_triangulo, ["base", "altura"]),
    3: ("círculo", area_circulo, ["radio"]),
    4: ("rectángulo", area_rectangulo, ["base", "altura"]),
    5: ("pentágono", area_pentagono, ["perímetro", "apotema"]),
    6: ("trapecio", area_trapecio, ["base1", "base2", "altura"]),
    7: ("rombo", area_rombo, ["diagonal mayor", "diagonal menor"]),
    8: ("romboide", area_romboide, ["base", "altura"]),
}

while True:
    opcion = menu()
    if opcion == 9:
        print("Saliendo de la calculadora... Gracias por usarla!")
        break
    elif opcion in opciones:
        figura, funcion, parametros = opciones[opcion]
        valores = solicitar_valores(*parametros)
        area = funcion(*valores)
        mostrar_area(figura, area)
    else:
        print("Opción no válida. Intente de nuevo.")
