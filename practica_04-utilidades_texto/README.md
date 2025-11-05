# Práctica 04: Paquete con Subpaquetes (Utilidades de Texto)

Este directorio contiene la Práctica 4, la cual demuestra la creación y empaquetado de un proyecto con una **estructura de subpaquetes**.

**Objetivo:** Crear el paquete principal `utilidades_texto` que contiene el subpaquete `texto`, el cual a su vez tiene los módulos `conteo.py` y `formato.py`.

## 🚨 Nota Importante: Estructura

El principal desafío de esta práctica es mantener la estructura correcta para que `find_packages()` funcione.

- **Estructura Requerida:** `utilidades_texto/texto/conteo.py`
- **Solución implementada:** Los módulos `.py` (ej. `conteo.py`) se colocaron **directamente dentro** de la carpeta `texto`, y no dentro de una carpeta anidada.

## 📜 Contenido del Paquete

* **`texto/`**: Carpeta principal del paquete (es el subpaquete de nivel superior).
    * **`conteo.py`**: Funciones para contar palabras y caracteres.
    * **`formato.py`**: Funciones para convertir texto a mayúsculas/minúsculas.
* **`setup.py`**: Utiliza `packages=find_packages()` para que el sistema de empaquetado detecte automáticamente la jerarquía (`texto.conteo` y `texto.formato`).
* **`requirements.txt`**: Dependencias de desarrollo (`setuptools`, `wheel`, `notebook`).
* **`prueba_texto.ipynb`**: El notebook utilizado para verificar la correcta importación.

## 🚀 Cómo usar este proyecto

Para probar el paquete, sigue estos pasos desde este directorio (`practica_04-utilidades_texto/`).

### 1. Preparar el Entorno

Asegúrate de que el entorno `.venv` está activo.

```powershell
# 1. Instalar dependencias (setuptools, wheel, notebook)
python -m pip install -r requirements.txt
2. Construir e Instalar
PowerShell

# 1. Construir la distribución con la estructura final
python setup.py sdist bdist_wheel

# 2. Instalar el paquete en el entorno (desde la raíz para simular un usuario externo)
cd ..
python -m pip install .\practica_04-utilidades_texto\dist\utilidades_texto-0.1.tar.gz --upgrade
3. Pruebas y Verificación
El paquete se prueba mediante la importación de dos niveles de profundidad.

Prueba A: Terminal (REPL)
PowerShell

# 1. Entrar en Python
python

# 2. Probar las funciones
>>> from texto.conteo import contar_palabras
>>> from texto.formato import en_mayusculas

>>> frase = "Python es increíble"
>>> print(f"Palabras: {contar_palabras(frase)}")
Palabras: 3
>>> print(f"Mayúsculas: {en_mayusculas(frase)}")
Mayúsculas: PYTHON ES INCREÍBLE
>>> exit()