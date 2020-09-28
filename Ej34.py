# Ejercicio 34: Validar Dos Números. Si son iguales o la suma o el valor absoluto son 5.
#Try1

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))

if n1 == n2 or n1 + n2 == 5 or abs(n1+n2) == 5:
    print(True)
else:
    print(False)

