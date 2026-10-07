# LABORATORIO 4

## INSTRUCCIONES

En cada archivo .py dentro de esta carpeta encontrará el enunciado correspondiente a cada ejercicio del laboratorio.
Debe realizar los 6 ejercicios planteados en cada uno de los archivos.

Al finalizar, suban sus soluciones a un repostiorio remoto en GitHub. 

Deben entregar la carpeta comprimida (.zip) con sus soluciones en la asignación de Classroom, junto con el link al repositorio donde subieron sus programas.

## EJERCICIO 01: Tabla de multiplicar
1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for

## EJERCICIO 02: Sumatoria
1. Pide números enteros al usuario constantemente usando un bucle while. 
2. Suma los valores ingresados.
3. Detén el bucle únicamente cuando el usuario ingrese el número 0. 
4. Al final, muestra la suma total.

## EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales que tiene la palabra.

## EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.

## EJERCICIO 05: Menú de cómputo geométrico

**Complete las funciones** para que al ejecutar el programa, se muestre el menú y se le pida al usuario ingresar una de las opciones (1 - 4). 
- Si escoge 1, se pide ingresar el valor del radio, se calcula el radio y se muestra en pantalla
- Si se escoge 2, se pide ingresar el valor de la base y la altura, se calcula el area del rectángulo y se muestra en pantalla
- Si se escoge 3, se pide ingresar el valor de la base y la altura, se calcula el perímetro del rectángulo y se muestra en pantalla
- Si se escoge 4, se sale del menú y termina el programa
- Si se ingresa cualquier otra opcion, se imprime "Opción inválida. Intente de nuevo."

## EJERCICIO 06: Compresión de una imagen

Se tiene una imagen de pixeles en blanco y negro de dimensión 1xn. Para efectos prácticos de este ejercicio, esta imagen está representada por una lista de tamaño n, donde cada posición representa el valor del pixel correspondiente. 

Primero, se quiere **verificar que los valores** dentro de la imagen sean correctos. Para imágenes en blanco y negro, cada pixel ocupa un byte de información. Esto significa que cada valor puede tomar valores entre 0 y 255 (ambos incluídos). Recorra la imagen proporcionada y verifique que los valores en cada pixel estan en el rango esperado:
- Si el valor < 0, reemplace por 0
- Si el valor > 255, reemplace por 255
- Si el valor está dentro del rango, mantiene su valor
- Lleva un conteo de cuantos pixeles modificas

Una vez verificada la imagen, se desea comprimir en función a un número ingresado por el usuario. Aunque existen distintos métodos de compresión, en este programa se quiere usar la compresión por promedio en bloques deslizantes. Esta consiste en escoger un número k entero, donde 1 <= k <= n, que representa el tamaño del bloque seleccionado para promediar, es decir, la cantidad de pixeles de la imagen original que se van a agrupar para formar un pixel en la imagen comprimirda. Considere que se avanza una posición por cada promedio a realizar (step). Los valores de los extremos solo se utilizan una sola vez.

Ej: imagen = [50, 62, 75, 2, 5]
- Con k = 1:
    - imagen_comprimida = [50, 62, 75, 2, 5]
- Con k = 2:
    - imagen_comprimida = [promedio(50, 62), promedio(62, 75), promedio(75, 2), promedio(2, 5)]
    - imagen_comprimida = [52              , 68.5            , 38.5           , 3.5           ]
- Con k = 3:
    - imagen_comprimida = [promedio(50, 62, 75), promedio(62, 75, 2), promedio(75, 2, 5)]
    - imagen_comprimida = [62.33               , 46.33              , 27.33             ]
- Con k = 4:
    - imagen_comprimida = [promedio(50, 62, 75, 2), promedio(62, 75, 2, 5)]
    - imagen_comprimida = [47.25                  , 35.25                 ]
- Con k = 5:
    - imagen_comprimida = [promedio(50, 62, 75, 2, 5)]
    - imagen_comprimida = [38.80                     ]

**Nota:** Vea que hay una relación entre *n*, *k* y *n_comp*, donde *n_comp* es el tamaño de la lista comprimida ( k = n - n_comp + 1 )

Pídale al usuario que **ingrese el tamaño deseado de la imagen comprimida (n_comp)**. 
- Use try/except para evitar que se pare la ejecución si el usuario ingresa algún caracter no numérico
- Utilice while para asegurar que el numero ingresado no sea mayor al tamaño original y no sea negativo
- Si el usuario ingresa 0, la imagen comprimida es una lista vacía
- Si la entrada está bien, **haga la compresión de la lista**. Esta debe ser de numeros enteros.

Finalmente, **muestra el resultado en pantalla**: la imagen comprimida y el contador de los pixeles modificados en la imagen original
