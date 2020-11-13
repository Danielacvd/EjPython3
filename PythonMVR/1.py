"""
#1- Crear 2 variables, pais, continente, imprimir sus valores por pantalla, muestra el tipo de dato de cada variable
"""

#Try1
pais = "Chile"
continente = "LA"
print(f"Pais: {pais}, Contienente: {continente}")
print(f"Tipo de dato de variable pais: {type(pais)}\nTipo de dato variable contienente: {type(continente)}")

#Try2
pais = lambda pais: f"Pais: {pais}, tipo de dato: {type(pais)}"
continente = lambda continente: f"Contienen: {continente}, tipo de dato: {type(continente)}"

print(pais('Chile'))
print(continente('LA'))