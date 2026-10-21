def consultar_saldo(saldo):
    print(f"Su saldo actual es: ${saldo}")


def depositar(saldo, monto):
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    else:
        print("Monto inválido.")
    return saldo


def retirar(saldo, monto):
    if 0 < monto <= saldo:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
    elif monto > saldo:
        print("Fondos insuficientes")
    else:
        print("Monto inválido")
    return saldo
