'''
EJERCICIO 13: IVA
    1. Usa la constante 'IVA'.
    2. Crea una variable 'precio'.
    3. Calcula el impuesto.
    4. Calcula el monto total.
'''

# Escriba su solución
iva = 16
precio = float(input("Ingrese el precio del producto en dolares: "))
def calculo_de_iva(precio, iva):
    impuesto = precio * iva / 100
    monto_total = precio + impuesto
    return impuesto, monto_total
print(f"El impuesto es: {calculo_de_iva(precio, iva)[0]}")
print(f"El monto total es: {calculo_de_iva(precio, iva)[1]}")
