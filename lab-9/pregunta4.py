'''## Pregunta 4 — Clase Semaforo (`question_4.py`)

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
'''
class Semaforo:
    def __init__(self, color_inicial="rojo"):
        self._color = color_inicial

    def siguiente_estado(self):
        if self._color == "rojo":
            self._color = "verde"
        elif self._color == "verde":
            self._color = "amarillo"
        elif self._color == "amarillo":
            self._color = "rojo"

    def puede_avanzar(self):
        return self._color == "verde"
semaforo = Semaforo()

semaforo.siguiente_estado()
semaforo.puede_avanzar()        # True
print(semaforo.puede_avanzar())  # True

semaforo.siguiente_estado()
semaforo.puede_avanzar()        # False
print(semaforo.puede_avanzar())  # False