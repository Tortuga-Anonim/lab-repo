"""
EJERCICIO 01: Calculadora de Propina y División de Cuenta

Escribe una función llamada calcular_total_persona(subtotal, porcentaje_propina=10, personas=1) que:
    1. Calcule el monto de la propina en base al subtotal y al porcentaje dado.
    2. Sume la propina al subtotal para obtener el total general.
    3. Divida el total general entre el número de personas.
    4. Retorne el valor que le corresponde pagar a cada persona (redondeado a 2 decimales usando round()).

Ejemplos de casos de prueba:
    - calcular_total_persona(100, 15, 4) -> Debe retornar 28.75
    - calcular_total_persona(50) -> Debe retornar 55.0 (usando valores por defecto: 10% de propina, 1 persona).
"""
def calcular_total_persona(subtotal, porcentaje_propina=10, personas=1):
    propina = subtotal * (porcentaje_propina / 100)
    total_general = subtotal + propina
    total_por_persona = total_general / personas
    return round(total_por_persona, 2)

print(f"El total por persona es: {calcular_total_persona(100, 15, 4)}")
print(f"El total por persona (valores por defecto) es: {calcular_total_persona(50)}")
