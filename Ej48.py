# Ejercicio 48: Convertir una cadena de caracteres a entero y real.
#Try2
# int(), float()

#Try1
# cadena = '3.1415'
# cadena_entero = int(cadena[0])
# cadena_real = float(cadena)
# print(cadena_entero)
# print(cadena_real)

def entero(n):
    return int(n[0])

def real(n):
    return float(n)

cadena = '3.1415'
print(entero(cadena)) 
print(real(cadena))        