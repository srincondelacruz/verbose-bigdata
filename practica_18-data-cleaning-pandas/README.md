# Práctica 18: Data Cleaning y Manipulación con Pandas

Este directorio contiene la práctica completa sobre **Limpieza de Datos (Data Cleaning)** y **Análisis Exploratorio (EDA)**, estructurada en 12 módulos temáticos.

## 🎯 Objetivo

Dominar la librería Pandas para transformar datasets "sucios" en datos listos para análisis, cubriendo desde la selección básica hasta el manejo avanzado de índices y *outliers*.

## 🗂️ Índice de Contenidos y Notebooks

### 📚 Fundamentos
* **[01. Introducción](./01-IntroductionToPandas/Intro.ipynb)**: Carga de datos, estructuras DataFrame/Series y exploración inicial (`shape`, `info`).
* **[02. Análisis Exploratorio (EDA)](./02-Exploratory_Data_Analysis/EDA.ipynb)**: Estadísticas descriptivas (`describe`), detección de duplicados y tipos de datos.

### ✂️ Selección y Manipulación
* **[03. Slicing and Dicing](./03-Slicing_and_Dicing/Slicing.ipynb)**: Selección de subconjuntos con `loc` e `iloc`.
* **[04. Manipulación de Índices](./04-Index_Manipulation/Index-Manipulation.ipynb)**: `set_index`, `reset_index` y uso de índices para búsquedas.
* **[05. Selección Condicional](./05-Conditional_Selection/Conditional-Selection.ipynb)**: Filtrado de datos basado en condiciones booleanas y máscaras.

### 🛠️ Modificación de Estructura
* **[06. Añadir/Eliminar Filas y Columnas](./06-Adding_Dropping_Rows_Cols/Add-Drop.ipynb)**: Uso de `drop`, `concat` y creación de columnas calculadas.
* **[07. Ordenación](./07-Sorting_Data/Sorting.ipynb)**: Ordenar valores (`sort_values`) y orden por índice.
* **[08. Actualización](./08-Updating_Rows_Cols/Update-row-cols.ipynb)**: Renombrar columnas y actualizar valores específicos.

### 🧹 Limpieza de Datos (Data Cleaning)
* **[09. Manejo de Valores Nulos](./09-Handling_Missing_Values/Missing-Values.ipynb)**: Detección (`isna`), eliminación (`dropna`) e imputación (`fillna`).
* **[10. Limpieza Avanzada](./10-Data_Cleaning_Part2/Data-Cleaning2.ipynb)**: Técnicas adicionales de estandarización y limpieza de strings.

### 🔍 Avanzado
* **[11. Indexación Avanzada](./11-Advanced_Indexing/Advanced-Index.ipynb)**: Multi-índices (Hierarchical Indexing) y operaciones avanzadas.
* **[12. Manejo de Outliers](./12-Handling_Outliers/Untitled-1.ipynb)**: Detección y tratamiento de valores atípicos estadísticos.

---

## 🛠️ Herramientas

* **Librerías:** `pandas`, `numpy`, `matplotlib` (para visualización básica).
* **Dataset:** `Customers.csv` / `survey_results_public.csv`.
