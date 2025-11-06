import math

def logaritmo(x, base=math.e):
    if x <= 0:
        raise ValueError("El logaritmo sólo está definido para números positivos.")
    return math.log(x, base)

def exponencial(x):
    return math.exp(x)

