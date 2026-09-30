'''
EJERCICIO 11: Listas
    1. Cree una lista con 5 números enteros.
    2. Evalúe uno a uno cuáles de los elementos son múltiplos de 7
    3. Muestre en pantalla una lista de estos elementos.
'''

# Escriba su solución

lista = []
print("Por favor, introduce 5 números:")
for i in range(5):
    numero = float(input(f"Introduce el número {i + 1}: "))
    lista.append(numero)
print(f"\nTu lista es:{lista}")

multiplos_de_7 = []
for num in lista:
    if num % 7 == 0:
        multiplos_de_7.append(num)
print(f"Los múltiplos de 7 en la lista son: {multiplos_de_7}")
