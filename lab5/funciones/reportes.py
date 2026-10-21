from funciones import operaciones


def generar_resumen(lista_notas):
    promedio = operaciones.calcular_promedio(lista_notas)
    maximo = operaciones.encontrar_maximo(lista_notas)
    print("REPORTE DE NOTAS")
    print(f"Promedio: {promedio}")
    print(f"Nota máxima: {maximo}")
