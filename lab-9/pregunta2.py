'''## Pregunta 2 — Clase CuentaBancaria (`question_2.py`)

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
'''
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            print("Monto inválido")

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self._saldo

    def transferir(self, destino, monto):
        if 0 < monto <= self._saldo:
            self.retirar(monto)
            destino.depositar(monto)
        else:
            print("Fondos insuficientes")
c1 = CuentaBancaria("Pedro", 100)
c2 = CuentaBancaria("María", 50)

c1.depositar(200)
c1.obtener_saldo()     # → 300
print(c1.obtener_saldo())  # → 300
c1.retirar(50)
c1.obtener_saldo()     # → 250
c1.retirar(500)        # → "Fondos insuficientes"
print(c1.obtener_saldo())  # → 250
c1.transferir(c2, 100)
c1.obtener_saldo()     # → 150
c2.obtener_saldo()     # → 150
print(c1.obtener_saldo())  
print(c2.obtener_saldo())

