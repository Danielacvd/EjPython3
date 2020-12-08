"""
Variables y condicionales
"""
"""
1. Pedir los coeficientes de una ecuación se 2o grado, y muestre sus soluciones reales. Si no existen,
debe indicarlo.

"""
from math import sqrt
# ax**2 + bx + c = 0
# a al cuadrado, b al lineal, c independiente
#x = -b +- sqrt(b**2 - 4ac)/2*a

#a1, b2, c-8

a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

solucion_mas = (-(b)+sqrt(b**2-(4*a*c)))/2*a
solucion_menos = (-(b)-sqrt(b**2-(4*a*c)))/2*a

print(f"La solucion con mas es {solucion_mas}")
print(f"La solucion con menos es {solucion_menos}")