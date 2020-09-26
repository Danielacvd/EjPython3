# Ejercicio 17: Crear una función para determinar si un número es cercano a 1000 o 2000.
#Try1

def cercano(n):
    if n <= 1000:
        if n == 1000:
            print("El numero es 1000")
        else:    
            print(f"El numero {n} es cercano a 1000")
    else:
        print(f"El numero {n} es cercano a 2000") 

numero = int(input("Ingresa un numero: "))           
cercano(numero)