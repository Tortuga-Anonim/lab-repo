# Clase 1: Ejercicios de Python y Git

## PARTE 1

### Temas
- Variables y constantes
- Tipos de datos primitivos: `int`, `float`, `bool`, `str`
- Expresiones aritméticas
- Expresiones lógicas
- Operadores
- Entradas y salidas
- Listas
- Condicionales

### Instalacion de Python en Windows

1. Abre la pagina oficial: `https://www.python.org/downloads/windows/`
2. Descarga Python 3 para Windows.
3. Ejecuta el instalador.
4. Marca la opcion `Add python.exe to PATH`.
5. Haz clic en `Install Now`.
6. Al terminar, abre `cmd` o `PowerShell`.
7. Verifica la instalacion:

```bash
python --version
```

Si no funciona, prueba:

```bash
py --version
```

### Como ejecutar un ejercicio

```bash
python ejercicios/ejercicio_01_presentacion.py
```

o en Windows:

```bash
py ejercicios/ejercicio_01_presentacion.py
```

### Nota para los estudiantes

Cada archivo contiene solo el enunciado del ejercicio. La resolucion se hace escribiendo el codigo desde cero. Se recomienda:
1. Resolver del 1 al 10 en una primera parte.
2. Resolver del 11 al 15 en una segunda parte, ya que en esta parte de la clase se explicará git también
3. Cambien los valores de los ejercicios y observen como cambia la salida.

### Secuencia de ejercicios

1. `ejercicio_01_presentacion.py`: crear variables básicas.
2. `ejercicio_02_tipos.py`: usar `int`, `float`, `bool`, `str`
3. `ejercicio_03_radio.py`: usar constantes en una expresión matemática.
4. `ejercicio_04_calculadora.py`: entradas de usuario y expresiones aritmeticas.
5. `ejercicio_05_comparaciones.py`: operadores de comparacion.
6. `ejercicio_06_division.py`: operadores relacionados a la división.
7. `ejercicio_07_divisible.py`: residuo de una division y condicionales.
8. `ejercicio_08_operaciones_logicas.py`: operaciones logicas con datos de tipo `bool`.
9. `ejercicio_09_rango.py`: aplicacion practica de operaciones logicas y condicionales.
10. `ejercicio_10_valor_absoluto.py`: comparaciones, condicionales y funciones integradas.
11. `ejercicio_11_listas.py`: listas y modulo.
12. `ejercicio_12_promedio.py`: listas, condicionales y funciones integradas.
13. `ejercicio_13_iva.py`: aplicacion de operaciones y constantes.
14. `ejercicio_14_descuentp.py`: aplicacion de operaciones y condicionales.
15. `ejercicio_15_coordenadas.py`: aplicacion de condicionales.

## PARTE 2

### Temas
- Git y GitHub

### Ejercicio 1
1. Inicien un repositorio local del laboratorio que realizaron en la primera parte.
```bash
git init
```
2. En el ejercicio 1 de la primera parte (`ejercicio_01_presentacion.py`), modifiquen los valores de las variables
4. Agregen los cambios al area de staging
```bash
git add .
```
5. Hagan un commit de los cambios
```bash
git commit -m "mensaje descriptivo de los cambios"
```
6. Creen un repositorio en su GitHub
7. Conecten su repositorio local con el nuevo repositorio remoto (los comandos se encuentran en gitHub)
```bash
git remote add origin link_del_repositorio
git branch -M main
git push -u origin main
```
8. Observe la actualización del repositorio en su github
9. Creen una rama nueva en local
```bash
git branch new
```
10. Cambien a esa rama que crearon
```bash
git checkout new
```
11. Vuelvan a modificar los valores de las variables en el primer ejercicio
12. Agreguen los cambios al staging area
13. Hagan commit de los nuevos cambios 
14. Publiquen la rama local al repo remoto
```bash
git push origin new
```

### Ejercicio 2
1. Entren en un nuevo directorio para crear un nuevo proyecto
2. Clonen el repositorio del laboratorio
```bash
git clone https://github.com/UMA-Programacion-I/lab1.git
```
3. Cambien de dirección a la carpeta del proyecto
```bash
cd lab1
```
4. Creen una rama cuyo nombre sea su APELLIDO (ejemplo con mi apellido)
```bash
git branch lerones
```
5. Cambien a la rama de su apellido
```bash
git checkout lerones
```
6. Copien la carpeta 'ejercicios' con sus soluciones de la parte 1 del laboratorio en el directorio donde se encuentran
7. Manden los cambios al staging area
8. Hagan commit de los cambios
9. Publiquen la rama
```bash
git push origin lerones
```

NOTA: Además de la publicación en github dentro de la organización del curso, creen un zip de la carpeta lab1 que tenga la carpeta .git, el README original y la carpeta de ejercicios con sus soluciones. Este archivo lo deben publicar en el classroom
también