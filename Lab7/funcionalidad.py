from captura import pedir_flotante


def mostrar_empleado(empleado: dict):
    print(f"Nombre: {empleado['nombre']} | Edad: {empleado['edad']} | "
          f"Salario: {empleado['salario']:.2f} | Departamento: {empleado['dpto']}")


def listar_empleados(empleados: list):
    if not empleados:
        print("No hay empleados registrados.")
        return
    print("\n=== Lista de empleados ===")
    for empleado in empleados:
        mostrar_empleado(empleado)


def buscar_por_departamento(empleados: list, dpto_a_buscar: str) -> list:
    encontrados = [e for e in empleados if e["dpto"].lower() == dpto_a_buscar.lower()]
    if not encontrados:
        print(f"No hay empleados en el departamento '{dpto_a_buscar}'.")
    else:
        print(f"\n=== Empleados en {dpto_a_buscar} ===")
        for empleado in encontrados:
            mostrar_empleado(empleado)
    return encontrados


def aplicar_aumento_salarial(empleados: list, empleado_a_buscar: str) -> list:
    for empleado in empleados:
        if empleado["nombre"].lower() == empleado_a_buscar.lower():
            porcentaje = pedir_flotante("Porcentaje de aumento: ")
            empleado["salario"] = empleado["salario"] * (1 + porcentaje / 100)
            print(f"Nuevo salario de {empleado['nombre']}: {empleado['salario']:.2f}")
            return empleados
    print(f"No se encontró al empleado '{empleado_a_buscar}'.")
    return empleados


def obtener_promedio_salarial(empleados: list) -> float:
    if not empleados:
        return 0.0
    return sum(e["salario"] for e in empleados) / len(empleados)
