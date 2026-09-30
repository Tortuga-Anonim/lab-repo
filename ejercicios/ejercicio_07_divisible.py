'''
EJERCICIO 7: Divisible
    Escribir un programa que, dado dos números enteros, el programa pruebe si el primero es divisible entre el segundo.
    Muestre en pantalla 'Sí' (si es divisible) o 'No' (si no es divisible)
'''

# Escriba su solución
numero_entero1 = int(input("Ingrese el primer número entero: "))
numero_entero2 = int(input("Ingrese el segundo número entero: "))

if numero_entero2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    if numero_entero1 % numero_entero2 == 0:
        print("Sí, el primer número es divisible entre el segundo.")
    else:
        print("No, el primer número no es divisible entre el segundo.")
