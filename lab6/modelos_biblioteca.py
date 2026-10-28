def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set):
    inventario[isbn] = (titulo, autor, categoria)
    categorias = agregar_categoria(categorias, categoria)
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre: str) -> dict:
    usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
    return usuarios


def prestar_libro(isbn: str, id_usuario: str, inventario: dict, usuarios: dict):
    if isbn not in inventario:
        print(f"El libro con ISBN {isbn} no está disponible en el inventario.")
        return usuarios
    if id_usuario not in usuarios:
        print(f"El usuario con ID {id_usuario} no está registrado.")
        return usuarios
    usuarios[id_usuario]["libros_prestados"].append(isbn)
    del inventario[isbn]
    return usuarios
