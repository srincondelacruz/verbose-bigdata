# Guion de la Práctica 03: Paquete de Módulo Simple

Este documento detalla los pasos para crear el paquete `operaciones_basicas` y probar el aislamiento de entornos.

---

## 1. Prueba de Aislamiento (Jupyter)

*Esta prueba se realiza en el entorno de la Práctica 2 (`practica_02-pip_jupyter`)*

Verifica que **NO PUEDES** importar la librería `paquete` (creada en la Práctica 1) desde el *notebook* de Jupyter de la Práctica 2.

```python
# Esto debe fallar con un ModuleNotFoundError
from paquete.hola.saludos import saludar
Esto demuestra que los entornos virtuales están correctamente aislados.

2. Crear y distribuir un paquete de operaciones matemáticas
Este es un ejemplo de un paquete basado en un módulo único (.py).

2.1 Crea la estructura
(En nuestro repositorio, esta es la carpeta practica_03-operaciones_basicas).

2.2 En operaciones.py, escribe las siguientes funciones:
Python

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
2.3 Crea el archivo setup.py
Para un módulo único, se usa py_modules:

Python

from setuptools import setup

setup(
    name="operaciones_basicas",
    version="0.1",
    description="Mi paquete de operaciones matemáticas básicas",
    py_modules=['operaciones']
)
2.4 Genera la distribución
En la terminal, desde la raíz de este proyecto:

PowerShell

python setup.py sdist bdist_wheel
2.5 Instala el paquete desde otra ubicación
Simula ser un usuario externo:

PowerShell

# Sube a un directorio padre (ej. la raíz del repo)
cd ..

# Instala desde el archivo .tar.gz
python -m pip install .\practica_03-operaciones_basicas\dist\operaciones_basicas-0.1.tar.gz
2.6 Prueba el paquete
Desde la terminal (fuera de la carpeta del proyecto), entra en Python y prueba:

Python

>>> from operaciones import sumar
>>> sumar(5, 10)
15
2.7 Realiza las mismas pruebas anteriores desde un notebook de Jupyter
Instala Jupyter en este mismo entorno (python -m pip install notebook).

Lanza jupyter notebook.

En una celda, importa y prueba sumar y restar.