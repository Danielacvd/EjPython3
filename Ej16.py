# Ejercicio 16: Crear una función para evaluar un número y realizar una operación.
# fn(n): si n <= 15 => 15 - n; (15 - n) * 2
#Try1

def evaluar(n):
    if n <= 15:
        print(f"{15-n}")
    else:
        print(f"{(15 - n)*2}")

numero = int(input("Ingresa un numero: "))
evaluar(numero)        