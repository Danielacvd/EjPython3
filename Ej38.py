# Ejercicio 38: Resolver la expresión algebraica (x + y) * (x + y).
#Try1

# (x + y) * (x + y) = x^2 + 2xy + y^2
# (2 + 3) * (2 + 3) = 5 * 5 = 25

def respuesta(x, y):
    print(f"({x} + {y}) * ({x} + {y}) = {x**2 + 2*x*y + y**2} ")

x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))

respuesta(x, y)