# Laboratorio 8 — Ordenamiento y Búsqueda

## Temas
- Búsqueda binaria
- Bubble Sort y `sorted()` de Python
- Listas y diccionarios

---

## Pregunta 1 — Búsqueda Binaria (`question_1.py`)

Tienes una lista de puntajes **ya ordenada de menor a mayor**. Tu tarea es implementar búsqueda binaria para encontrar si un puntaje existe.

La idea es sencilla: en vez de revisar uno por uno, divides la lista a la mitad en cada paso:
- Si el elemento del medio es el que buscas → encontrado.
- Si es mayor → busca en la mitad izquierda.
- Si es menor → busca en la mitad derecha.
- Si las mitades se agotan → no existe.

### Funciones a implementar

1. `binary_search(lista: list, objetivo: int) -> int`
   - Retorna el índice donde está `objetivo`, o `-1` si no existe.
   - Usa las variables `left`, `right`, `mid` para llevar el control.

2. `esta_en_lista(lista: list, objetivo: int) -> str`
   - Usa `binary_search` internamente.
   - Retorna `"Puntaje X encontrado en posición Y"` o `"Puntaje X no encontrado"`.

```python
puntajes = [10, 25, 33, 47, 58, 61, 74, 89]

binary_search(puntajes, 47)   # → 3
binary_search(puntajes, 50)   # → -1

esta_en_lista(puntajes, 61)   # → "Puntaje 61 encontrado en posición 5"
esta_en_lista(puntajes, 99)   # → "Puntaje 99 no encontrado"
```

---

## Pregunta 2 — Bubble Sort (`question_2.py`)

Tienes una lista de estudiantes con nombre y nota. Tu tarea es ordenarla de dos formas distintas.

**Bubble Sort** funciona comparando elementos vecinos y cambiándolos de lugar si están en el orden incorrecto. Repite esto hasta que la lista quede ordenada.

### Funciones a implementar

1. `bubble_sort(lista: list) -> list`
   - Ordena una lista de números de **menor a mayor** usando bubble sort.
   - No uses `sorted()` ni `.sort()` aquí — impleméntalo tú con ciclos.

2. `ordenar_estudiantes(estudiantes: list) -> list`
   - Recibe una lista de diccionarios `{"nombre": str, "nota": float}`.
   - Retorna la lista ordenada por `nota` de **mayor a menor** usando `sorted()` con `key=` y `reverse=True`.

```python
numeros = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numeros)
# → [11, 12, 22, 25, 34, 64, 90]

estudiantes = [
    {"nombre": "Ana",    "nota": 85},
    {"nombre": "Luis",   "nota": 92},
    {"nombre": "Maria",  "nota": 78},
    {"nombre": "Carlos", "nota": 95},
]
ordenar_estudiantes(estudiantes)
# → [Carlos 95, Luis 92, Ana 85, Maria 78]
```

---

## Pregunta 3 — Diccionarios (`question_3.py`)

Implementa las 3 funciones que se pidieron en el parcial del lunes para la sección 2
