"""
EJERCICIO 06: Compresión de una imagen

Se tiene una imagen de pixeles en blanco y negro de dimensión 1xn. Para efectos prácticos de este ejercicio, esta imagen está
representada por una lista de tamaño n, donde cada posición representa el valor del pixel correspondiente. 

Primero, se quiere verificar que los valores dentro de la imagen sean correctos. Para imágenes en blanco y negro, cada pixel 
ocupa un byte de información. Esto significa que cada valor puede tomar valores entre 0 y 255 (ambos incluídos). Recorra la 
imagen proporcionada y verifique que los valores en cada pixel estan en el rango esperado:
    - Si el valor < 0, reemplace por 0
    - Si el valor > 255, reemplace por 255
    - Si el valor está dentro del rango, mantiene su valor
    - Lleva un conteo de cuantos pixeles modificas

Una vez verificada la imagen, se desea comprimir en función a un número ingresado por el usuario. Aunque existen distintos métodos
de compresión, en este programa se quiere usar la compresión por promedio en bloques deslizantes. Esta consiste en escoger un 
número k entero, donde 1 <= k <= n, que representa el tamaño del bloque seleccionado para promediar, es decir, la cantidad de pixeles
de la imagen original que se van a agrupar para formar un pixel en la imagen comprimirda. Considere que se avanza una posición por
cada promedio a realizar (step). Los valores de los extremos solo se utilizan una vez.

Ej: 
    imagen = [50, 62, 75, 2, 5]
    Con k = 1:
    imagen_comprimida = [50, 62, 75, 2, 5]
    Con k = 2:
    imagen_comprimida = [promedio(50, 62), promedio(62, 75), promedio(75, 2), promedio(2, 5)]
    imagen_comprimida = [52              , 68.5            , 38.5           , 3.5           ]
    Con k = 3:
    imagen_comprimida = [promedio(50, 62, 75), promedio(62, 75, 2), promedio(75, 2, 5)]
    imagen_comprimida = [62.33               , 46.33              , 27.33             ]
    Con k = 4:
    imagen_comprimida = [promedio(50, 62, 75, 2), promedio(62, 75, 2, 5)]
    imagen_comprimida = [47.25                  , 35.25                 ]
    Con k = 5:
    imagen_comprimida = [promedio(50, 62, 75, 2, 5)]
    imagen_comprimida = [38.80                     ]

Nota: Vea que hay una relación entre n, k y n_comp, donde n_comp es el tamaño de la lista comprimida ( k = n - n_comp + 1 )

Pídale al usuario que ingrese el tamaño deseado de la imagen comprimida (n_comp). 
    - Use try/except para evitar que se pare la ejecución si el usuario ingresa algún caracter no numérico
    - Utilice while para asegurar que el numero ingresado no sea mayor al tamaño original y no sea negativo
    - Si el usuario ingresa 0, la imagen comprimida es una lista vacía
    - Si la entrada está bien, haga la compresión de la lista. Esta debe ser de numeros enteros.

Finalmente, muestra el resultado en pantalla: la imagen comprimida y el contador de los pixeles modificados en la imagen original

"""

#########################################################################################################################
## PARTE 1: Definición de imagen

imagen = [100, 98, -3, 0, 56, 86, 7, 300, 255, 256, 35, -621, -1, 50, 126, 201]

#########################################################################################################################
## PARTE 2: Verificación de la imagen

pixeles_modificados = 0

for posicion in range(len(imagen)):
    if imagen[posicion] < 0:
        imagen[posicion] = 0
        pixeles_modificados += 1
    elif imagen[posicion] > 255:
        imagen[posicion] = 255
        pixeles_modificados += 1

#########################################################################################################################
## PARTE 3: Pedir nuevo tamaño deseado

tamano_original = len(imagen)

while True:
    try:
        tamano_comprimido = int(input(f"Ingrese el tamaño de la imagen comprimida (0 a {tamano_original}): "))
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")
        continue

    if tamano_comprimido < 0:
        print("El tamaño no puede ser negativo.")
    elif tamano_comprimido > tamano_original:
        print(f"El tamaño no puede ser mayor que el de la imagen original ({tamano_original}).")
    else:
        break

#########################################################################################################################
## PARTE 4: Compresión de la imagen

imagen_comprimida = []

if tamano_comprimido > 0:
    tamano_bloque = tamano_original - tamano_comprimido + 1

    for inicio in range(tamano_comprimido):
        suma_bloque = 0
        for posicion in range(inicio, inicio + tamano_bloque):
            suma_bloque += imagen[posicion]
        imagen_comprimida.append(round(suma_bloque / tamano_bloque))

#########################################################################################################################
## PARTE 5: Mostrar resultados

print(f"Imagen verificada: {imagen}")
print(f"Imagen comprimida: {imagen_comprimida}")
print(f"Pixeles modificados en la imagen original: {pixeles_modificados}")
