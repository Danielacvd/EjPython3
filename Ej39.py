# Ejercicio 39: Calcular el valor futuro para una cantidad, interés, y número de años específicos.
#Try1

# VF = VP(1+i)^n

valor_presente = 10000
interes = 3.5
periodos = 7

Vf = valor_presente * (1 + interes/100)**7
print(Vf)