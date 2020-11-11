"""
Mostrar todas las tablas de multiplicar que hay desde el 1 al 10
"""

#Try1
for i in range(1, 11):
    print(f"\nTabla de multiplicar del {i}")
    for e in range(1, 11):
        print(f"{i} * {e} = {i*e}") 
