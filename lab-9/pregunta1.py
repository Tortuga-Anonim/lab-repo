'''La universidad quiere reemplazar su sistema de notas basado en diccionarios por uno orientado a objetos.

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
 '''
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self._notas = []

    def agregar_nota(self, nota):
        self._notas.append(nota)

    def calcular_promedio(self):
        if len(self._notas) == 0:
            return 0
        return sum(self._notas) / len(self._notas)

    def mostrar_resumen(self):
        promedio = self.calcular_promedio()
        print(f"{self.nombre} ({self.carrera}) - Promedio: {promedio:.2f}")
e1 = Estudiante("Ana", "Ingeniería")
e1.agregar_nota(18)
e1.agregar_nota(16)
e1.agregar_nota(19)

e1.calcular_promedio()   # → 17.666...
e1.mostrar_resumen()     # → "Ana (Ingeniería) - Promedio: 17.67"
print(e1.calcular_promedio())  # → 17.666...

e2 = Estudiante("Luis", "Sistemas")
e2.calcular_promedio()   # → 0
e2.mostrar_resumen()     # → "Luis (Sistemas) - Promedio: 0.00"
print(e2.calcular_promedio())  # → 0