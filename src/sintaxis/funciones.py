# Definición de una función con parametros y argumentos


def print_msj(msj: str):
    return print("Primer función: " + msj)


def print_operacion(operacion: str, num1: int, num2: int):
    resultado = None

    if operacion == None or num1 == None or num2 == None:
        resultado = "debe llegar todos los parametros para la operación"
    elif operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    else:
        resultado = "No se reconocio el metodo que se esta empleando para esta función"

    return print("Segunda función: " + str(resultado))


print_msj("Hello, world!")
print_operacion("suma", 2, 8)
