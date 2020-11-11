"""
Mostrar todos los numeros impares que hay entre 2 numero que decida el user
"""
#Try1
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

if num1 >= num2:
    print("El primer numero debe ser menor al segundo")
else:    
    for i in range(num1, num2):
        if not i % 2 == 0:
            print(i)
    else:
        print(f"Esos son los numeros impares estre {num1} y {num2}")        