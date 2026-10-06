pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]
conteo_piezas_validas = 0

for peso_pieza in pesos_piezas:
    if peso_pieza <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif peso_pieza <= 13:
        print("Pieza Ligera aprobada.")
        conteo_piezas_validas += 1
    else:
        print("Pieza Pesada aprobada.")
        conteo_piezas_validas += 1

print(f"Piezas válidas: {conteo_piezas_validas}")