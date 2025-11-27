# Comandos Clave de PySpark

## 1. Inicialización y Configuración

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql.types import StructType
from pyspark.sql.functions import col
from pyspark.sql.functions import expr

# Inicializa o recupera la sesión de Spark
spark = SparkSession.builder.appName("...").getOrCreate()

# Configura parámetros de Spark a nivel de sesión
spark.setConf("propiedad", "valor")

# Habilita la Ejecución Adaptativa de Consultas (AQE)
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Habilita el soporte de Apache Arrow para UDFs vectorizadas
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
```

## 2. Creación y Carga de DataFrames

```python
# Crea un DataFrame a partir de datos en memoria
spark.createDataFrame(data)
spark.createDataFrame(data=..., schema=esquema)

# Convierte un RDD en un DataFrame
rdd.toDF(columnas)

# Carga datos desde archivos CSV
spark.read.csv("ruta.csv")
spark.read.option("header", True).csv(...)
spark.read.option("inferSchema", True).csv(...)

# Carga datos desde archivos JSON
spark.read.json("ruta.json")
spark.read.option("multiline", True).json(...)

# Carga datos desde archivos Parquet
spark.read.parquet("ruta.parquet")

# Método genérico para cargar datos
spark.read.format("csv").load("ruta")

# Crea un DataFrame a partir de una tabla de catálogo
spark.table('samples.tpch.customer')

# Escribe el DataFrame a archivos
df.write.csv("ruta")
df.write.json("ruta")
df.write.mode("overwrite").save("ruta")
df.write.saveAsTable("nombre_tabla")

# Reduce o cambia el número de particiones
df.coalesce(n)
df.repartition(n)
```

## 3. Inspección y Acciones

```python
# Muestra los datos del DataFrame
df.show(n, truncate=False)

# Muestra el esquema del DataFrame
df.printSchema()

# Devuelve el número total de filas
df.count()

# Devuelve información sobre columnas
df.columns
df.dtypes

# Muestra un sumario estadístico
df.describe().show()

# Devuelve registros
df.first()
df.head(n)
df.collect()
df.take(n)

# Marca el DataFrame para almacenamiento
df.persist()
df.cache()
```

## 4. Transformaciones de Columnas

```python
# Selecciona columnas específicas
df.select("col1", "col2")
df.select(df.col1, (df.col2 + 10).alias("NewCol"))
df.selectExpr("*", "Units * Revenue as total")

# Elimina columnas
df.drop("col1", "col2")

# Añade o modifica columnas
df.withColumn("new_col", expresion)
df.withColumnRenamed("old", "new")

# Cambia el tipo de dato
df.col.cast(T.IntegerType())

# Funciones de columna
F.lit("valor")
F.to_date(df.Date, "M/d/yyy")
F.year("Date")
F.month("Date")
F.concat_ws(" ", col1, col2)
F.trim("Zip")
F.lower("Country")
F.upper("Country")
```

## 5. Transformaciones de Filas (Filtro, Orden y Unión)

```python
# Filtra filas
df.filter(df.col > 10)
df.where(df.col == "Canada")
df.filter((cond1) & (cond2))
df.col.isNull()

# Ordena el DataFrame
df.sort("col")
df.orderBy("col")
df.orderBy(df.col.desc())

# Limita el número de filas
df.limit(n)

# Elimina duplicados
df.distinct()
df.dropDuplicates(["col1", "col2"])

# Une DataFrames
df1.union(df2)
```

## 6. Gestión de Nulos

```python
# Elimina filas con nulos
df.na.drop("any")
df.na.drop("all")
df.na.drop(subset=["col1"])

# Rellena valores nulos
df.na.fill(valor, subset=["col1"])
df.na.fill({"col1": v1, "col2": v2})

# Sustituye valores específicos
df.na.replace(["old"], ["new"], subset=["col"])
```

## 7. Agregaciones

```python
# Agrupa datos
df.groupBy("col")

# Aplica funciones de agregación
.agg(F.sum("revenue").alias("total"))
df.groupBy("col").agg({"Zip": "count", "Revenue": "avg"})

# Funciones de agregación
F.count("col")
F.count_distinct("col")
F.sum("col")
F.avg("col")
F.min("col")
F.max("col")
F.collect_list("col")
F.collect_set("col")

# Tablas pivote
df.groupBy().pivot("col").sum("rev")
```

## 8. Joins (Uniones)

```python
# Une dos DataFrames
df1.join(df2, on="id", how="inner")
df1.join(df2, df1.key == df2.key, "left")

# Tipos de join
how="inner"      # Solo filas coincidentes
how="left"       # Todas las filas del DataFrame izquierdo
how="outer"      # Todas las filas de ambos DataFrames
how="left_anti"  # Registros de la izquierda sin coincidencia
```

## 9. Uso de SQL y Vistas

```python
# Crea vistas temporales
df.createOrReplaceTempView("vista_temp")
df.createOrReplaceGlobalTempView("vista_global")

# Ejecuta consultas SQL
spark.sql("select * from ventas where...")
spark.sql("create database if not exists s8a")

# Persiste/cachea una tabla
spark.catalog.cacheTable("table_name")
```

## 10. Funciones de Ventana (Window Functions)

```python
from pyspark.sql.window import Window

# Define ventanas
Window.partitionBy('col')
Window.orderBy('col')

# Aplica funciones sobre ventanas
F.avg(col('nota')).over(win)

# Define ventanas dinámicas
Window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
Window.rangeBetween(start, end)

# Funciones de ventana específicas
F.rank().over(win)
F.lag('col', n, default).over(win)
F.lead('col', n, default).over(win)
F.last('col', True).over(win)
```

## 11. UDFs (Funciones Definidas por el Usuario)

```python
from pyspark.sql.functions import udf

# Registra una UDF
udfBonus = udf(funcion_python, TipoDato())

# Registra para Spark SQL
spark.udf.register("nombre_sql", funcion_python, tipo)

# UDF vectorizada (más rápida)
@F.pandas_udf(LongType())
def funcion_pandas_udf(s: pd.Series) -> pd.Series:
    return s * 2
```

## 12. Conversión a Pandas

```python
# Convierte a DataFrame de Pandas
df.toPandas()

# Usa la API de Pandas para procesamiento distribuido
df.pandas_api()
```