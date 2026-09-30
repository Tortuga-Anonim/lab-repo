'''
EJERCICIO 14: Descuento
    Con una tasa de impuestos constante del 8%, el precio de una compra (en $) y el estado del cliente (si es estudiante o no),
    calcule y muestre subtotal, descuento, impuesto y total final de la compra. Tenga en cuenta que:
        1. Si el precio de la compra supera los 100$, se aplica un descuento del 10%
        2. Si el cliente es estudiante, se aplica un descuento adicional del 5% sobre cualquier descuento anterior
        3. El impuesto sobre las ventas se añade luego de aplicados los descuentos correspondientes

'''

# Escriba su solución
tasa_de_impuestos = 8
precio_de_compra = float(input("Ingrese el precio de la compra en dolares: "))
estudiante = input("¿Es el cliente un estudiante? (s/n): ").lower() == "s"
def calculo_de_descuento(precio, estudiante, tasa_de_impuestos):
    descuento = 0
    if precio > 100:
        descuento += precio * 10 / 100
    else:
        print("El monto no aplica para el descuento del 10%")
    if estudiante:
        descuento += (precio - descuento) * 5 / 100
    subtotal = precio - descuento
    impuesto = subtotal * tasa_de_impuestos / 100
    total_final = subtotal + impuesto
    return subtotal, descuento, impuesto, total_final
subtotal, descuento, impuesto, total_final = calculo_de_descuento(precio_de_compra, estudiante, tasa_de_impuestos)
print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Impuesto: {impuesto}")
print(f"Total final: {total_final}")
