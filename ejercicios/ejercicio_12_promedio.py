'''
EJERCICIO 12: Promedio
    1. Crea una lista con 3 notas
    2. Calcula el promedio de las notas sin utilizar funciones integradas
    3. Muestra el resultado.
    4. Calcula el promedio de las notas con funciones integradas
    5. Muestre el resultado.

    Qué le pasa a tu algoritmo si se modifica la longitud de la lista?
'''

# Escriba su solución
lista_notas = []
print("Por favor, introduce 3 notas:")
for i in range(3):
    numero = float(input(f"Introduce la nota {i + 1}: "))
    lista_notas.append(numero)
print(f"\nTu lista es:{lista_notas}")
def calcular_promedio(lista):
    suma = 0
    for nota in lista:
        suma += nota
    promedio = suma / len(lista)
    return promedio
print(f"El promedio de las notas es: {calcular_promedio(lista_notas)}")
