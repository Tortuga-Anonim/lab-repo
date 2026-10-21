"""
EJERCICIO 04: Reporte de notas

Crea un paquete llamado paquete_academico con la siguiente jerarquía de archivos:

paquete_academico/
│
├── __init__.py
├── operaciones.py
└── reportes.py

1. En operaciones.py, define las funciones:
    calcular_promedio(lista_notas): Retorna el promedio de una lista de números.
    encontrar_maximo(lista_notas): Retorna la nota más alta de una lista de números.

2. En reportes.py, define la función:
    generar_resumen(lista_notas): Utiliza las funciones de operaciones.py para imprimir un reporte en consola con 
    el promedio y la nota máxima.

3. En tu script principal (este archivo, ejercicio_04.py, que se encuentra fuera del paquete), importa los submódulos 
del paquete y prueba generar un resumen para una lista de notas de ejemplo (por ejemplo: [85, 90, 78, 92, 88]).
"""

from funciones import operaciones, reportes

notas = [85, 90, 78, 92, 88]
reportes.generar_resumen(notas)
