"""
Mostrar todos los numeros entre 2 numeros que le usuario diga.
"""

#Try1

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))


if num1 >=num2:
    print("El primero numero debe ser menor al segundo")
else:    
    for i in range(num1+1, num2):
        print(i)
    else:
        print(f"Estos son los numero entre {num1} y {num2}")