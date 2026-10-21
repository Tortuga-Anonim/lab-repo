def verificar_pin(pin_correcto):
    intentos = 3
    while intentos > 0:
        pin = input("Ingrese su PIN de 4 dígitos: ")
        if pin == pin_correcto:
            return True
        intentos -= 1
        print(f"PIN incorrecto. Te quedan {intentos} intentos.")
    return False
