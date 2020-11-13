"""
Pedir 2 numeros al usuario y hacer todas las operaciones basicas de una calculadora con los 2 numeros.
"""
#Try1
numero_1 = input("Ingresa el primero numero: ")
numero_2 = input("Ingresa el segundo numero: ")

print(f"La suma es: {int(numero_1) + int(numero_2)}")
print(f"La resta es: {int(numero_1) - int(numero_2)}")
print(f"La multiplicacion es: {int(numero_1) * int(numero_2)}")
print(f"La diviion es: {int(numero_1) / float(numero_2)}")

#Try2
suma = lambda n1, n2: f"La suma es: {int(numero_1)+int(numero_2)}"
print(suma(numero_1, numero_2))
resta = lambda n1, n2: f"La resta es: {int(numero_1)-int(numero_2)}"
print(resta(numero_1, numero_2))
multiplicacion = lambda n1, n2: f"La multiplicacion es: {int(numero_1)*int(numero_2)}"
print(multiplicacion(numero_1, numero_2))
division = lambda n1, n2: f"La division es: {int(numero_1)/int(numero_2)}"
print(division(numero_1, numero_2))