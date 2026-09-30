'''
EJERCICIO 3: Constantes y expresiones
    1. Cree una variable que represente el radio de un círculo
    2. Use pi como constante.
    3. Calcula el area del círculo.
    4. Calcule el perímetro del círculo

    Formulas:
        area = pi x radio^2
        perimetro = 2 x pi x radio
'''

# Escriba su solución


import math


rad = 21
pi = math.pi

area = pi * rad ** 2
perimetro = 2 * pi * rad

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")
