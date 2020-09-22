# Ejercicio 6: Obtener un conjunto de números separados por coma y crear una lista.
#Try 1
# 2, 8, 9, 0, 1, 


numeros = input("Ingresa varios numeros se parados por comas: ")

lista = numeros.split(', ')
print(lista)
print(type(lista))


