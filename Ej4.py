# Ejercicio 4: Solicitar el valor del radio de un círculo para calcular su área.
#Try1

from math import pi
def area(radio):
    return pi*radio**2

radio = int(input("Ingresa el radio del circulo: "))
print(f"El area es: {area(radio)}")