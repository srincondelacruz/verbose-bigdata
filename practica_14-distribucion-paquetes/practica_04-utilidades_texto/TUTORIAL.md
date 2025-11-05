# Guion de la Práctica 04: Paquete con Subpaquetes

Este documento detalla los pasos para crear el paquete `utilidades_texto`, que utiliza una estructura de subpaquetes.

---

## 3. Crear y distribuir un paquete con subpaquetes

### 3.1 Crea un nuevo proyecto llamado `utilidades_texto`

(En nuestro repositorio, esta es la carpeta `practica_04-utilidades_texto`).

La estructura debe ser:

practica_04-utilidades_texto/ 
├── texto/ │ 
├── init.py <-- Archivo clave para definir 'texto' como un paquete 
│ ├── conteo.py <-- Módulo de conteo 
│ └── formato.py <-- Módulo de formato 
└── setup.py



### 3.2 Implementa los módulos

#### `texto/conteo.py`

```python
def contar_palabras(frase):
    return len(frase.split())

def contar_caracteres(frase):
    return len(frase)
texto/formato.py
Python

def en_mayusculas(frase):
    return frase.upper()

def en_minusculas(frase):
    return frase.lower()
3.3 Crea el archivo setup.py
Para paquetes con subcarpetas (como texto/), usamos find_packages():

Python

from setuptools import setup, find_packages

setup(
    name="utilidades_texto",
    version="0.1",
    packages=find_packages(), # Esto encuentra 'texto' automáticamente
    description="Paquete con herramientas para manipular texto"
)
3.4 Genera la distribución
En la terminal, desde la raíz de este proyecto (practica_04...):

PowerShell

python setup.py sdist bdist_wheel
3.5 Instálalo desde otra carpeta
Simula ser un usuario externo (desde la raíz del repositorio):

PowerShell

cd ..
python -m pip install .\practica_14-distribucion-paquetes\practica_04-utilidades_texto\dist\utilidades_texto-0.1.tar.gz --upgrade
3.6 Prueba las funciones
Desde la terminal (fuera de la carpeta del proyecto), entra en Python y prueba las importaciones de dos niveles:

Python

>>> from texto.conteo import contar_palabras, contar_caracteres
>>> from texto.formato import en_mayusculas, en_minusculas

>>> frase = "Python es increíble"
>>> print("Palabras:", contar_palabras(frase))
Palabras: 3
>>> print("Caracteres:", contar_caracteres(frase))
Caracteres: 19
>>> print("Mayúsculas:", en_mayusculas(frase))
Mayúsculas: PYTHON ES INCREÍBLE
>>> print("Minúsculas:", en_minusculas(frase))
Minúsculas: python es increíble
3.7 Realiza las mismas pruebas anteriores desde un notebook de Jupyter
Instala Jupyter en este mismo entorno (python -m pip install notebook).

Lanza jupyter notebook.

En una celda, importa y prueba las 4 funciones (recuerda guardar el notebook .ipynb dentro de esta carpeta).