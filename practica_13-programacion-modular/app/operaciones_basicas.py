from paquete.suma import suma
from paquete.resta import resta
from paquete.subpaquete.multiplicacion import multiplicacion
from paquete.subpaquete.division import division

def operar_todo(a, b):
    return {
        "suma": suma(a, b),
        "resta": resta(a, b),
        "multiplicacion": multiplicacion(a, b),
        "division": division(a, b)
    }

