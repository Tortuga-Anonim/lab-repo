"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""
numero_secreto = hash("semilla") % 1000000 + 1
intentos = 0

while True:
    texto = input("Adivine el número (1 a 1000000): ")

    if not texto.isdigit():
        print("Por favor ingrese un numero entero")
        continue

    intento = int(texto)
    intentos += 1

    if intento < numero_secreto:
        print("El número buscado es mayor")
    elif intento > numero_secreto:
        print("El número buscado es menor")
    else:
        print(f"¡Adivinaste en {intentos} intentos!")
        break


