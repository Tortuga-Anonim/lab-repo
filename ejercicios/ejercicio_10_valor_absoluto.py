'''
EJERCICIO 10: Valor absoluto
    1. Sin utilizar la función de valor absoluto que viene incluida con Python, implemente la siguiente función
        x →|x^2-x-1|+|x-2|-3|x^4-x^2-x+1|
    2. Muestre el resultado
    3. Luego, realice la implementación con la función integrada de Python y compare ambos algoritmos
'''

# Escriba su solución
x = float(input("Ingrese un valor para x: "))
def calculo_de_valor_absoluto(x):

    calculo1 = ((x**2 - x - 1) ** 2) ** 0.5
    calculo2 = ((x - 2) ** 2) ** 0.5
    calculo3 = ((x**4 - x**2 - x + 1) ** 2) ** 0.5

    return calculo1 + calculo2 - 3 * calculo3
print(f"El resultado de la función es: {calculo_de_valor_absoluto(x)}")
