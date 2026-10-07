"""
EJERCICIO 02: Sumatoria

1. Pide números enteros al usuario constantemente usando un bucle while. 
2. Suma los valores ingresados.
3. Detén el bucle únicamente cuando el usuario ingrese el número 0. 
4. Al final, muestra la suma total.
"""

suma = 0
texto = input("Ingrese un numero entero: ")

while texto != "0":
    if texto.isdigit():
        suma += int(texto)
    else:
        print("Por favor ingrese un numero entero")
    texto = input("Ingrese un numero entero: ")

print(f"La suma total es: {suma}")
