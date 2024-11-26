import math 

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_rectangulo(base, altura):
    return base * altura

def area_pentagono(perimetro, apotema):
    return (perimetro * apotema) / 2

def area_trapecio(base1, base2, altura):
    return ((base1 + base2) * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_romboide(base, altura):
    return base * altura
