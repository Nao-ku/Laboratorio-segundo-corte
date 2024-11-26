from interfaz import (
    menu, solicitar_valor, mostrar_area,
    solicitud_cuadrado, solicitud_triangulo, solicitud_circulo,
    solicitud_rectangulo, solicitud_pentagono, solicitud_trapecio,
    solicitud_rombo, solicitud_romboide
)
from figuras import (
    area_cuadrado, area_triangulo, area_circulo, area_rectangulo,
    area_pentagono, area_trapecio, area_rombo, area_romboide
)

# Diccionario de opciones
opciones = {
    1: ("cuadrado", area_cuadrado, solicitud_cuadrado),
    2: ("triángulo", area_triangulo, solicitud_triangulo),
    3: ("círculo", area_circulo, solicitud_circulo),
    4: ("rectángulo", area_rectangulo, solicitud_rectangulo),
    5: ("pentágono", area_pentagono, solicitud_pentagono),
    6: ("trapecio", area_trapecio, solicitud_trapecio),
    7: ("rombo", area_rombo, solicitud_rombo),
    8: ("romboide", area_romboide, solicitud_romboide),
}

# Bucle principal
while True:
    opcion = menu()
    if opcion == 9:
        print("Saliendo de la calculadora... ¡Gracias por usarla!")
        break
    elif opcion in opciones:
        figura, funcion_area, solicitud_funcion = opciones[opcion]
        parametros = solicitud_funcion()
        if not isinstance(parametros, tuple):
            parametros = (parametros,)
        area = funcion_area(*parametros)
        mostrar_area(figura, area)
    else:
        print("Opción no válida. Intente de nuevo.")

