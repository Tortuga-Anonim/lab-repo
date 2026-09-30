'''
EJERCICIO 6: División
    1. Cree dos variables de tipo 'int'
    2. Muestre las distintas partes la división: dividendo, divisor, resto y cociente
    3. Utilice siempre el número mayor como el dividendo.
    4. Muestre como con el divisor, resto y cociente se consigue el dividendo

    Ejemplo: con 57 y 5
        Dividendo: 57
        Divisor: 5
        Cociente: 11
        Resto: 2
        El número 57 es 5 veces 11 más 2
'''

# Escriba su solución
variable1 = int(input("Ingrese el primer número: "))
variable2 = int(input("Ingrese el segundo número: "))

dividendo = max(variable1, variable2)
divisor = min(variable1, variable2)
cociente = dividendo // divisor
resto = dividendo % divisor

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Cociente: {cociente}")
print(f"Resto: {resto}")
print(f"El número {dividendo} es {divisor} veces {cociente} más {resto}")
