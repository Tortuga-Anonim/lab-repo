def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    if linea is None or not isinstance(linea, str):
        raise ValueError("La línea debe ser una cadena de texto no vacía.")
    linea = linea.strip()
    partes = linea.split(",")
    
    if len(partes) != 4:
        raise ValueError("La línea debe tener 4 partes separadas por comas.")

    codigo = partes[0].strip()
    nombre = partes[1].strip()
    precio = float(partes[2].strip())
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    cantidad = int(partes[3].strip())
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    return {"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad}


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    if linea is None or not isinstance(linea, str):
        raise ValueError("La línea debe ser una cadena de texto no vacía.")
    producto = parsear_producto(linea)
    valor = round(producto["precio"] * producto["cantidad"], 1)
    return f"{producto['codigo']} - {producto['nombre']}: ${valor}"

def _validar_lineas(lineas):
    if lineas is None or not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("La entrada debe ser una lista de cadenas de texto no vacía.")
    for linea in lineas:
        if not isinstance(linea, str):
            raise ValueError("Todos los elementos de la lista deben ser cadenas de texto.")
def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))
    return salida


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    total = 0.0
    for linea in lineas:
        producto = parsear_producto(linea)
        total += producto["precio"] * producto["cantidad"]
    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    max_producto = parsear_producto(lineas[0])
    max_valor = max_producto["precio"] * max_producto["cantidad"]
    for linea in lineas[1:]:
        producto = parsear_producto(linea)
        valor = producto["precio"] * producto["cantidad"]
        if valor > max_valor:
            max_valor = valor
            max_producto = producto
    return f"{max_producto['codigo']} - {max_producto['nombre']}: ${round(max_valor, 1)}"


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # ejemplos rápidos para visualizar (descomenta cuando implementes)
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
