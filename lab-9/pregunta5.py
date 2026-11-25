'''## Pregunta 5 — Clases Tarea y ListaTareas (`question_5.py`)

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
3. `contar_por_prioridad(prioridad)`  — Retorna la cantidad de tareas de la prioridad indicada.'''
class Tarea:
    def __init__(self, titulo, prioridad="baja", completada=False):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

class ListaTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_pendientes(self):
        pendientientes = []
        for tarea in self.tareas:
            if not tarea.completada:
                pendientientes.append(tarea)
        return pendientientes

    def contar_por_prioridad(self, prioridad):
        return len([tarea for tarea in self.tareas if tarea.prioridad == prioridad])
t1 = Tarea("Tomar agua", "alta")
t2 = Tarea("Llamar a Octavio")
t3 = Tarea("Investigar PC", "media", True)
t1.marcar_completada()

lt = ListaTareas("Planificación del día")
lt.agregar_tarea(t1)
print(lt.listar_pendientes())          # []
lt.agregar_tarea(t3)
print(lt.listar_pendientes())         
lt.agregar_tarea(t2)
print(lt.contar_por_prioridad("baja")) # 1