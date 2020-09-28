# Ejercicio 33: Sumar dos números. Si la suma está entre 10 y 30, retornar 30.
#Try1

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))

suma = n1 + n2
if suma >= 10 and suma <= 30:
    print("30")
else:
    print("La suma no esta entre 30")    