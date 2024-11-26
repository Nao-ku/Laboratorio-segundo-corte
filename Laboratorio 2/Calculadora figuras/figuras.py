#libreria
import math
#area cuadrado
def area_cuadrado(lado):
    """
    calcula el area del cuadrado
    a = 1 * 1
    tipo float
    """
    area = lado * lado
    return area

#area triangulo
def area_triangulo(base,altura):
    """
    calcula el area del triangulo 
    a = (b*h)/2
    tipo float
    """
    area = (base*altura)/2
    return area
#area circulo
def area_circulo(radio):
    """
    calcula el area del circulo
    a = pi.r^2
    tipo float
    """
    area = math.pi * radio * radio
    return area
#area rectangulo
def area_rectangulo(base,altura):
    """
    calcular el area del rectangulo
    a= b*a
    tipo float
    """
    area = base *altura
    return area
#area pentagono
def area_pentagono(perimetro,apotema):
    """
    calcular el area del pentagono
    a= (p*ap)/2
    tipo float
    """
    area = (perimetro * apotema) /2
    return area
#area trapecio
def area_trapecio(base1,base2,altura):
    """
    calcular el area del trapecio
    a= ((base1+base2)*altura)/2
    tipo float
    """
    area =((base1 * base2) * altura) /2
    return area
def area_rombo(diagonal_mayor,diagonal_menor):
    """
    calcular el area del rombo
    a= (diagonal_mayor,diagonal_menor)/2
    tipo float
    """
    area = (diagonal_mayor,diagonal_menor) /2
    return area
def area_romboide(base,altura):
    """
    calcular el area del romboide
    a= base*altura
    tipo float
    """
    area = (base*altura)
    return area
def area_pentagono(perimetro,apotema):
    """
    calcular el area del pentagono
    a= (p*ap)/2
    tipo float
    """
    area = (perimetro * apotema) /2
    return area
