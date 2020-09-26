# Ejercicio 15: Calcular el volumen de una esfera a partir del radio dado.
# Try1

#V= 4/3*pi*r**3

from math import pi

radio = float(input("Ingresa el radio: "))
v = (4/3)*pi*radio**3
print(f"El Volumen para el radio: {radio} es: {v}")