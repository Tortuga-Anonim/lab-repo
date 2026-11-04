from funcionalidad import obtener_promedio_salarial


def calcular_estadisticas(empleados: list) -> dict:
    salarios = list(map(lambda e: e["salario"], empleados))
    edades = [e["edad"] for e in empleados]
    return {
        "total": len(empleados),
        "edad_promedio": sum(edades) / len(edades),
        "menores_30": len(list(filter(lambda edad: edad < 30, edades))),
        "salario_promedio": obtener_promedio_salarial(empleados),
        "salario_maximo": max(salarios),
        "salario_minimo": min(salarios),
        "supera_1000": any(s > 1000 for s in salarios),
    }


def mostrar_estadisticas(empleados: list):
    if not empleados:
        print("No hay empleados registrados para calcular estadísticas.")
        return
    stats = calcular_estadisticas(empleados)
    print("\n=== Estadísticas generales ===")
    print(f"Cantidad total de empleados: {stats['total']}")
    print(f"Edad promedio: {stats['edad_promedio']:.1f}")
    print(f"Empleados menores de 30 años: {stats['menores_30']}")
    print(f"Salario promedio: {stats['salario_promedio']:.2f}")
    print(f"Salario máximo: {stats['salario_maximo']:.2f}")
    print(f"Salario mínimo: {stats['salario_minimo']:.2f}")
    if stats["supera_1000"]:
        print("Sí hay al menos un salario que supera los 1000.")
    else:
        print("Ningún salario supera los 1000.")
