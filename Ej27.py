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


#Try2
print("***Solucion2***")
def impares(n):
    lista2 = []
    i = 0
    while i < n:
        lista2.append(randint(1, 10000))
        i += 1
    resultado2 = []    
    for i in lista2:
        if not i % 2 == 0:
            resultado2.append(i)

    print(f"De la lista {lista2}\nEstos son los numero impares: {resultado2}")   

impares(n)     