'''
EJERCICIO 4: Calculadora
    1. Pídale al usuario ingresar dos numeros.
    2. Calcula su suma, resta, multiplicación y división de los números ingresados
    4. Muestre los resultados
'''

# Escriba su solución
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    division = num1 / num2
    print(f"La división de {num1} y {num2} es: {division}")

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
