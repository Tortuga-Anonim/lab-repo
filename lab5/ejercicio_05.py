"""
EJERCICIO 05: Refactorización de un programa de Cajero Automático

Se tiene un programa que simula un cajero automático. Este es funcional, pero está mal estructurado. 
Debes dividir el código proporcionado en una estructura modular de tres archivos:

    1. auth.py (Módulo de Autenticación):

        - Debe contener una función, por ejemplo, verificar_pin(pin_correcto) que gestione el ciclo de los intentos y 
        retorne True si el usuario acierta o False si agota los intentos.

    2. operaciones.py (Módulo de Lógica Bancaria):

        - Debe contener funciones puras o con parámetros claros para las acciones del cajero, por ejemplo:
            consultar_saldo(saldo)
            depositar(saldo, monto) (retorna el nuevo saldo)
            retirar(saldo, monto) (retorna el nuevo saldo si es posible, o muestra error)

    3. main.py (Script Principal):

        - Debe importar auth y operaciones.
        - Debe inicializar las variables principales (saldo = 1000.0, pin_correcto = "1234").
        - Debe coordinar el flujo del programa principal llamando a las funciones de los módulos importados.

"""


from funciones import main
