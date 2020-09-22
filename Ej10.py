# Ejercicio 10: Solicitar al usuario un número n y calcular n + nn + nnn
#Try1
# n = 3 => 3 + 33 + 333 = 369

num = input("Ingresa un numero: ")
res = int(num) + int((num+num)) + int((num+num+num))
print(res)
