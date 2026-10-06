print("A. Mover a la derecha")
print("B. Mover a la izquierda")
print("C. Mover hacia el frente")
print("D. Mover hacia atrás")
print("E. Apagar")

while True:
    codigo_comando = input("Ingrese un código de comando: ").strip().upper()

    match codigo_comando:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            break
        case _:
            print("Comando no reconocido. Intente de nuevo.")
