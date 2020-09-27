# Ejercicio 29: Calcular el área de un triángulo.
#Try1
#Base*altura/2

datos = []

for i in range(2):
    datos.append(float(input("ingresa los datos, Base y Altura: ")))


print(f"El area del triangulo es: {(datos[0]*datos[1]/2)}")