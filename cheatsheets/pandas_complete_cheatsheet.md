# 📘 Cheatsheet Completo: Pandas, KPIs, Data Cleaning & Visualización

## Tabla de Contenidos
- [Data Cleaning](#1--data-cleaning-limpieza-de-datos)
- [Cálculo Rápido y Lambdas](#2--trucos-de-cálculo-rápido-y-funciones-lambda)
- [KPIs de Negocio](#3--cálculo-de-kpis-de-negocio-recetas-listas)
- [Series Temporales](#4--series-temporales-y-fechas)
- [Agregaciones Avanzadas](#5--agregaciones-avanzadas-groupby--transform)
- [Feature Engineering](#6--feature-engineering-crear-nuevas-variables)
- [Funciones Salvavidas](#-resumen-de-funciones-salvavidas)
- [Examen Pro](#-cheatsheet-anexo-examen-pro)
- [Visualización de Datos](#-cheatsheet-visualización-de-datos-en-python)

---

## 1. 🧹 Data Cleaning (Limpieza de Datos)

Antes de calcular nada, tus datos deben estar limpios.

### Manejo de Nulos (NaN)

```python
# Ver nulos
df.isnull().sum()

# Borrar filas con nulos en columnas específicas
df.dropna(subset=['columna_clave'], inplace=True)

# Rellenar nulos (Imputación)
df['columna'].fillna(0, inplace=True)           # Con un valor fijo
df['columna'].fillna(method='ffill', inplace=True) # Con el valor anterior (útil en series de tiempo)
```

### Manejo de Duplicados

```python
# Ver duplicados
df.duplicated().sum()

# Borrar duplicados
df.drop_duplicates(inplace=True)
```

### Conversión de Tipos (Casting)

Crucial para fechas y números que vienen como texto.

```python
# A fecha (DateTime)
df['fecha'] = pd.to_datetime(df['fecha'])

# A numérico (forzando errores a NaN)
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')

# A categoría (ahorra memoria)
df['categoria'] = df['categoria'].astype('category')
```

### Filtros Rápidos (Masking)

```python
# Filtrar filas
df_activos = df[df['estado'] == 'Activo']
df_pago = df[df['precio'] > 0]

# Filtro con múltiples condiciones (& = AND, | = OR)
df_segmento = df[(df['edad'] > 18) & (df['pais'] == 'España')]
```

---

## 2. ⚡ Trucos de Cálculo Rápido y Funciones Lambda

### apply() con lambda: La navaja suiza

Aplica una función personalizada a cada fila o columna. Es más lento que la vectorización pura, pero muy flexible.

```python
# Ejemplo: Categorizar precios
# Si precio < 20 -> 'Bajo', si no -> 'Alto'
df['tipo_precio'] = df['precio'].apply(lambda x: 'Bajo' if x < 20 else 'Alto')

# Ejemplo: Extraer dominio de un email
df['dominio'] = df['email'].apply(lambda x: x.split('@')[1])
```

### Vectorización (¡Más rápido que apply!)

Siempre que puedas, usa operaciones directas de Pandas/Numpy.

```python
# Malo (Lento con bucles o apply)
# df['total'] = df.apply(lambda row: row['precio'] * row['cantidad'], axis=1)

# Bueno (Vectorizado - Instantáneo)
df['total'] = df['precio'] * df['cantidad']
```

### np.where(): El "IF" de Excel para Pandas

Ideal para crear columnas condicionales masivas.

```python
import numpy as np
# Crear columna 'Status' basada en condiciones
df['status'] = np.where(df['dias_activos'] > 30, 'Fiel', 'Nuevo')
```

---

## 3. 📊 Cálculo de KPIs de Negocio (Recetas Listas)

Aquí tienes las fórmulas de los ejercicios traducidas a código Pandas eficiente.

### Tasa de Conversión (%)

```python
# (Usuarios que compraron / Total usuarios) * 100
tasa_conv = (df['compro'].sum() / len(df)) * 100
```

### ARPU (Average Revenue Per User)

```python
# Ingresos Totales / Usuarios Únicos
arpu = df['monto'].sum() / df['usuario_id'].nunique()
```

### CAC (Customer Acquisition Cost)

```python
# Gasto Marketing / Nuevos Clientes
# Asumiendo un DataFrame de marketing agrupado por canal
df_mkt['CAC'] = df_mkt['gasto_marketing'] / df_mkt['nuevos_clientes']
```

### Churn Rate (Tasa de Cancelación)

```python
# (Clientes Cancelados / Clientes al Inicio) * 100
churn_rate = (clientes_cancelados / clientes_inicio) * 100
```

### Ticket Promedio

```python
# Promedio del monto de las transacciones
ticket_promedio = df_transacciones['monto'].mean()
```

### LTV (Lifetime Value) Simple

```python
# ARPU * Vida media del cliente (1 / Churn Rate)
ltv = arpu * (1 / (churn_rate / 100))
```

---

## 4. 📅 Series Temporales y Fechas

### Extracción de partes de la fecha (.dt accessor)

```python
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.day_name()
df['anio_mes'] = df['fecha'].dt.to_period('M') # Formato '2024-01'
```

### Diferencias de Tiempo (timedelta)

Para calcular días entre dos fechas (ej: Tiempo de Conversión).

```python
df['dias_conversion'] = (df['fecha_compra'] - df['fecha_registro']).dt.days
```

### Rolling Windows (Medias Móviles)

Para suavizar gráficas y ver tendencias.

```python
# Media móvil de 7 días
df['media_movil_7d'] = df['ventas'].rolling(window=7).mean()
```

### Resampling (Re-muestreo)

Cambiar la frecuencia de los datos (ej: de diario a mensual).

```python
# Suma de ventas mensual
df_mensual = df.set_index('fecha').resample('M')['ventas'].sum()
```

---

## 5. 🏗️ Agregaciones Avanzadas (groupby + transform)

### groupby() Básico

Te reduce la tabla (ej: 1 fila por país).

```python
# Ventas totales por país
df.groupby('pais')['ventas'].sum()
```

### transform(): El truco para NO reducir filas

Calcula una estadística grupal pero la pega en cada fila original. Vital para comparar individuos vs su grupo.

```python
# Calcular el promedio de ventas de SU país y pegarlo al lado de cada usuario
df['promedio_pais'] = df.groupby('pais')['ventas'].transform('mean')

# Ahora puedes filtrar quién vende más que el promedio de su país
df_top = df[df['ventas'] > df['promedio_pais']]
```

---

## 6. 🏆 Feature Engineering (Crear nuevas variables)

### Binning (Categorizar números en rangos)

Convertir edad en 'Joven', 'Adulto', 'Senior'.

```python
bins = [0, 18, 35, 60, 100]
labels = ['Niño', 'Joven', 'Adulto', 'Senior']
df['grupo_edad'] = pd.cut(df['edad'], bins=bins, labels=labels)
```

### One-Hot Encoding (Variables Dummy)

Convertir categorías a columnas binarias (0/1) para Machine Learning.

```python
# De columna 'pais' -> columnas 'pais_España', 'pais_Mexico', etc.
df_dummies = pd.get_dummies(df['pais'], prefix='pais')
```

### Extracción de Texto (.str accessor)

```python
# Contar palabras en una reseña
df['num_palabras'] = df['review'].str.split().str.len()

# Buscar palabras clave (contiene 'error'?)
df['tiene_error'] = df['log'].str.contains('error', case=False)
```

---

## 💡 Resumen de Funciones "Salvavidas"

| Función | ¿Qué hace? | Ejemplo |
|---------|-----------|---------|
| `df.describe()` | Resumen estadístico rápido | `df.describe()` |
| `df.value_counts()` | Cuenta frecuencias únicas | `df['pais'].value_counts()` |
| `df.nunique()` | Cuenta valores únicos | `df['user_id'].nunique()` |
| `df.sort_values()` | Ordena la tabla | `df.sort_values('fecha', ascending=False)` |
| `df.pivot_table()` | Crea tablas dinámicas tipo Excel | `df.pivot_table(index='mes', columns='pais', values='ventas')` |
| `pd.concat()` | Pega tablas (una abajo de otra) | `pd.concat([df_enero, df_febrero])` |
| `pd.merge()` | Une tablas por clave (como VLOOKUP/SQL JOIN) | `pd.merge(df_ventas, df_clientes, on='cliente_id')` |

---

## 🎓 Cheatsheet: Anexo "Examen Pro"

Estas son las funciones que te salvarán cuando te pidan cosas específicas de estructura o filtrado avanzado.

### 1. 🔍 Selección y Filtrado (El clásico `loc` vs `iloc`)

En los exámenes adoran preguntar esto.
* `.loc`: Filtras por ETIQUETA (nombre de columna o condición lógica).
* `.iloc`: Filtras por POSICIÓN (índice numérico, como en Excel).

```python
# Dame las filas donde la edad sea > 18, y solo las columnas 'nombre' y 'email'
df.loc[df['edad'] > 18, ['nombre', 'email']]

# Dame las primeras 5 filas y las primeras 3 columnas (por posición pura)
df.iloc[0:5, 0:3]
```

### 2. 🔄 Unir Tablas (`merge` y `concat`)

Si el examen tiene dos datasets (ej: `clientes` y `ventas`), usarás esto seguro.

#### `pd.merge()` (Como el BUSCARV / VLOOKUP de Excel o JOIN de SQL)

```python
# Unir ventas con clientes usando el 'cliente_id' como llave
# how='left' -> Me quedo con todas las ventas, si no hay cliente pone NaN
# how='inner' -> Solo filas donde haya coincidencia en ambos lados
df_total = pd.merge(df_ventas, df_clientes, on='cliente_id', how='left')
```

#### `pd.concat()` (Pegar uno debajo de otro)

```python
# Pegar las ventas de enero debajo de las ventas de febrero
df_anual = pd.concat([df_enero, df_febrero], axis=0)
```

### 3. 📊 Tablas Dinámicas (`pivot_table`)

Si te piden "Resumir las ventas por Región y Producto en una tabla", no uses `groupby`, usa `pivot_table`. Es más limpio visualmente.

```python
# Filas = Región, Columnas = Producto, Valores = Suma de Ventas
tabla = df.pivot_table(index='region', 
                       columns='producto', 
                       values='ventas', 
                       aggfunc='sum', 
                       fill_value=0) # Rellena huecos con 0
```

### 4. 🔢 Ordenar y Rankear (`sort_values`)

Fundamental para "Top 10" o "Los peores".

```python
# Ordenar por Ventas (descendiente) y luego por Fecha (ascendente)
df.sort_values(by=['ventas', 'fecha'], ascending=[False, True], inplace=True)

# Dame los 5 mejores
df.head(5)
```

### 5. 🛠️ Limpieza Rápida (`replace` y `astype`)

#### `replace`: Para corregir errores tipográficos masivos.

```python
# Cambiar 'M' por 'Male' y 'F' por 'Female' en toda la columna
df['genero'] = df['genero'].replace({'M': 'Male', 'F': 'Female'})
```

#### `astype`: Para cambiar tipos de datos (vital para memoria y cálculos).

```python
# Convertir texto a número
df['precio'] = df['precio'].astype(float)
```

### ⚡ Trucos para Cálculos Rápidos (La Magia de Lambda)

En un examen, el tiempo es oro. `apply` con `lambda` es tu navaja suiza para lógica compleja que no sabes hacer con funciones nativas.

**Estructura:** `df['col'].apply(lambda x: FORMULA)`
* Léelo así: "Por cada valor `x` en la columna, aplícale esta fórmula".

#### Truco 1: Categorización rápida (IF/ELSE en una línea)

```python
# Si la nota es > 5 es 'Aprobado', si no 'Suspenso'
df['estado'] = df['nota'].apply(lambda x: 'Aprobado' if x >= 5 else 'Suspenso')
```

#### Truco 2: Limpieza de Strings sucios

Imagina que tienes precios como "100 €" y quieres quitar el símbolo.

```python
# Toma el string x, reemplaza '€' por nada, y conviértelo a float
df['precio_limpio'] = df['precio_sucio'].apply(lambda x: float(x.replace('€', '').strip()))
```

#### Truco 3: Operar con dos columnas a la vez

Cuidado aquí: `axis=1` significa "recorre por filas".

```python
# Si la columna A es mayor que la B, resta A-B, si no, pon 0
df['diferencia'] = df.apply(lambda row: row['A'] - row['B'] if row['A'] > row['B'] else 0, axis=1)
```

---

## 📊 Cheatsheet: Visualización de Datos en Python

### 1. 🔌 Setup Inicial

Siempre empieza tu notebook importando las librerías de gráficos.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración opcional para que se vean más bonitos por defecto
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6)) # Tamaño por defecto (ancho, alto)
```

### 2. 📉 Gráficos Rápidos (Directo desde Pandas)

Ideales para un vistazo rápido sin escribir mucho código.

```python
# Histograma (Distribución de una variable)
df['ataque'].plot(kind='hist', bins=20, title='Distribución de Ataque')

# Gráfico de Barras (Para conteos o comparaciones)
df['tipo_1'].value_counts().plot(kind='bar', color='skyblue')

# Gráfico de Línea (Series temporales / Fechas)
df.plot(x='fecha', y='ventas', kind='line')
```

### 3. 🎨 Gráficos Estadísticos (Seaborn)

Más bonitos y potentes para análisis profundo.

#### A. Detectar Outliers (Boxplot) 📦

El gráfico de la "caja y bigotes". Muestra el rango, la mediana y los puntos raros.

```python
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['ataque'])
plt.title('Detección de Outliers en Ataque')
plt.show()
```

#### B. Ver Correlaciones (Scatterplot) 🌌

La "nube de puntos". Clave para ver relaciones (ej: Ataque vs Defensa).

```python
plt.figure(figsize=(10, 6))
# hue='tipo_1' pinta los puntos de colores según su categoría
sns.scatterplot(data=df, x='ataque', y='defensa', hue='tipo_1', alpha=0.6)
plt.title('Ataque vs Defensa (Glass Cannons)')
plt.show()
```

#### C. Comparar Categorías (Barplot) 📊

Mejor que el de Pandas porque calcula promedios automáticamente.

```python
# Muestra el PROMEDIO de ataque por cada tipo
sns.barplot(data=df, x='type_1', y='attack')
plt.xticks(rotation=45) # Gira las etiquetas si no caben
plt.show()
```

#### D. Mapa de Calor (Heatmap) 🔥

Para ver correlaciones entre todas las variables numéricas a la vez.

```python
matriz_corr = df[['attack', 'defense', 'stamina', 'speed']].corr()
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm')
plt.title('Mapa de Correlación')
plt.show()
```

### 4. 🛠️ Personalización (Hazlo Profesional)

Añade esto antes de `plt.show()` para que tu gráfico se entienda.

```python
plt.title('Título Grande y Descriptivo')
plt.xlabel('Etiqueta Eje X (ej: Puntos de Ataque)')
plt.ylabel('Etiqueta Eje Y (ej: Puntos de Defensa)')

# Cambiar tamaño (Ancho, Alto) en pulgadas
plt.figure(figsize=(12, 8))

# Rotar etiquetas del eje X (útil si son nombres largos)
plt.xticks(rotation=45)
```

### 5. 💾 Guardar el Gráfico

Para ponerlo en tu PowerPoint o informe.

```python
# Guarda lo que has dibujado en un archivo imagen
plt.savefig('mi_grafico_increible.png', dpi=300, bbox_inches='tight')
# dpi=300: Alta calidad
# bbox_inches='tight': Que no se corten los bordes
```

---

## 📝 Licencia

Este documento es de uso libre para fines educativos.

