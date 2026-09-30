'''
EJERCICIO 9: rango
    1. Crea una variable 'nota'.
    2. Si la nota está entre 0 y 10 (no incluído), muestre que ha reprobado
    3. Si la nota está entre 10 y 20, muestre que ha aprobado
    4. Si la nota está fuera del rango 0-20, indique que la escala de la nota es incorrecta

    NOTA: Haga las evaluaciones condicionales utilizando expresiones con 'and' y 'or' según sea el caso
'''

# Escriba su solución
nota = float(input("Ingrese la nota: "))

if nota < 0 or nota >= 20:
    print("La escala de la nota es incorrecta.")
elif nota < 10:
    print("Reprobaste")
else:
    print("Aprobaste!!!")
