"""
EJERCICIO 05: Menú de cómputo geométrico.

Complete las funciones para que al ejecutar el programa, se muestre el menú y se le pida al usuario ingresar una de las opciones
(1 - 4). 
    - Si escoge 1, se pide ingresar el valor del radio, se calcula el área del círculo y se muestra en pantalla
    - Si se escoge 2, se pide ingresar el valor de la base y la altura, se calcula el area del triángulo y se muestra en pantalla
    - Si se escoge 3, se pide ingresar el valor de la base y la altura, se calcula el perímetro del rectángulo y se muestra en pantalla
    - Si se escoge 4, se sale del menú y termina el programa
    - Si se ingresa cualquier otra opcion, se imprime "Opción inválida. Intente de nuevo."

"""

PI = 3.141592653589793


def pedir_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            continue

        if valor <= 0:
            print("El valor debe ser mayor que cero.")
        else:
            return valor


def area_circulo(radio):
    area = PI * radio ** 2
    print(f"El área del círculo de radio {radio} es: {area:.2f}")


def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo de base {base} y altura {altura} es: {area:.2f}")


def perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    print(f"El perímetro del rectángulo de base {base} y altura {altura} es: {perimetro:.2f}")


def menu():
    activo = True
    while activo:
        print("\nCALCULADORA GEOMÉTRICA")
        print("1. Área de un Círculo")
        print("2. Área de un Triángulo")
        print("3. Perímetro de un Rectángulo")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        match opcion:
            case "1":
                radio = pedir_numero_positivo("Ingrese el radio del círculo: ")
                area_circulo(radio)
            case "2":
                base = pedir_numero_positivo("Ingrese la base del triángulo: ")
                altura = pedir_numero_positivo("Ingrese la altura del triángulo: ")
                area_triangulo(base, altura)
            case "3":
                base = pedir_numero_positivo("Ingrese la base del rectángulo: ")
                altura = pedir_numero_positivo("Ingrese la altura del rectángulo: ")
                perimetro_rectangulo(base, altura)
            case "4":
                print("Saliendo...")
                activo = False
            case _:
                print("Opción inválida. Intente de nuevo.")


menu()
