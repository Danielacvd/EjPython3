"""
Obtener el porcentaje de otro numero, pido numero y que porciento lo quiero sacar a ese numero
"""
#Try1
n = int(input("Ingresa un numero: "))
porciento = int(input("Ingresa que porcentaje del numero quieres: "))
res = (n*porciento)/100
print(f"El {porciento} porciento de {n} es: {res}")
