## Pregunta 1 – Parseo de productos (procesamiento por lotes)

#### **Contexto general**
Una tienda guarda los datos de su inventario como líneas de texto separadas por comas con el formato:
`codigo,nombre,precio,cantidad`

Se necesita procesar una lista completa de líneas, extraer la información de cada producto y generar reportes útiles (resúmenes por producto, total del inventario, etc.)

#### **Funciones a implementar**

1) `parsear_producto(linea: str) -> dict`
   - Convierte una línea en el diccionario `{"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}`.
   - Valida formato y tipos. Esta función es la base del resto.
   - Implementación:
     - Validar que line sea str. Si no, raise ValueError (⚠️ Googlear).
     - Separar por comas con `.split(",")` (⚠️ Googlear). Debe haber exactamente 4 elementos; si no, raise ValueError.
     - Limpiar espacios alrededor de cada campo con `.strip()` (⚠️ Googlear).
     - Convertir:
       - precio → float. Si falla la conversión o precio < 0, raise ValueError.
       - cantidad → int. Si falla la conversión o cantidad < 0, raise ValueError.
       - Retornar el diccionario `{"codigo" : codigo, "nombre" : nombre, "precio" : precio, "cantidad" : cantidad}`.

2) `resumen_de_producto(linea: str) -> str`
   - Usa parsear_producto y devuelve: `"CODIGO - NOMBRE: $VALOR"` con `VALOR = precio * cantidad` (redondeado a 1 decimal).
   - Implementación:
     - Llamar a parsear_producto(linea) para obtener los 4 valores.
     - Calcular valor = precio * cantidad y redondear a 1 decimal.
     - Retornar el string con formato exacto:
       - "{codigo} - {nombre}: ${valor_redondeado}".

3) `_validar_lineas(lineas: list) -> void` (función de ayuda interna)
   - Verifica que lineas sea lista no vacía y que cada elemento sea str.
   - Levanta ValueError si no cumple.
   - Implementación:
     - Verificar que lineas sea una lista y no esté vacía.
     - Recorrer con un for: cada elemento debe ser str; si alguno no lo es → raise ValueError.

4) `resumen_de_lotes(lineas: list) -> list`
   - Devuelve una lista con los resúmenes de cada producto.
   - Debe llamar a `resumen_de_producto` por cada línea (for loop).
   - Implementación:
     - Llamar a _validar_lineas(lineas).
     - Crear una lista vacía salida.
     - Recorrer lineas con un for:
     - Para cada linea, llamar resumen_de_producto(linea) y agregar el resultado a salida.
     - Retornar salida.

5) `valor_de_lote(lineas: list) -> float`
   - Devuelve el valor total del inventario (suma de precio * cantidad de todas las líneas), redondeado a 1 decimal.
   - Debe llamar a parsear_producto para cada línea.
   - Implementación:
     - Llamar a _validar_lineas(lineas).
     - Iniciar total = 0.0
     - Recorrer lineas con un for:
     - Llamar parsear_producto(linea) para obtener precio y cantidad.
     - Acumular total += precio * cantidad.
     - Retornar round(total, 1).

6) `producto_maximo_valor(lineas: list) -> str`
   - Devuelve el resumen del producto con mayor precio * cantidad.
   - En caso de empate, devuelve el primero que alcanza el máximo.
   - Debe reutilizar parsear_producto (y formatear igual que resumen_de_producto).
   - Implementación:
     - Llamar a _validar_lineas(lineas).
     - Inicializar variables con el primer producto válido (usando parsear_producto).
     - Recorrer el resto de las líneas:
     - Calcular valor = precio * cantidad.
     - Si valor es mayor al mejor actual, actualizar el mejor.
     - En caso de empate, no actualizar (se queda el primero).
     - Al final, formatear la respuesta igual que resumen_de_producto (con 1 decimal) y retornarla.

Debe escribir las funciones en el archivo 'parseo.py'. Pruebe que su código funciona correctamente.

## Pregunta 2 - Gestión de Biblioteca

#### **Contexto general**
Se desea construir un programa en Python que administre libros, usuarios, categorías y préstamos utilizando listas, tuplas, diccionarios y conjuntos, organizado en funciones modulares.
- Las tuplas se usarán para representar datos fijos que no deben cambiar, como los metadatos de un libro: (isbn, titulo, autor).
- Las listas almacenarán colecciones ordenadas y dinámicas, como el historial de préstamos de un usuario o la lista general de libros disponibles.
- Los diccionarios serán la base de datos principal en memoria, donde la clave es el ISBN o el nombre de usuario y el valor es la información detallada en cada caso.
- Los conjuntos se usarán para almacenar los géneros o categorías disponibles en la biblioteca (ej. {"Fantasía", "Ciencia Ficción", "Historia"}).

#### **Funciones a implementar**

1) `agregar_categoria(categorias : set, nueva_categoria : str) -> set`
    - Permite agregar una categoría o género al registro de categorías de la Biblioteca
    - Reciba un conjunto de categorías y una nueva categoría a agregar. 
    - Agrega la categoría al conjunto (recuerda que los set manejan los duplicados automáticamente)
    - Debe retornar el conjunto actualizado 

2) `registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set) -> dict, set`
    - Esta función crea un libro con toda su información en el inventario de la Biblioteca
    - Crea una tupla con la información básica del libro: (titulo, autor, categoria)
    - Agrega esta tupla al diccionario inventario usando el isbn como clave.
    - Agrega la categoría del libro que se está registrando al registro (use la función agregar_categoria)
    - La función devuelve el inventario (dict) y el registro de categorías (set)

3) `registrar_usuario(usuarios: dict, id_usuario: str, nombre) -> dict`
    - Esta función guarda en un diccionario al usuario, utilizando su id como clave. 
    - Cada usuario debe tener un diccionario interno con su nombre y una lista vacía para sus "libros prestados"
    - La función retorna el registro de usuarios con su información (dict)

4) `prestar_libro(isbn: str, id_usuario: str, inventario: dict, usuarios: dict) -> dict`
    - Esta función se encarga de el préstamo de libros de la Biblioteca
    - Debe verificar si el libro existe en el inventario.
    - Debe verificar si el usuario existe
    - Si ambos existen, mueva o agregue el ISBN a la lista de libros prestados del usuario y elimine o marque el libro como no disponible en el inventario.


Debe escribir las funciones en el archivo 'modelos_biblioteca.py'. Pruebe que su código funciona correctamente en el archivo 'biblioteca.py', asignando valores e importando el módulo de los modelos para usar las funciones.