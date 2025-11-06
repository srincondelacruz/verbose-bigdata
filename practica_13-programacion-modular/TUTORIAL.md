# Práctica 13: Programación Modular

Este documento cubre los conceptos de Módulos, Paquetes y Subpaquetes en Python, incluyendo la refactorización de código secuencial a modular.

---

## 1. Forma secuencial versus forma modular

*Los códigos de este ejemplo los puedes descargar desde [aquí](https://bit.ly/2Y4xW4V).*

### Ejercicio propuesto 1:
Modifica el ejemplo resuelto en clase añadiendo resta, multiplicación y división.

---

## 2. Idea básica: Módulos

*Los códigos de esta sección los puedes descargar desde [aquí](https://bit.ly/2L1VbDa).*

Crear un módulo es tan sencillo como crear un fichero `.py` con funciones o clases.

**`saludos.py`**
```python
def saludar():
    print("Hola, te estoy saludando desde la función saludar() " \
            "del módulo saludos")

class Saludo():
    def __init__(self):
        print("Hola, te estoy saludando desde el __init__ " \
                "de la clase Saludo")
Luego se puede utilizar desde otro script (script.py) en el mismo directorio.

script.py (Opción 1: Importar módulo)

Python

import saludos

saludos.saludar()
saludos.Saludo()
script.py (Opción 2: Importar contenido)

Python

from saludos import saludar, Saludo

saludar()
Saludo()
Ejercicio propuesto 2:
Modificar el ejemplo anterior, esta vez en vez de saludar utilizar despedir.

3. Idea básica: Paquetes
Los códigos de esta sección los puedes descargar desde aquí.

Para crear un paquete, creamos un fichero especial __init__.py (vacío) en el directorio donde tengamos los módulos que queremos agrupar.

Estructura:

script.py
paquete/
    ├── __init__.py
    └── saludos.py
script.py

Python

from paquete.saludos import saludar
saludar()
4. Idea básica: Subpaquetes
Los códigos de esta sección los puedes descargar desde aquí.

La jerarquía se puede expandir creando subpaquetes, siempre añadiendo el fichero __init__.py en cada uno.

Estructura:

script.py
paquete/
    ├── __init__.py
    ├── hola/
    │   ├── __init__.py
    │   └── saludos.py
    └── adios/
        ├── __init__.py
        └── despedidas.py
paquete/hola/saludos.py

Python

def saludar():
    print("Hola, te estoy saludando desde la función saludar() " \
          "del módulo saludos")
paquete/adios/despedidas.py

Python

def despedir():
    print("Adiós, me estoy despidiendo desde la función despedir() " \
            "del módulo despedidas")
script.py (main)

Python

from paquete.hola.saludos import saludar
from paquete.adios.despedidas import despedir

saludar()
despedir()
5. El Programa Principal (Main)
Suele ser una buena práctica llamar main.py al fichero que contiene nuestro programa principal o punto de entrada (entry point).

Ejercicio propuesto 3: Estructura de Paquetes (Messages)
Escribe un programa Python organizado con los paquetes messages.funny y messages.curt.

Solución
Estructura de directorios:

messages/
├── __init__.py
├── funny/
│   ├── __init__.py
│   ├── modf1.py
│   ├── modf2.py
│   └── modf3.py
└── curt/
    ├── __init__.py
    ├── modc1.py
    ├── modc2.py
    └── modc3.py
client.py
<img src="/icons/database_red.svg" alt="/icons/database_red.svg" width="40px" /> Importante: Para que un directorio califique como un paquete, debe contener un archivo __init__.py.

Códigos de Módulos:

Python

# modf1.py
def funf1():
    print('The ability to speak several languages is an asset...')
    print("ability to keep your mouth shut in any language is priceless")

# modf2.py
def funf2():
    print('If you cut off your left arm...')
    print('then your right arm would be left')

# modf3.py
def funf3():
    print('Alcohol is a solution!')

# modc1.py
def func1():
    print('Light travels faster than sound...')
    print('People look intelligent, till they open their mouth')

# modc2.py
def func2():
    print('There is no physical evidence to say that today is Tuesday...')
    print('We have to trust someone who kept the count since first day')

# modc3.py
def func3():
    print('We spend five days a week pretending to be someone else...')
    print('in order to spend two days being who we are')
Programa Cliente (client.py)

Python

import messages.funny.modf1
import messages.funny.modf2
import messages.funny.modf3
import messages.curt.modc1
import messages.curt.modc2
import messages.curt.modc3

messages.funny.modf1.funf1()
messages.funny.modf2.funf2()
messages.funny.modf3.funf3()
messages.curt.modc1.func1()
messages.curt.modc2.func2()
messages.curt.modc3.func3()
Ejercicio propuesto 4: Mejorar Imports
Reescribe las sentencias import del ejercicio 3 para que sean más convenientes.

Solución (client.py v2):

Python

from messages.funny.modf1 import funf1
from messages.funny.modf2 import funf2
from messages.funny.modf3 import funf3
from messages.curt.modc1 import func1
from messages.curt.modc2 import func2
from messages.curt.modc3 import func3

funf1()
funf2()
funf3()
func1()
func2()
func3()
Beneficio: Las llamadas a funciones no necesitan la sintaxis con puntos.

Limitación: Solo se importa la función especificada.

Ejercicio propuesto 5: Importar con * (Wildcard)
¿Podemos reescribir las importaciones usando la notación *?

Solución (client.py v3):

Python

from messages.curt.modc1 import *
from messages.curt.modc2 import *
from messages.curt.modc3 import *
from messages.funny.modf1 import *
from messages.funny.modf2 import *
from messages.funny.modf3 import *

funf1()
funf2()
funf3()
func1()
func2()
func3()
Limitación: * no es popular ya que no indica qué función/clase estamos importando y puede contaminar el namespace.

Ejercicio propuesto 6: De Programación Secuencial a Modular
Convertir una calculadora de paradigma secuencial a modular.

Versión Secuencial (calculadora_secuencial.py):
Python

import math
import statistics

# ========================
# Datos iniciales
# ========================
a = 10
b = 5
lista = [1, 2, 3, 4, 4, 5]

# ========================
# Operaciones Básicas
# ========================
print("=== Operaciones Básicas ===")
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "Error: división por cero"
# ... (resto de prints) ...

# ========================
# Estadísticas
# ========================
print("\n=== Estadísticas Básicas ===")
media = statistics.mean(lista)
mediana = statistics.median(lista)
moda = statistics.mode(lista)
# ... (resto de prints) ...

# ========================
# Operaciones Especiales
# ========================
print("\n=== Operaciones Especiales ===")
potencia = a ** b
raiz = math.sqrt(a) if a >= 0 else "Error: raíz de número negativo"
logaritmo = math.log(a) if a > 0 else "Error: logaritmo indefinido"
exponencial = math.exp(b)
# ... (resto de prints) ...
Versión Modular:
(Esta es la estructura que tienes en tu carpeta practica_13)

📁 Estructura del Proyecto

.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── operaciones_basicas.py
│   └── estadisticas.py
├── paquete/
│   ├── __init__.py
│   ├── suma.py
│   ├── resta.py
│   └── subpaquete/
│       ├── __init__.py
│       ├── multiplicacion.py
│       └── division.py
└── operaciones_especiales/
    ├── __init__.py
    ├── potencias_raices.py
    └── log_exp.py
📄 paquete/suma.py

Python

def suma(a, b):
    return a + b
📄 paquete/resta.py

Python

def resta(a, b):
    return a - b
📄 paquete/subpaquete/multiplicacion.py

Python

def multiplicacion(a, b):
    return a * b
📄 paquete/subpaquete/division.py

Python

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
📄 operaciones_especiales/potencias_raices.py

Python

import math

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("Raíz de número negativo.")
    return math.sqrt(numero)
📄 operaciones_especiales/log_exp.py

Python

import math

def logaritmo(x, base=math.e):
    if x <= 0:
        raise ValueError("Logaritmo indefinido.")
    return math.log(x, base)

def exponencial(x):
    return math.exp(x)
📄 app/operaciones_basicas.py

Python

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
📄 app/estadisticas.py

Python

import statistics

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    return statistics.mode(lista)
📄 app/main.py (El Entry Point)

Python

# Corrección: Python necesita rutas relativas o absolutas claras.
# Asumiendo que 'app' está en el PYTHONPATH.
try:
    from app.operaciones_basicas import operar_todo
    from app.estadisticas import calcular_media, calcular_mediana, calcular_moda
    # Para importar 'operaciones_especiales', debe estar en el PYTHONPATH
    # o instalado como paquete.
    from operaciones_especiales.potencias_raices import potencia, raiz_cuadrada
    from operaciones_especiales.log_exp import logaritmo, exponencial
except ImportError:
    print("Error de importación: Asegúrate de que los paquetes 'app' y 'operaciones_especiales' estén accesibles.")
    exit()

def main():
    a = 10
    b = 5
    lista = [1, 2, 3, 4, 4, 5]

    print("=== Operaciones Básicas ===")
    resultados = operar_todo(a, b)
    for operacion, resultado in resultados.items():
        print(f"{operacion}: {resultado}")

    print("\n=== Estadísticas Básicas ===")
    print(f"Media: {calcular_media(lista)}")
    print(f"Mediana: {calcular_mediana(lista)}")
    print(f"Moda: {calcular_moda(lista)}")

    print("\n=== Operaciones Especiales ===")
    print(f"Potencia ({a}^{b}): {potencia(a, b)}")
    print(f"Raíz cuadrada de {a}: {raiz_cuadrada(a)}")
    print(f"Logaritmo de {a} base e: {logaritmo(a)}")
    print(f"Exponencial de {b}: {exponencial(b)}")

if __name__ == "__main__":
    main()
Nota: Los __init__.py (vacíos) son cruciales para que Python trate los directorios como paquetes.

Ejercicio propuesto 7: De Secuencial a Modular (Calificaciones)
Tu tarea es convertir el siguiente sistema monolítico (imperativo) a una arquitectura modular.

(El código monolítico de imperativo_completo.py se omite por brevedad, pero es el ejemplo largo del tutorial).

Ejercicio propuesto 8: Modularizar Estructura de Proyecto
Escoger una de las cuatro estructuras de carpetas (Data Engineering, Big Data, Data Science, Generative AI) y "modularizar como si fuese un proyecto con paquetes y subpaquetes con Python".

(Las estructuras de carpetas se omiten por brevedad).