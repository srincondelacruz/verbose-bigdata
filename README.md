# 🚀 Data Engineering Portfolio

<div align="center">

![Banner](https://img.shields.io/badge/🎯_Data_Engineering-Portfolio-0066CC?style=for-the-badge&labelColor=1a1a2e)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)](https://databricks.com)
[![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)](https://spark.apache.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)

**Repositorio con +18 proyectos prácticos de Big Data e Ingeniería de Datos**

[🔥 Proyectos Destacados](#-proyectos-destacados) • [📊 Cloud & Pipelines](#-cloud--data-pipelines) • [⚡ Big Data](#-big-data--procesamiento) • [🐍 Python](#-python-avanzado)

</div>

---

## 🔥 Proyectos Destacados

<table>
<tr>
<td width="50%">

### 🏆 [End-to-End Data Engineering](./practica_41-End-to-End-DE/)
Pipeline completo de ingeniería de datos: migración SQL Server → Azure Data Lake → Databricks (arquitectura medallion Bronze/Silver/Gold) → Power BI.

**Stack:** `Azure Data Factory` `Data Lake Gen2` `Databricks` `Synapse Analytics` `Power BI` `Key Vault`

</td>
<td width="50%">

### 🌤️ [Streaming Meteo Azure](./practica_32-Batch-Streaming-Azure-Databricks-PowerBI/)
Pipeline end-to-end de datos meteorológicos con ingesta batch y streaming, arquitectura medallion y dashboards en tiempo real.

**Stack:** `Event Hubs` `Data Lake Gen2` `Databricks` `Data Factory` `Power BI`

</td>
</tr>
<tr>
<td width="50%">

### 🔄 [ELT Pipeline con dbt](./practica_34-ELT-con-dbt/)
Pipeline ELT moderno para análisis de ventas Walmart siguiendo mejores prácticas: staging → intermediate → marts.

**Stack:** `dbt` `PostgreSQL` `Docker` `Python`

</td>
<td width="50%">

### 🧠 [Vector DB + AI Foundry](./practica_29-MongoDB-AzureAIFoundry/)
Base de datos vectorial con MongoDB Atlas y Azure AI Foundry para búsqueda semántica y embeddings.

**Stack:** `MongoDB Atlas` `Azure AI Foundry` `Vector Embeddings`

</td>
</tr>
</table>

---

## 📊 Cloud & Data Pipelines

| # | Proyecto | Descripción | Tecnologías |
|:-:|:---------|:------------|:------------|
| **41** | [End-to-End DE Project](./practica_41-End-to-End-DE/) | Pipeline completo: SQL Server local → Lakehouse → ML → Power BI. Arquitectura medallion (Bronze/Silver/Gold) | `Azure` `Databricks` `Synapse` `Power BI` |
| **35** | [Data Warehouse Azure](./practica_35-Data_Warehouse_Azure/) | Implementación de Data Warehouse en la nube de Azure | `Azure Synapse` `Data Warehouse` |
| **34** | [ELT con dbt](./practica_34-ELT-con-dbt/) | Pipeline ELT moderno: Extract, Load, Transform con arquitectura por capas | `dbt` `PostgreSQL` `Docker` |
| **32** | [Batch & Streaming Azure](./practica_32-Batch-Streaming-Azure-Databricks-PowerBI/) | Flujo completo batch/streaming con datos meteorológicos y dashboards real-time | `Event Hubs` `Databricks` `Power BI` |
| **29** | [MongoDB + AI Foundry](./practica_29-MongoDB-AzureAIFoundry/) | Base de datos vectorial y búsqueda semántica con IA | `MongoDB` `Azure AI` `Embeddings` |
| **28** | [BD Vectorial FE](./practica_28-BD_vectorial_FE/) | Feature Engineering con base de datos vectorial PostgreSQL | `PostgreSQL` `pgvector` `Azure` |
| **27** | [SQL Server → Lakehouse](./practica_27-De_SQL_Server_local_a_Lakehouse,_Power_BI_y_ML/) | Migración on-premise a cloud con Data Factory y ML | `Data Factory` `Data Lake` `Spark MLlib` |

---

## ⚡ Big Data & Procesamiento

| # | Proyecto | Descripción | Tecnologías |
|:-:|:---------|:------------|:------------|
| **26** | [Hadoop Ecosystem](./practica_26-hadoop/) | Ecosistema Hadoop: HDFS, MapReduce y procesamiento distribuido | `Hadoop` `HDFS` `Docker` |
| **25** | [Formatos Big Data](./practica_25-formatos_bigdata/) | Comparativa de formatos: Parquet, Avro, ORC, Delta Lake | `Parquet` `Avro` `Delta Lake` |
| **24** | [NumPy Avanzado](./practica_24-numpy/) | Computación numérica eficiente y operaciones vectorizadas | `NumPy` `Python` |
| **23** | [Docker para Data](./practica_23-docker/) | Contenedorización de aplicaciones y servicios de datos | `Docker` `Docker Compose` |
| **22** | [Scala para Spark](./practica_22-scala/) | Fundamentos de Scala para procesamiento con Apache Spark | `Scala` `Spark` |
| **21** | [PySpark Básico](./practica_21-pySpark_basico/) | Procesamiento distribuido: DataFrames, transformaciones y acciones | `PySpark` `Spark SQL` |

---

## 📈 Data Analytics & Feature Engineering

| # | Proyecto | Descripción | Tecnologías |
|:-:|:---------|:------------|:------------|
| **20** | [Feature Engineering](./practica_20-Feature_Engineering/) | Técnicas de ingeniería de características para ML | `Pandas` `NumPy` `Scikit-learn` |
| **19** | [KPIs con Pandas](./practica_19-Pandas%20KPIs/) | Cálculo de métricas de negocio: conversión, tiempo promedio, retención | `Pandas` `Data Analysis` |

---

## 🐍 Python Avanzado

| # | Proyecto | Descripción | Tecnologías |
|:-:|:---------|:------------|:------------|
| **17** | [Herencia en Python](./practica_17-Herencia/) | Métodos de instancia, clase, estáticos. Herencia y `super()` | `OOP` `Python` |
| **16** | [OOP Completo](./practica_16-OOP/) | Pilares de OOP: clases, encapsulación, métodos especiales | `OOP` `Python` |
| **15** | [Comprehensions](./practica_15-Comprehensions/) | List, Dict y Set comprehensions para código pythónico | `Python` |
| **14** | [Data Science Cases](./practica_14-casos_data_science/) | Notebooks con librerías fundamentales de Data Science | `Jupyter` `Pandas` `Matplotlib` |
| **14** | [Distribución Paquetes](./practica_14-distribucion-paquetes/) | Creación y distribución de paquetes Python | `setuptools` `pip` |
| **13** | [Programación Modular](./practica_13-programacion-modular/) | Modularidad, paquetes y refactorización de código | `Python` `Modules` |
| **12** | [Tipos de Argumentos](./practica_12-tipos_de_argumentos/) | Posicionales, keywords, `*args`, `**kwargs`, scope | `Python` |

---

## 📚 Recursos Adicionales

<table>
<tr>
<td>

### 📖 Cheatsheets
- [**Pandas Complete**](./cheatsheets/pandas_complete_cheatsheet.md) - Guía completa de Pandas, KPIs y visualización
- [**PySpark Commands**](./cheatsheets/pyspark_commands.md) - Comandos esenciales de PySpark

</td>
<td>

### 🏆 Proyectos Personales
- [**LeetCode Solutions**](./ejercicios_personales-leetcode/) - Algoritmos y estructuras de datos con análisis de complejidad O(n)

</td>
</tr>
</table>

---

## 🛠️ Stack Tecnológico

<div align="center">

| Categoría | Tecnologías |
|:---------:|:------------|
| **☁️ Cloud** | Azure Data Factory, Data Lake Gen2, Databricks, Synapse Analytics, Event Hubs |
| **📊 BI & Viz** | Power BI, Matplotlib, Seaborn |
| **⚡ Big Data** | Apache Spark, PySpark, Hadoop, Delta Lake |
| **🗄️ Databases** | PostgreSQL, MongoDB, SQL Server, pgvector |
| **🔧 Tools** | Docker, dbt, Git, Jupyter |
| **🐍 Languages** | Python 3.11, Scala, SQL |

</div>

---

<div align="center">

**📫 Contacto** • [LinkedIn](https://linkedin.com) • [GitHub](https://github.com)

![Made with ❤️](https://img.shields.io/badge/Made_with-❤️-red?style=flat-square)
![Big Data](https://img.shields.io/badge/Big_Data-Engineering-blue?style=flat-square)

</div>
