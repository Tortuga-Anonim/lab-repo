# Laboratorio 6 — Programación Orientada a Objetos

## Temas
- Clases y objetos
- Atributos y métodos
- Constructor (`__init__`)
- Encapsulamiento (`_atributo`)

---

## Contexto

Hasta ahora representaban datos con diccionarios y funciones sueltas. En este laboratorio van a reescribir esos mismos problemas usando clases, para ver de primera mano qué cambia y por qué.

La idea central: en vez de pasar un diccionario como parámetro a cada función, los datos y las funciones viven juntos dentro del objeto.

---

## Pregunta 1 — Clase Estudiante (`question_1.py`)

La universidad quiere reemplazar su sistema de notas basado en diccionarios por uno orientado a objetos.

Antes lo hacían así:

```python
estudiante = {"nombre": "Ana", "carrera": "Ingeniería", "notas": [18, 16, 19]}

def agregar_nota(est, nota):
    est["notas"].append(nota)

def calcular_promedio(est):
    if len(est["notas"]) == 0:
        return 0
    return sum(est["notas"]) / len(est["notas"])
```

Ahora tu tarea es diseñar la clase `Estudiante` que agrupe esos datos y funciones en un solo objeto.

### Lo que debes implementar

**Constructor `__init__(self, nombre, carrera)`**
- Recibe `nombre` y `carrera` como parámetros.
- Inicializa `_notas` como lista vacía. Usa `_notas` (con guión bajo) — nadie debería modificarla directamente desde afuera.

**Métodos obligatorios:**

1. `agregar_nota(self, nota)` — agrega `nota` a `_notas`.

2. `calcular_promedio(self)` — retorna el promedio de `_notas`. Si no hay notas, retorna `0`.

3. `mostrar_resumen(self)` — imprime una línea con el formato:
   `"Ana (Ingeniería) - Promedio: 17.5"`

```python
e1 = Estudiante("Ana", "Ingeniería")
e1.agregar_nota(18)
e1.agregar_nota(16)
e1.agregar_nota(19)

e1.calcular_promedio()   # → 17.666...
e1.mostrar_resumen()     # → "Ana (Ingeniería) - Promedio: 17.67"

e2 = Estudiante("Luis", "Sistemas")
e2.calcular_promedio()   # → 0
```

---

## Pregunta 2 — Clase CuentaBancaria (`question_2.py`)

Un banco necesita modelar cuentas bancarias. El problema con el enfoque anterior era que cualquier parte del código podía hacer `cuenta["saldo"] = -100` sin ninguna validación.

Con POO, el saldo queda protegido dentro del objeto y solo se puede modificar a través de métodos que aplican las reglas del negocio.

### Lo que debes implementar

**Constructor `__init__(self, titular, saldo_inicial=0)`**
- Recibe `titular` y opcionalmente `saldo_inicial`.
- Guarda el saldo en `_saldo`. Nadie debería tocarlo directamente.

**Métodos obligatorios:**

1. `depositar(self, monto)` — suma `monto` a `_saldo` solo si `monto > 0`. Si no, imprime `"Monto inválido"`.

2. `retirar(self, monto)` — resta `monto` de `_saldo` solo si `0 < monto <= _saldo`. Si no, imprime `"Fondos insuficientes"`.

3. `obtener_saldo(self)` — retorna el valor actual de `_saldo`.

4. `transferir(self, destino, monto)` — retira `monto` de esta cuenta y lo deposita en la cuenta `destino`. Solo si el retiro es posible.

```python
c1 = CuentaBancaria("Pedro", 100)
c2 = CuentaBancaria("María", 50)

c1.depositar(200)
c1.obtener_saldo()     # → 300

c1.retirar(50)
c1.obtener_saldo()     # → 250

c1.retirar(500)        # → "Fondos insuficientes"

c1.transferir(c2, 100)
c1.obtener_saldo()     # → 150
c2.obtener_saldo()     # → 150
```

---

## Pregunta 3 — Clase Libro (`question_3.py`)

Un amigo quiere llevar registro de los libros que está leyendo y poder consultar su progreso. Para ayudarlo, decides hacer el modelo de Libro con POO.

### Lo que debes implementar

**Constructor `__init__(self, titulo, autor, paginas, leidas=0)`**
- Recibe `titulo`, `autor`, `paginas` y opcionalmente `leidas`.
- Guarda las paginas leídas en `_progreso`. Nadie debería tocarlo directamente.

**Métodos obligatorios:**

1. `leer(self, cantidad)` — suma páginas leídas sin superar el total de `paginas`. Si no, imprime `"Cantidad inválida"`.

2. `progreso(self)` — retorna el porcentaje leído.

3. `resumen(self)` — retorna o imprime un resumen legible del estado del libro.

```python
l1 = Libro("Pachinko", "Min Jin Lee", 496, 193)
l2 = Libro("El Conde de Monte Cristo", "Alexander Dumas", 1276)

l1.leer(200)           
l1._progreso    # → 393

l1.progreso()   # → 79%

l1.resumen()    # → "Pachinko - Min Jin Lee (79%): 393 páginas leídas de 496"
c2.resumen()    # → "El Conde de Monte Cristo - Alexander Dumas (0%): 0 páginas leídas de 1276"
```

---

## Pregunta 4 — Clase Semaforo (`question_4.py`)

Se quiere simular una máquina de estados simple para simular el funcionamiento de un semáforo

### Lo que debes implementar

**Constructor `__init__(self, color_inicial="rojo")`**
- Recibe opcionalmente `color_inicial`.
- Guarda el color en `_color`. Nadie debería tocarlo directamente.

**Métodos obligatorios:**

1. `siguiente_estado(self)` — avanza el semáforo en orden ("rojo" -> "verde" -> "amarillo" -> "rojo").

2. `puede_avanzar()` — retorna True solo si el color actual es "verde"


```python
semaforo = Semaforo()

semaforo.siguiente_estado()
semaforo.puede_avanzar()        # True

semaforo.siguiente_estado()
semaforo.puede_avanzar()        # False
```

---

## Pregunta 5 — Clases Tarea y ListaTareas (`question_5.py`)

Que un objeto de una clase ListaTareas almacene y gestione instancias de Tareas (otra clase).

### Lo que debes implementar

**Constructor Tarea `__init__(self, titulo, prioridad="baja", completada=False)`**
- Recibe el `titulo` de la actividad y opcionalmente su `prioridad` y estado `completada`
- `prioridad` puede ser "baja", "media" o "alta"
- `completada` es un booleano que indica si la tarea se completó o no

**Métodos obligatorios de Tarea:**

1. `marcar_completada()` — Cambia el estado de la tarea de no completado a completado.

**Constructor ListaTarea `__init__(self, nombre)`**
- Recibe el `nombre` de la lista
- Debe tener una lista interna de tareas, inicialmente vacía. 

**Métodos obligatorios de ListaTarea:**

1. `agregar_tarea(tarea)`    — Agrega una tarea a la lista.
2. `listar_pendientes()`     — Retorna una lista de las actividades no completadas.
3. `contar_por_prioridad(prioridad)`  — Retorna la cantidad de tareas de la prioridad indicada.


```python
t1 = Tarea("Tomar agua", "alta")
t2 = Tarea("Llamar a Octavio")
t3 = Tarea("Investigar PC", "media", True)
t1.marcar_completada()

lt = ListaTareas("Planificación del día")
lt.agregar_tarea(t1)
lt.listar_pendientes()          # []
lt.agregar_tarea(t3)
lt.contar_por_prioridad("baja") # 1

```

