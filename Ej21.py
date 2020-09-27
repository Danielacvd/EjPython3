# Ejercicio 21: Generar los n primeros números pares positivos.
#Try1


def pares(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1
    else:
        print("Fin ciclo...")



numero = int(input("Ingresa un numero: "))
pares(numero)