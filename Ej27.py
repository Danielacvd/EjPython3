#Ejercicio 27: Generar un conjunto de números aleatorios y determinar cuáles son impares.
#Try1
from random import randint

n = int(input("Cuantos numeros random quieres: "))
lista = []
for i in range(n):
    lista.append(randint(1, 100))
else:
    print("Fin ciclo")    

print(lista)

for i in lista:
    if not i % 2 == 0:
        print(i) 
