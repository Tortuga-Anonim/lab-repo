"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
frase = input("Ingrese una frase: ")
vocales = "aeiouáéíóúü"
contador = 0

for letra in frase:
    if letra.lower() in vocales:
        contador += 1

if contador == 0:
    print("La frase no tiene vocales.")
elif contador == 1:
    print("La frase tiene 1 vocal.")
else:
    print(f"La frase tiene {contador} vocales.")