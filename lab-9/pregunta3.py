'''## Pregunta 3 — Clase Libro (`question_3.py`)

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
l2.resumen()    # → "El Conde de Monte Cristo - Alexander Dumas (0%): 0 páginas leídas de 1276"
```

'''
class Libro:
    def __init__(self, titulo, autor, paginas, leidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = leidas

    def leer(self, cantidad):
        if cantidad < 0 or self._progreso + cantidad > self.paginas:
            print("Cantidad inválida")
        else:
            self._progreso += cantidad

    def progreso(self):
        if self.paginas == 0:
            return 0
        return (self._progreso / self.paginas) * 100

    def resumen(self):
        porcentaje = round(self.progreso())
        return f"{self.titulo} - {self.autor} ({porcentaje}%): {self._progreso} páginas leídas de {self.paginas}"
l1 = Libro("Pachinko", "Min Jin Lee", 496, 193)
l2 = Libro("El Conde de Monte Cristo", "Alexander Dumas", 1276)

l1.leer(200)           
l1._progreso    # → 393
print(l1._progreso)  # → 393

l1.progreso()   # → 79%
print(l1.progreso())  # → 79.0
l1.resumen()    # → "Pachinko - Min Jin Lee (79%): 393 páginas leídas de 496"
l2.resumen()    # → "El Conde de Monte Cristo - Alexander Dumas (0%): 0 páginas leídas de 1276"
print(l1.resumen())  # → "Pachinko - Min Jin Lee (79%): 393 páginas leídas de 496"
print(l2.resumen())  # → "El Conde de Monte Cristo - Alexander Dumas