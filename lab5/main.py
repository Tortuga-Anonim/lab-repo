import auth
import operaciones

saldo = 1000.0
pin_correcto = "1234"

print("CAJERO AUTOMÁTICO")

if auth.verificar_pin(pin_correcto):
    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                operaciones.consultar_saldo(saldo)
            case "2":
                monto = float(input("Ingrese monto a depositar: "))
                saldo = operaciones.depositar(saldo, monto)
            case "3":
                monto = float(input("Ingrese monto a retirar: "))
                saldo = operaciones.retirar(saldo, monto)
            case "4":
                print("Gracias por usar el cajero.")
                break
            case _:
                print("Opción inválida.")
else:
    print("Tarjeta bloqueada por seguridad.")
