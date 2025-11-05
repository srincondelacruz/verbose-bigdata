# Práctica 01: Creación y Distribución de Paquetes

Este directorio contiene la primera práctica del módulo de Big Data, enfocada en el ciclo de vida de un paquete de Python.

**Objetivo:** Aprender a estructurar, empaquetar, distribuir e instalar un paquete de Python utilizando `setuptools` y `wheel`.

## 📜 Contenido del Paquete

* **`paquete/`**: El paquete fuente, que contiene:
    * `hola/`: Un sub-paquete con la función `saludar()` (y `prueba()` a partir de la v0.2).
    * `adios/`: Un sub-paquete con la función `despedir()`.
* **`setup.py`**: El script de configuración que le dice a `setuptools` cómo construir el paquete (actualmente en v0.2).
* **`requirements.txt`**: Las dependencias necesarias para *desarrollar* y *distribuir* este paquete (ej. `twine`, `wheel`).

## 🚀 Cómo usar este proyecto

Para probar el paquete, sigue estos pasos desde este directorio (`practica_01-distribucion/`).

### 1. Preparar el Entorno

Asegúrate de tener el entorno virtual activado.

```powershell
# 1. (Si no existe) Crear el entorno
python -m venv .venv

# 2. Activar el entorno
.\.venv\Scripts\Activate.ps1

# 3. Instalar las dependencias de desarrollo (wheel, twine, etc.)
pip install -r requirements.txt
2. Instalar en Modo Editable (Desarrollo)
Esto te permite probar el paquete localmente. Cualquier cambio en los archivos .py se reflejará al instante.

PowerShell

# Instalar el paquete en modo editable
pip install -e .

# Probarlo (ejecutar 'python' e importar)
# >>> from paquete.hola.saludos import saludar
# >>> saludar()
3. Construir y Probar la Distribución Real
Esto simula cómo un usuario final instalaría el paquete.

PowerShell

# 1. Construir los archivos .whl y .tar.gz (aparecerán en la carpeta /dist)
python setup.py sdist bdist_wheel

# 2. Desinstalar la versión editable (si la tenías)
pip uninstall paquete -y

# 3. Instalar la versión "real" desde el archivo generado (ej. v0.2)
pip install dist\paquete-0.2.tar.gz --upgrade

# 4. Probarlo (ej. la nueva función de la v0.2)
# >>> from paquete.hola.saludos import prueba
# >>> prueba()
4. (Opcional) Publicar en TestPyPI
Para publicar nuevas versiones en el índice de paquetes de prueba de PyPI.

PowerShell

# Subir los paquetes de la carpeta /dist
python -m twine upload --repository testpypi dist/*

---