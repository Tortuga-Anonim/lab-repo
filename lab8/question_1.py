def binary_search(lista: list, objetivo: int) -> int:
    """
    Input:
        lista: list de ints ordenada de menor a mayor
        objetivo: int a buscar
    Output:
        int: índice de objetivo en lista, o -1 si no existe
    """
    left = 0
    right = len(lista) - 1

    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] > objetivo:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def esta_en_lista(lista: list, objetivo: int) -> str:
    """
    Input:
        lista: list de ints ordenada de menor a mayor
        objetivo: int a buscar
    Output:
        str: "Puntaje X encontrado en posición Y" o "Puntaje X no encontrado"
    """
    posicion = binary_search(lista, objetivo)
    if posicion != -1:
        return f"Puntaje {objetivo} encontrado en posición {posicion}"
    return f"Puntaje {objetivo} no encontrado"


if __name__ == "__main__":
    puntajes = [10, 25, 33, 47, 58, 61, 74, 89]

    print(binary_search(puntajes, 47))   # → 3
    print(binary_search(puntajes, 50))   # → -1

    print(esta_en_lista(puntajes, 61))   # → "Puntaje 61 encontrado en posición 5"
    print(esta_en_lista(puntajes, 99))   # → "Puntaje 99 no encontrado"
