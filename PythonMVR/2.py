"""
Mostrar por pantalla todos los numeros pares del 1 al 100
"""
#Try1
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
else:
    print("Estos son los primeros 100 numeros pares")      


#Try2
def es_par(num):
    if num % 2 == 0:
        print(num)

for i in range(1, 101):
    es_par(i)
else:
    print('Fin cliclo For, Try2')    
