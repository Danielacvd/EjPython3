# Ejercicio 18: Calcular la suma de tres números, e incluir una condición de igualdad.
# Calcula la suma de tres números. Si los tres números son iguales, la suma se multiplica por 3.
#Try1

i = 0
numeros = []
while i <3:
    numeros.append(int(input("Ingresa un numero: ")))
    i += 1
else:
    if numeros[0] == numeros[1] and numeros[1] == numeros[2]:
        print(f"La suma es:{sum(numeros)*3}")
    else:
        print(f"La suma es:{sum(numeros)}")


