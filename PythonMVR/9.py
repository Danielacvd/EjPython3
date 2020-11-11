"""
El programa nos pide indefinidamente un numero hasta ingresar el 97, ahi se detiene, muestra por pantalla los que voy introduciendo
"""
#Para otro Try hacer que un random intente adivinar, revisar cuantas veces se demoro...
#Try1

while(True):
    n = int(input("Ingresa el numero secreto: "))
    if n == 97:
        print("Adivinaste el numero GRATZZZZ!!!!")
        break
    