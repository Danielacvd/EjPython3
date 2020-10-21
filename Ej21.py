# Ejercicio 21: Generar los n primeros números pares positivos.
#Try2

#Try1
def pares(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1
    else:
        print("Fin ciclo while ...")

numero = int(input("Ingresa un numero: "))
pares(numero)
#Try2
#con for
for i in range(1,numero+1):
    if i % 2 == 0:
        print(i)
else:
    print("Fin ciclo for")        