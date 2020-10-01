# Ejercicio 40: Calcular la distancia entre dos puntos cartesianos.
#Try1
# P1(x1, y1), P2(x2, y2)

#d = sqrt((x2-x1)²+(y2 - y1)²)

from math import sqrt

x1 = int(input("Ingresa valor para x1: "))
x2 = int(input("Ingresa valor para x2: "))
y1 = int(input("Ingresa valor para y1: "))
y2 = int(input("Ingresa valor para y2: "))

d = sqrt((x2 -x1)**2+(y2 - y1)**2)
print(f"La distancia es: {d}")