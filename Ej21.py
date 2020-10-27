# Ejercicio 21: Generar los n primeros números pares positivos.
#Try3

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
#Try3
#Esto tenia que estar arriba
from random import randint

n = randint(1, 1000)
print(n)

u = 1
while u <= n:
    if u % 2 == 0:
        print(u)
    u += 1    
else:
    print("Fin Solucion 3")        
