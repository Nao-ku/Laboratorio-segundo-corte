Proceso CalculadoraDeFigurasGeometricas
	
    Definir lado, base, altura, radio, perimetro, apotema, area Como Real
    Definir base_mayor, base_menor, diagonal_mayor, diagonal_menor Como Real
    Definir opcion Como Entero
	
    Mientras opcion <> 9 Hacer
        Escribir ""
        Escribir "Bienvenido a la calculadora de figuras geom�tricas"
        Escribir "Seleccione una opci�n del men�:"
        Escribir "1. Cuadrado"
        Escribir "2. Tri�ngulo"
        Escribir "3. C�rculo"
        Escribir "4. Rect�ngulo"
        Escribir "5. Pent�gono"
        Escribir "6. Trapecio"
        Escribir "7. Rombo"
        Escribir "8. Romboide"
        Escribir "9. Salir"
        
        Leer opcion
		
        Segun opcion Hacer
            Caso 1:
                Escribir "Usted seleccion�: Cuadrado"
                Escribir "Ingrese el valor del lado:"
                Leer lado
                area <- lado * lado
                Escribir "El �rea del cuadrado es:", area
				
            Caso 2:
                Escribir "Usted seleccion�: Tri�ngulo"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- (base * altura) / 2
                Escribir "El �rea del tri�ngulo es:", area
				
            Caso 3:
                Escribir "Usted seleccion�: C�rculo"
                Escribir "Ingrese el valor del radio:"
                Leer radio
                area <- 3.1416 * radio * radio
                Escribir "El �rea del c�rculo es:", area
				
            Caso 4:
                Escribir "Usted seleccion�: Rect�ngulo"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- base * altura
                Escribir "El �rea del rect�ngulo es:", area
				
            Caso 5:
                Escribir "Usted seleccion�: Pent�gono"
                Escribir "Ingrese el valor del per�metro:"
                Leer perimetro
                Escribir "Ingrese el valor del apotema:"
                Leer apotema
                area <- (perimetro * apotema) / 2
                Escribir "El �rea del pent�gono es:", area
				
            Caso 6:
                Escribir "Usted seleccion�: Trapecio"
                Escribir "Ingrese el valor de la base mayor:"
                Leer base_mayor
                Escribir "Ingrese el valor de la base menor:"
                Leer base_menor
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- ((base_mayor + base_menor) * altura) / 2
                Escribir "El �rea del trapecio es:", area
				
            Caso 7:
                Escribir "Usted seleccion�: Rombo"
                Escribir "Ingrese el valor de la diagonal mayor:"
                Leer diagonal_mayor
                Escribir "Ingrese el valor de la diagonal menor:"
                Leer diagonal_menor
                area <- (diagonal_mayor * diagonal_menor) / 2
                Escribir "El �rea del rombo es:", area
				
            Caso 8:
                Escribir "Usted seleccion�: Romboide"
                Escribir "Ingrese el valor de la base:"
                Leer base
                Escribir "Ingrese el valor de la altura:"
                Leer altura
                area <- base * altura
                Escribir "El �rea del romboide es:", area
				
            Caso 9:
                Escribir "Saliendo de la calculadora..."
				
            De Otro Modo:
                Escribir "�Opci�n err�nea! Por favor seleccione una opci�n v�lida."
				
        Fin Segun
    Fin Mientras
	
    Escribir "�Gracias por usar la calculadora de figuras geom�tricas!"

FinProceso






