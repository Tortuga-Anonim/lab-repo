'''
EJERCICIO 8:
    1. Crea dos variables de tipo booleano.
    2. Combínalas con 'and y 'or' (por separado)
    3. Realiza la negación (not) de ambos
    4. Muestra los resultados
'''

# Escriba su solución
boolean1 = True
boolean2 = False

boolean1_and_boolean2 = boolean1 and boolean2
boolean1_or_boolean2 = boolean1 or boolean2
not_boolean1 = not boolean1
not_boolean2 = not boolean2

print(f"El valor de la variable booleana1 es: {boolean1}")
print(f"El valor de la variable booleana2 es: {boolean2}")
print(f"El resultado de {boolean1} AND {boolean2} es: {boolean1_and_boolean2}")
print(f"El resultado de {boolean1} OR {boolean2} es: {boolean1_or_boolean2}")
print(f"La negación de {boolean1} es: {not_boolean1}")
print(f"La negación de {boolean2} es: {not_boolean2}")
