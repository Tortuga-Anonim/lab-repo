def bubble_sort(lista: list) -> list:
    """
    Input:
        lista: list de números
    Output:
        list: la misma lista ordenada de menor a mayor (usando bubble sort)
    """
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def ordenar_estudiantes(estudiantes: list) -> list:
    """
    Input:
        estudiantes: list de dicts con formato {"nombre": str, "nota": float}
    Output:
        list: estudiantes ordenados por nota de mayor a menor (usa sorted())
    """
    return sorted(estudiantes, key=lambda x: x["nota"], reverse=True)


if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(numeros))
    # → [11, 12, 22, 25, 34, 64, 90]

    estudiantes = [
        {"nombre": "Ana",    "nota": 85},
        {"nombre": "Luis",   "nota": 92},
        {"nombre": "Maria",  "nota": 78},
        {"nombre": "Carlos", "nota": 95},
    ]
    print(ordenar_estudiantes(estudiantes))
    # → [{"nombre": "Carlos", ...}, {"nombre": "Luis", ...}, ...]
