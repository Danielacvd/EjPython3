# Ejercicio 39: Calcular el valor futuro para una cantidad, interés, y número de años específicos.
#Try2

# VF = VP(1+i)^n
#Try1
# valor_presente = 10000
# interes = 3.5
# periodos = 7
# Vf = valor_presente * (1 + interes/100)**7
# print(Vf)

def valor_futuro(vp, i, n):
    return f"{(vp * (1 + i/100)**n)}"

valor_presente = 10000
interes = 3.5
periodos = 7

print(valor_futuro(valor_presente, interes, periodos))