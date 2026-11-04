import captura
import funcionalidad
import estadisticas


def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Ingresar empleados")
    print("2. Mostrar empleados")
    print("3. Buscar por departamento")
    print("4. Aplicar aumento salarial")
    print("5. Mostrar estadísticas")
    print("6. Salir")


def main():
    empleados = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            empleados = captura.registrar_empleados(empleados)
        elif opcion == "2":
            funcionalidad.listar_empleados(empleados)
        elif opcion == "3":
            dpto = captura.pedir_texto("Departamento a buscar: ")
            funcionalidad.buscar_por_departamento(empleados, dpto)
        elif opcion == "4":
            nombre = captura.pedir_texto("Nombre del empleado: ")
            empleados = funcionalidad.aplicar_aumento_salarial(empleados, nombre)
        elif opcion == "5":
            estadisticas.mostrar_estadisticas(empleados)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
