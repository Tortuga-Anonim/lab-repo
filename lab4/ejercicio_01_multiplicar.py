"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""
num = float(input("ingrese un numero: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")