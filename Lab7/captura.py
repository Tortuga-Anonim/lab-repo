def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero.")


def pedir_flotante(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número.")


def pedir_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")


def capturar_empleado() -> dict:
    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero("Edad: ")
    salario = pedir_flotante("Salario mensual: ")
    dpto = pedir_texto("Departamento: ")
    return {"nombre": nombre, "edad": edad, "salario": salario, "dpto": dpto}


def registrar_empleados(empleados: list) -> list:
    cantidad = pedir_entero("¿Cuántos empleados desea ingresar? ")
    for i in range(cantidad):
        print(f"\n--- Empleado {i + 1} ---")
        empleados.append(capturar_empleado())
    print(f"\nSe registraron {cantidad} empleado(s).")
    return empleados
