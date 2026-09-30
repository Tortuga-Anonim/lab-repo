'''
EJERCICIO 5: Comparaciones
    1. Almacena dos números en variables diferentes.
    2. Evalúa:
       - igualdad
       - diferencia
       - mayor que
       - menor que
    3. Muestra los resultados
'''

# Escriba su solución
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

igualdad = numero1 == numero2
diferencia = numero1 != numero2
mayor_que = numero1 > numero2
menor_que = numero1 < numero2

print(f"¿{numero1} es igual a {numero2}? {igualdad}")
print(f"¿{numero1} es diferente de {numero2}? {diferencia}")
print(f"¿{numero1} es mayor que {numero2}? {mayor_que}")
print(f"¿{numero1} es menor que {numero2}? {menor_que}")
