# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres.
#Try1 Sin join

palabra = "hola"
invertida = []
res = ""
for i in palabra:
    invertida.append(i)

invertida.reverse()
for u in invertida:
    res +=f"{u}"
print(f"Palabra original: {palabra}")
print(f"Palabra inversa: {res}")


 