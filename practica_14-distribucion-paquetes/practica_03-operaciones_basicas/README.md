# Práctica 03: Paquete Simple (Módulo Único)

Este directorio contiene la Práctica 3, enfocada en crear y distribuir un paquete de Python basado en un **único módulo** (`.py`) en lugar de un paquete con subdirectorios.

**Objetivo:** Aprender a empaquetar un módulo simple usando `py_modules` en `setup.py` y probarlo tanto en la terminal como en Jupyter.

## 📜 Contenido del Paquete

* **`operaciones.py`**: El módulo fuente con las funciones `sumar` y `restar`.
* **`setup.py`**: El script de configuración que usa `py_modules=['operaciones']` para el empaquetado.
* **`requirements.txt`**: Las dependencias de desarrollo (ej. `setuptools`, `wheel`, `notebook`).
* **`prueba_operaciones.ipynb`**: El notebook usado para verificar que el paquete instalado funciona en Jupyter.

## 🚀 Cómo usar este proyecto

Para probar el paquete, sigue estos pasos desde este directorio (`practica_03-operaciones_basicas/`).

### 1. Preparar el Entorno

```powershell
# 1. (Si no existe) Crear el entorno
python -m venv .venv

# 2. Activar el entorno
.\.venv\Scripts\Activate.ps1

# 3. Instalar las dependencias de desarrollo
python -m pip install -r requirements.txt
2. Construir e Instalar el Paquete
PowerShell

# 1. Construir los archivos .whl y .tar.gz
python setup.py sdist bdist_wheel

# 2. Instalar el paquete en el entorno
# (Lo hacemos desde la raíz para simular un usuario externo)
cd ..
python -m pip install .\practica_03-operaciones_basicas\dist\operaciones_basicas-0.1.tar.gz
cd practica_03-operaciones_basicas
3. Probar el Paquete
Una vez instalado, el paquete operaciones está disponible en todo el entorno.

Prueba A: Terminal (REPL)
PowerShell

# 1. Entrar en Python
python

# 2. Probar
>>> from operaciones import sumar
>>> sumar(10, 5)
15
>>> exit()
Prueba B: Jupyter Notebook
PowerShell

# 1. Lanzar Jupyter
jupyter notebook

# 2. Abrir el notebook
El archivo prueba_operaciones.ipynb contiene las mismas pruebas (from operaciones import sumar, restar) que demuestran que el paquete es accesible desde el kernel de Jupyter.

