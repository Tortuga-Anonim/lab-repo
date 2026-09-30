'''
EJERCICIO 15: Ubicación de coordenadas
    Considere las coordenadas 'x' y 'y' de un punto como flotantes. Muestre dónde se ubica el punto en los cuadrantes del espacio:
    - Cuadrante I
    - Cuadrante II
    - Cuadrante III
    - Cuadrante IV
    - Eje X
    - Eje Y
    - En el origen (0,0)
'''

# Escriba su solución
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

if x > 0 and y > 0:
    print("El punto se encuentra en el Cuadrante I")
elif x < 0 and y > 0:
    print("El punto se encuentra en el Cuadrante II")
elif x < 0 and y < 0:
    print("El punto se encuentra en el Cuadrante III")
elif x > 0 and y < 0:
    print("El punto se encuentra en el Cuadrante IV")
elif x == 0 and y != 0:
    print("El punto se encuentra en el Eje Y")
elif x != 0 and y == 0:
    print("El punto se encuentra en el Eje X")
else:
    print("El punto se encuentra en el origen (0,0)")
