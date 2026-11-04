# Laboratorio: Sistema de Administración de Empleados

### Desarrollar un programa modular en Python que permita:
1.	Registrar empleados
2.	Consultar información básica
3.	Calcular estadísticas utilizando diccionarios de python.

 
### Descripción General
En este laboratorio vas a construir un pequeño sistema de administración de empleados que se ejecuta desde consola.

El programa permitirá registrar empleados, mostrar información del personal, buscar por departamento, aplicar aumentos salariales y visualizar estadísticas generales.

El sistema estará dividido en cuatro **módulos** principales:
1.	captura.py → Registro de empleados.
2.	funcionalidad.py → Operaciones sobre los datos.
3.	estadisticas.py → Cálculo y visualización de estadísticas.
4.	main.py → Programa principal (menú interactivo).
 
### Estructura y Requisitos

### captura.py — Registro de empleados
Este módulo se encargará de ingresar la información de los empleados. Cada empleado debe tener los siguientes datos:

- Nombre
- Edad
- Salario mensual
- Departamento

Los datos deben almacenarse en una lista de diccionarios:

```python
empleados = [] # Donde voy almacenar la informacion
empleado = {
  "nombre": "Daniela",
  "edad": 25,
  "salario": 900,
  "dpto": "IT"
} # La informacion puntual de un empleado
empleados.append(empleado) # Guardando la info
```
 
### funcionalidad.py — Operaciones
Contendrá las funciones que permiten trabajar con las listas de empleados. Debe incluir al menos las siguientes funciones:

- **listar_empleados(empleados)**: Muestra la información de todos los empleados registrados.
- **buscar_por_departamento(empleados, dpto_a_buscar)**: Solicita un nombre de departamento y muestra los empleados que pertenecen a él.
- **aplicar_aumento_salarial(empleados, empleado_a_buscar)**: Solicita un porcentaje y aplica un aumento proporcional al salario del empleado especificado.
- **obtener_promedio_salarial(empleados)**: Calcula el salario promedio general
 
### estadisticas.py — Estadísticas generales
Muestra información agregada sobre los empleados:
- Cantidad total de empleados.
- Edad promedio.
- Cantidad de empleados con edad menor a 30.
- Salario promedio.
- Salario máximo y mínimo.
- Indicar si algún salario supera los 1000.


**Tip:** recuerden que pueden utilizar `list comprehensions` o funciones como `map, filter, reduce, etc.`
 
### main.py — Programa principal
Debe contener un menú que permita ejecutar las opciones de los otros módulos.
El menú debe repetirse hasta que el usuario elija la opción “6. Salir”.
Ejemplo de menú:

```python
=== Menú Principal ===
1. Ingresar empleados # Pedimos la informacion del empleado a ingresar
2. Mostrar empleados
3. Buscar por departamento # Pedimos el nombre del dpto a buscar
4. Aplicar aumento salarial # Pedimos el nombre del empleado a buscar
5. Mostrar estadísticas
6. Salir
```
