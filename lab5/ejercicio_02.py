"""
EJERCICIO 02: Validación de contraseña segura

Implementa una función que reciba una contraseña y verifique: 
    1. Que tenga al menos 8 caracteres de longitud.
    2. Que contenga al menos un número (puedes usar un bucle o una verificación con dígitos).
    3. Que contenga al menos una letra mayúscula.

La función debe retornar True si cumple todas las condiciones, y False en caso contrario. 
(Ayuda: puedes crear funciones auxiliares pequeñas para cada validación, fomentando la modularidad de tu programa).

Ejemplos de casos de prueba:
    - es_contrasena_segura("Python123") -> True
    - es_contrasena_segura("clave") -> False
    - es_contrasena_segura("12345678") -> False
"""

def tiene_longitud_minima(contrasena):
    return len(contrasena) >= 8


def tiene_numero(contrasena):
    for caracter in contrasena:
        if caracter.isdigit():
            return True
    return False


def tiene_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False


def es_contrasena_segura(contrasena):
    return (tiene_longitud_minima(contrasena)
            and tiene_numero(contrasena)
            and tiene_mayuscula(contrasena))


print(es_contrasena_segura("Python123"))
print(es_contrasena_segura("clave"))
print(es_contrasena_segura("12345678"))

contrasena = input("Ingrese su contraseña: ")
if es_contrasena_segura(contrasena):
    print("La contraseña es segura")
else:
    print("La contraseña NO es segura")
