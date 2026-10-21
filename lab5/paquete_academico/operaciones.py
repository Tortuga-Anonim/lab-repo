def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def encontrar_maximo(lista_notas):
    maximo = lista_notas[0]
    for nota in lista_notas:
        if nota > maximo:
            maximo = nota
    return maximo
