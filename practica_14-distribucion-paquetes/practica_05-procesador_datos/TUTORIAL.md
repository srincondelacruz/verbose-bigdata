# Guion de la Práctica 05: Paquete de Análisis de Datos

Este documento detalla los pasos para crear el paquete `procesador_datos`.

---

## 4. Crear, distribuir y probar un paquete de análisis de datos

### 4.1 Crea un nuevo proyecto llamado `procesador_datos`

(En nuestro repositorio, esta es la carpeta `practica_05-procesador_datos`).

La estructura debe ser:

procesador_datos/ ├── analisis/ │ ├── init.py │ ├── limpieza.py │ └── estadisticas.py └── setup.py



### 4.2 Implementa los módulos

#### `analisis/limpieza.py`

```python
def eliminar_nulos(lista):
    return [x for x in lista if x is not None]
analisis/estadisticas.py
Python

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

def maximo(lista):
    return max(lista) if lista else None

def minimo(lista):
    return min(lista) if lista else None
4.3 Crea el setup.py
Debe usar find_packages() para detectar la carpeta analisis.

Python

from setuptools import setup, find_packages

setup(
    name="procesador_datos",
    version="0.1",
    packages=find_packages(),
    description="Paquete para limpieza y cálculo de estadísticas básicas."
)
4.4 Genera la distribución
PowerShell

python setup.py sdist bdist_wheel
4.5 Instálalo desde una carpeta diferente
PowerShell

cd ..
python -m pip install .\practica_14-distribucion-paquetes\practica_05-procesador_datos\dist\procesador_datos-0.1.tar.gz --upgrade
4.6 Prueba el paquete
Desde la terminal (fuera de la carpeta del proyecto), entra en Python y prueba:

Python

>>> from analisis.limpieza import eliminar_nulos
>>> from analisis.estadisticas import promedio, maximo, minimo

>>> datos = [12, None, 34, 8, None, 25]

>>> limpios = eliminar_nulos(datos)
>>> print("Datos limpios:", limpios)
Datos limpios: [12, 34, 8, 25]
>>> print("Promedio:", promedio(limpios))
Promedio: 19.75
>>> print("Máximo:", maximo(limpios))
Máximo: 34
>>> print("Mínimo:", minimo(limpios))
Mínimo: 8
4.7 Realiza las mismas pruebas anteriores desde un notebook de Jupyter
Instala Jupyter en este mismo entorno (python -m pip install notebook).

Lanza jupyter notebook.

En una celda, importa y prueba las funciones con la lista de datos.