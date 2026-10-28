import modelos_biblioteca

inventario = {}
usuarios = {}
categorias = set()

categorias = modelos_biblioteca.agregar_categoria(categorias, "Fantasía")
categorias = modelos_biblioteca.agregar_categoria(categorias, "Historia")
categorias = modelos_biblioteca.agregar_categoria(categorias, "Fantasía")
print(categorias)

agregar_libro = modelos_biblioteca.registrar_libro
inventario, categorias = agregar_libro(inventario, "978-3-16-148410-0", "El Hobbit", "J.R.R. Tolkien", "Fantasía", categorias)
inventario, categorias = agregar_libro(inventario, "978-0-7432-7356-5", "1984", "George Orwell", "Ciencia Ficción", categorias)
inventario, categorias = agregar_libro(inventario, "978-0-452-28423-4", "Orgullo y Prejuicio", "Jane Austen", "Romance", categorias)
print(inventario)
print(categorias)

agregar_usuario = modelos_biblioteca.registrar_usuario
usuarios = agregar_usuario(usuarios, "user1", "Alice")
usuarios = agregar_usuario(usuarios, "user2", "Bob")
print(usuarios)

cambiar_libro = modelos_biblioteca.prestar_libro
usuarios = cambiar_libro("978-3-16-148410-0", "user1", inventario, usuarios)
usuarios = cambiar_libro("978-0-7432-7356-5", "user3", inventario, usuarios)
usuarios = cambiar_libro("978-0-452-28423-4", "user2", inventario, usuarios)
usuarios = cambiar_libro("978-3-16-148410-0", "user2", inventario, usuarios)
usuarios = cambiar_libro("978-1-56619-909-4", "user1", inventario, usuarios)
print(inventario)
print(usuarios)
