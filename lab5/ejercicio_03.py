"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""


def dias_del_mes(mes):
    if mes == 2:
        return 28
    elif mes in (4, 6, 9, 11):
        return 30
    else:
        return 31


def dia_del_anio(mes, dia):
    total = 0
    for m in range(1, mes):
        total += dias_del_mes(m)
    return total + dia


mes = int(input("Ingrese el mes actual (1-12): "))
while mes < 1 or mes > 12:
    print("Mes inválido, debe estar entre 1 y 12.")
    mes = int(input("Ingrese el mes actual (1-12): "))

maximo = dias_del_mes(mes)
dia = int(input("Ingrese el día actual: "))
while dia < 1 or dia > maximo:
    print(f"Día inválido, el mes {mes} tiene {maximo} días.")
    dia = int(input("Ingrese el día actual: "))

resultado = dia_del_anio(mes, dia)
print(f"Hoy es el día {resultado} del año.")
