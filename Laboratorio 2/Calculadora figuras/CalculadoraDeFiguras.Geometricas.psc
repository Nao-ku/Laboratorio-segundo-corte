Proceso CalculadoraDeFigurasGeometricas
	
    Definir lado, base, altura, radio, perimetro, apotema, area Como Real
    Definir base_mayor, base_menor, diagonal_mayor, diagonal_menor Como Real
    Definir opcion Como Entero
	
    Mientras opcion <> 9 Hacer
        Escribir ""
        Escribir "Bienvenido a la calculadora de figuras geométricas"
        Escribir "Seleccione una opción del menú:"
        Escribir "1. Cuadrado"
        Escribir "2. Triángulo"
        Escribir "3. Círculo"
        Escribir "4. Rectángulo"
        Escribir "5. Pentágono"
        Escribir "6. Trapecio"
        Escribir "7. Rombo"
        Escribir "8. Romboide"
        Escribir "9. Salir"
        
        Leer opcion
		
        Segun opcion Hacer
            Caso 1:
                Escribir "Usted seleccionó: Cuadrado"
                Escribir "Ingrese el valor del lado:"
                Leer lado
                area <- lado * lado
                Escribir "El área del cuadrado es:", area
				
            Caso 2:
                Escribir "Usted seleccionó: Triángulo"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- (base * altura) / 2
                Escribir "El área del triángulo es:", area
				
            Caso 3:
                Escribir "Usted seleccionó: Círculo"
                Escribir "Ingrese el valor del radio:"
                Leer radio
                area <- 3.1416 * radio * radio
                Escribir "El área del círculo es:", area
				
            Caso 4:
                Escribir "Usted seleccionó: Rectángulo"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- base * altura
                Escribir "El área del rectángulo es:", area
				
            Caso 5:
                Escribir "Usted seleccionó: Pentágono"
                Escribir "Ingrese el valor del perímetro:"
                Leer perimetro
                Escribir "Ingrese el valor del apotema:"
                Leer apotema
                area <- (perimetro * apotema) / 2
                Escribir "El área del pentágono es:", area
				
            Caso 6:
                Escribir "Usted seleccionó: Trapecio"
                Escribir "Ingrese el valor de la base mayor:"
                Leer base_mayor
                Escribir "Ingrese el valor de la base menor:"
                Leer base_menor
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- ((base_mayor + base_menor) * altura) / 2
                Escribir "El área del trapecio es:", area
				
            Caso 7:
                Escribir "Usted seleccionó: Rombo"
                Escribir "Ingrese el valor de la diagonal mayor:"
                Leer diagonal_mayor
                Escribir "Ingrese el valor de la diagonal menor:"
                Leer diagonal_menor
                area <- (diagonal_mayor * diagonal_menor) / 2
                Escribir "El área del rombo es:", area
				
            Caso 8:
                Escribir "Usted seleccionó: Romboide"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- base * altura
                Escribir "El área del romboide es:", area
				
            Caso 9:
                Escribir "Saliendo de la calculadora..."
				
            De Otro Modo:
                Escribir "¡Opción errónea! Por favor seleccione una opción válida."
				
        Fin Segun
    Fin Mientras
	
    Escribir "¡Gracias por usar la calculadora de figuras geométricas!"

FinProceso






