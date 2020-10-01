# Ejercicio 8: Obtener el primer y último de una lista.
#Try2
lenguajes = ['Python', 'C#', 'PHP', 'Java', 'JavaScript']

#Try1
# print(lenguajes[0])
# print(lenguajes[-1])

def primero_ultimo(lista):
    res = ""
    if lista[0]:
        res += f"{lista[0]}"    
    if lista[-1]:
      res += f" {lista[-1]}"
    return res        

print(primero_ultimo(lenguajes))


