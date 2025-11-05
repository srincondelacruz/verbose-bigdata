# Práctica 05: Paquete de Análisis de Datos (Procesador Datos)

Este directorio contiene la Práctica 5, la cual demuestra la creación de un paquete con utilidades enfocadas en la manipulación y estadística básica de listas.

**Objetivo:** Crear el paquete `procesador_datos` que contiene el subpaquete `analisis`, con los módulos `limpieza.py` (para manejo de nulos) y `estadisticas.py` (para promedio, máximo, mínimo).

## 📜 Contenido del Paquete

* **`analisis/`**: Carpeta principal del paquete (subpaquete).
    * **`limpieza.py`**: Contiene `eliminar_nulos()`.
    * **`estadisticas.py`**: Contiene `promedio()`, `maximo()`, y `minimo()`.
* **`setup.py`**: Utiliza `packages=find_packages()` para identificar la jerarquía.
* **`prueba_datos.ipynb`**: El notebook utilizado para verificar la funcionalidad en Jupyter.

## 🚀 Cómo usar este proyecto

Para probar el paquete, sigue estos pasos desde este directorio (`practica_05-procesador_datos/`).

### 1. Preparar el Entorno

Asegúrate de que el entorno `.venv` está activo.

```powershell
# 1. Instalar dependencias (setuptools, wheel, notebook, etc.)
python -m pip install -r requirements.txt
2. Construir e Instalar
PowerShell

# 1. Construir la distribución
python setup.py sdist bdist_wheel

# 2. Instalar el paquete en el entorno (desde la raíz para simular un usuario externo)
cd ..
python -m pip install .\practica_05-procesador_datos\dist\procesador_datos-0.1.tar.gz
3. Pruebas y Verificación
Las pruebas demuestran el correcto manejo de valores nulos y el cálculo estadístico.

PowerShell

# Ejemplo de prueba en Python REPL
python
>>> from analisis.limpieza import eliminar_nulos
>>> from analisis.estadisticas import promedio, maximo, minimo

>>> datos = [12, None, 34, 8, None, 25]
>>> limpios = eliminar_nulos(datos)
>>> print(f"Datos limpios: {limpios}")
Datos limpios: [12, 34, 8, 25]
>>> print(f"Promedio: {promedio(limpios)}")
Promedio: 19.75
>>> exit()