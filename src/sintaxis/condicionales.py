# valor para verificar el condicional
condicion: bool = False

# Condicional "if" basico del lenguaje
if condicion:
    print("Condición valida")
else:
    print("Condición invalida")
    # Esto imprimirá: "Condición invalida"

# Condicional ternario
comparacion = 10
ternario = True if comparacion > 5 else False
print(ternario)
# Esto imprimirá: "True"

# Condicional con operador logico
x = 10
y = 20
if x > 5 and y > 10:
    print("Ambas condiciones son verdaderas")
    # Esto imprimirá: "Ambas condiciones son verdaderas"

# Condicional de "in" para verificar la existencia en estructuras de datos:
lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("El 3 está en la lista")
    # Esto imprimirá: "El 3 está en la lista"


# Condicional "switch", aunque no existe realmente en python
# se puede emular su comportamiento
def case_1() -> str:
    return "Este es el caso 1"


def case_2() -> str:
    return "Este es el caso 2"


def case_3() -> str:
    return "Este es el caso 3"


# Diccionario que emula un switch
switch_case = {1: case_1, 2: case_2, 3: case_3}


# Función que ejecuta el "switch"
def switch(argument: int) -> str:
    return switch_case.get(argument, lambda: "Opción no válida")()


# Ejemplo de uso
resultado = switch(2)
print(resultado)
# Esto imprimirá: "Este es el caso 2"
