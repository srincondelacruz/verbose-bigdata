# Proyecto End-to-End Meteo en Azure

Este repositorio contiene todos los recursos utilizados para el desarrollo del proyecto **Meteo End-to-End en Azure**, un flujo completo de ingesta, procesamiento y consumo de datos meteorológicos tanto en *streaming* como en *batch*, siguiendo la arquitectura **medallion** (Bronze → Silver → Gold).

> [!IMPORTANT] 
> # Para seguir el tutorial hay que leerse el siguiente archivo: [Tutorial end2end](./docs/tutorial_end2end_meteo.md)

## 📁 Estructura del repositorio

### `docs/`

Contiene la documentación del proyecto, incluyendo:

* Descripción funcional y técnica.
* Arquitectura del sistema.
* Diseño del Lakehouse.
* Explicación de los servicios de Azure utilizados.
* Procesos de ingesta, transformación y publicación.

---

### `notebooks_databricks/`

Incluye los **notebooks de Azure Databricks** utilizados para:

* Procesamiento Bronze → Silver.
* Limpieza, normalización y validación de datos.
* Generación de tablas Gold para análisis.

Cada notebook está preparado para ejecutarse directamente en un clúster de Databricks.

---

### `scripts/`

Scripts auxiliares del proyecto, tales como:

* Generación de datos meteorológicos sintéticos.
* Simulación de envío de datos en *streaming* a Event Hubs.

---

## 🚀 Objetivo del proyecto

Crear una pipeline completa de datos meteorológicos usando servicios cloud de Azure, almacenando datos históricos en un Lakehouse y permitiendo su visualización en tiempo real mediante Power BI.

## 🛠️ Servicios principales utilizados

* **Azure Event Hubs** – Ingesta en *streaming*.
* **Azure Data Lake Storage Gen2** – Lakehouse estructurado por niveles.
* **Azure Databricks** – Procesamiento ETL.
* **Power BI** – Dashboards conectados al *tier Gold*.

---

## 📸 Capturas de Pantalla

### 🗄️ Azure Data Lake Storage Gen2

#### Creación del Data Lake
![Crear Data Lake - Paso 1](./screenshots/crear_datalake_1.png)

![Crear Data Lake - Paso 2](./screenshots/crear_datalake_2.png)

#### Configuración del Container y Carpetas
![Crear Container en Data Lake](./screenshots/crear_container_datalake.png)

![Crear Carpeta Landing](./screenshots/crear_carpeta_landing.png)

---

### 📡 Azure Event Hubs

![Crear Event Hubs Namespace](./screenshots/event_hubs_namespace_create.png)

![Crear Event Hub](./screenshots/event_hub_create.png)

![Crear Shared Access Policy](./screenshots/event_hub_shared_access_policy_create.png)

---

### ⚡ Azure Databricks

#### Despliegue y Configuración
![Databricks Desplegado](./screenshots/az_databricks_desplegado.png)

![Lanzar Workspace de Databricks](./screenshots/az_databricks_launch_workspace.png)

#### Compute y Configuración Spark
![Crear Compute en Databricks](./screenshots/databricks_create_compute.png)

![Configuración Spark](./screenshots/databricks_spark_conf.png)

#### Jobs y Scheduling
![Crear Job en Databricks](./screenshots/databricks_create_job.png)

![Nuevo Job Silver-Gold](./screenshots/databricks_nuevo_job_silver_gold.png)

![Job en Ejecución](./screenshots/databricks_job_running.png)

![Programar Job](./screenshots/databricks_schedule_job.png)

![Nuevo Schedule de Job](./screenshots/databricks_new_job_schedule.png)

---

### 🏭 Azure Data Factory

![Crear Data Factory](./screenshots/data_factory_create.png)

![Lanzar Data Factory Studio](./screenshots/adf_launch_studio.png)

![Crear Linked Service para Storage](./screenshots/adf_linked_service_storage_create.png)

---

### 📊 Power BI

#### Conexión a Databricks
![Obtener Datos desde Databricks](./screenshots/power_bi_obtener_datos_databricks.png)

![Obtener Info de Conexión](./screenshots/power_bi_databricks_get_conn_info.png)

![Access Token - Paso 1](./screenshots/power_bi_databricks_access_token_1.png)

![Access Token - Paso 2](./screenshots/power_bi_databricks_access_token_2.png)

![Access Token - Paso 3](./screenshots/power_bi_databricks_access_token_3.png)

#### Configuración de Datos
![Seleccionar Direct Query](./screenshots/power_bi_select_direct_query.png)

![Seleccionar Base de Datos Hive](./screenshots/power_bi_select_hive_db.png)

![Conector ADLS](./screenshots/power_bi_adls_connector.png)

![Configurar Actualización Automática](./screenshots/power_bi_configurar_actu_auto.png)

#### Dashboard Final
![Dashboard Completo en Power BI](./screenshots/PowerBI_dashboard_completo.png)

---

### 🔗 Azure Synapse Analytics

![Crear Synapse](./screenshots/synapse_create.png)
