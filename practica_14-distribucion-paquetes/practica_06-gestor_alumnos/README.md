# Práctica 06: Paquete con Subpaquetes (Gestor de Alumnos)

Este directorio contiene la última práctica de la serie, enfocada en la distribución de una utilidad de negocio que requiere múltiples módulos y funciones para trabajar con datos estructurados (listas de diccionarios).

**Objetivo:** Crear el paquete `gestor_alumnos` que contiene el subpaquete `notas`, con módulos para el cálculo de promedios y la generación de rankings.

## 📜 Contenido del Paquete

* **`notas/`**: Subpaquete principal.
    * **`promedio.py`**: Contiene la función `calcular_media()`.
    * **`ranking.py`**: Contiene la función `ordenar_por_nota()` (usa lambdas para ordenar diccionarios).
* **`setup.py`**: Utiliza `packages=find_packages()` para identificar la estructura.
* **`prueba_alumnos.ipynb`**: El notebook utilizado para verificar la funcionalidad en Jupyter.

## 🚀 Cómo usar este proyecto

Para probar el paquete, sigue estos pasos desde este directorio (`practica_06-gestor_alumnos/`).

### 1. Preparar el Entorno

Asegúrate de que el entorno `.venv` está activo.

```powershell
# 1. Instalar dependencias (setuptools, wheel, notebook, etc.)
python -m pip install -r requirements.txt
2. Construir e Instalar
PowerShell

# 1. Construir la distribución
python setup.py sdist bdist_wheel

# 2. Instalar el paquete en el entorno (desde la raíz)
cd ..
python -m pip install .\practica_06-gestor_alumnos\dist\gestor_alumnos-0.1.tar.gz
3. Pruebas y Verificación
Las pruebas demuestran la importación a dos niveles (from notas.ranking import...) y el correcto manejo de las estructuras de datos (lista de diccionarios).

PowerShell

# Ejemplo de prueba en Python REPL
python
>>> from notas.promedio import calcular_media
>>> from notas.ranking import ordenar_por_nota
>>> alumnos = [{'nombre': 'Ana', 'nota': 8.5}, {'nombre': 'Luis', 'nota': 9.2}, {'nombre': 'Sara', 'nota': 7.8}]
>>> print("Media:", calcular_media([a['nota'] for a in alumnos]))
Media: 8.5
>>> print("Ranking:", ordenar_por_nota(alumnos))
Ranking: [{'nombre': 'Luis', 'nota': 9.2}, {'nombre': 'Ana', 'nota': 8.5}, ...]
>>> exit()