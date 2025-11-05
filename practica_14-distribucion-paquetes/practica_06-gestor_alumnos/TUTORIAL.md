# Guion de la Práctica 06: Paquete Gestor de Alumnos

Este documento detalla los pasos para crear el paquete `gestor_alumnos`.

---

## 5. Crea un paquete llamado gestor_alumnos

El paquete debe tener:
* Un subpaquete `notas`.
* El subpaquete `notas` debe contener los módulos `promedio.py` y `ranking.py`.

### 5.1 Estructura del Proyecto

(En nuestro repositorio, esta es la carpeta `practica_06-gestor_alumnos`).

gestor_alumnos/ 
├── notas/ │ 
├── init.py 
│ ├── promedio.py 
│ └── ranking.py 
└── setup.py



### 5.2 Implementa los módulos

#### `notas/promedio.py`

Debe calcular la media de notas de una lista.

```python
def calcular_media(notas):
    """Calcula el promedio de una lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
notas/ranking.py
Debe ordenar los alumnos (diccionarios) por nota descendente.

Python

def ordenar_por_nota(alumnos):
    """Ordena una lista de diccionarios de alumnos por su clave 'nota' descendente."""
    return sorted(alumnos, key=lambda alumno: alumno.get('nota', 0), reverse=True)
5.3 Crea el setup.py
Debe usar find_packages() para detectar la carpeta notas.

Python

from setuptools import setup, find_packages

setup(
    name="gestor_alumnos",
    version="0.1",
    packages=find_packages(),
    description="Paquete para gestionar notas y rankings de alumnos."
)
5.4 Genera su distribución
Desde la raíz de este proyecto (practica_06...):

PowerShell

python setup.py sdist bdist_wheel
5.5 Instálalo desde otra carpeta y pruébalo
Desde la raíz del repositorio (verbose-bigdata):

PowerShell

# 1. Instalar
python -m pip install .\practica_14-distribucion-paquetes\practica_06-gestor_alumnos\dist\gestor_alumnos-0.1.tar.gz --upgrade

# 2. Entrar en Python
python
Python

# 3. Probar en la consola
>>> from notas.promedio import calcular_media
>>> from notas.ranking import ordenar_por_nota
>>> alumnos = [{'nombre': 'Ana', 'nota': 8.5}, {'nombre': 'Luis', 'nota': 9.2}, {'nombre': 'Sara', 'nota': 7.8}]
>>> print("Media:", calcular_media([a['nota'] for a in alumnos]))
Media: 8.5
>>> print("Ranking:", ordenar_por_nota(alumnos))
Ranking: [{'nombre': 'Luis', 'nota': 9.2}, {'nombre': 'Ana', 'nota': 8.5}, ...]
5.6 Pruébalo también en un notebook
Instala Jupyter en este mismo entorno (python -m pip install notebook).

Lanza jupyter notebook.

En una celda, importa y prueba las funciones calcular_media y ordenar_por_nota