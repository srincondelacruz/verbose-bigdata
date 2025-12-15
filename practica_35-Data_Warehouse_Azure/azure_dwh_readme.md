# Guía de Implementación: Data Warehouse en Azure

## 📋 Tabla de Contenidos

1. [Parte 1: Creación del Storage (Data Lake)](#parte-1-creación-del-storage-data-lake)
2. [Parte 2: Creación de Azure Data Factory (ADF)](#parte-2-creación-de-azure-data-factory-adf)
3. [Parte 3: Pipeline 1 - Ingesta (Copy Data)](#parte-3-pipeline-1---ingesta-copy-data)
4. [Parte 4: Pipeline 2 - Transformación (Data Flows)](#parte-4-pipeline-2---transformación-data-flows)
5. [Parte 5: Visualización con Power BI](#parte-5-visualización-con-power-bi)
6. [Parte 6: Azure Machine Learning (Extra)](#parte-6-azure-machine-learning-extra)

---

## 📝 Información de la Práctica

**Requisitos obligatorios:**
- Archivo `fact_sales` (obligatorio)
- `dim_customers` y `dim_products` (opcionales)

**Entrega:**
- CSV(s) finales de la carpeta `gold`
- Capturas de pantalla en documento Word

---

## Parte 1: Creación del Storage (Data Lake)

El primer paso es provisionar el almacenamiento que servirá como base para nuestro Data Lake.

### 1.1 Configuración de la Cuenta de Almacenamiento

En el portal de Azure, crear un nuevo recurso de **Storage Account**.

**Configuración:**
- **Suscripción:** Azure for Students (o tu suscripción activa)
- **Grupo de recursos:** Crear nuevo
- **Nombre de la cuenta:** (debe ser único)
- **Región:** France Central (o la más cercana)
- **Rendimiento:** Estándar
- **Redundancia:** LRS (Almacenamiento con redundancia local) para reducir costes

![Configuración Storage Account - imagen1](imagen1.png)

### 1.2 Configuración Avanzada (Data Lake Gen2)

Es crucial habilitar la funcionalidad de espacio de nombres jerárquico para convertir el Blob Storage en un verdadero Data Lake.

**Pasos:**
1. Ir a la pestaña **Avanzado**
2. Marcar la casilla: **Enable hierarchical namespace** (Habilitar espacio de nombres jerárquico)
3. En **Protección de datos**, deshabilitar opciones de recuperación (soft delete) para simplificar este laboratorio

![Configuración avanzada - imagen2](imagen2.png)

### 1.3 Estructura de Contenedores y Directorios

Una vez creado el recurso:

1. Ir a **Contenedores** y crear uno llamado `datalake`
2. Dentro de `datalake`, crear la estructura de carpetas siguiendo la arquitectura **"Medallion"**:
   - `/bronze` (Datos crudos)
   - `/silver` (Datos limpios)
   - `/gold` (Datos agregados)

> ⚠️ **IMPORTANTE:** Al crear cada directorio, añadir un archivo (cualquier .txt) para que no se borre automáticamente.

![Estructura de carpetas - imagen3](imagen3.png)

### 1.4 Carga de Datos Inicial (Capa Bronze)

Dentro de la carpeta `bronze`, crear dos subcarpetas: `crm` y `erp`. Subir los archivos CSV correspondientes a cada sistema.

**Carpeta `/bronze/crm/`:**
- `cust_info.csv`
- `prd_info.csv`
- `sales_details.csv`

**Carpeta `/bronze/erp/`:**
- `CUST_AZ12.csv`
- `LOC_A101.csv`
- `PX_CAT_G1V2.csv`

**Carpetas vacías a crear:**
- `/silver/crm/`
- `/silver/erp/`
- `/gold/`

![Archivos en Bronze - imagen4](imagen4.png)

---

## Parte 2: Creación de Azure Data Factory (ADF)

Azure Data Factory orquestará el movimiento y transformación de los datos.

### 2.1 Despliegue del Recurso

1. Buscar **"Data Factory"** en el marketplace
2. **Nombre:** (el que desees)
3. **Versión:** V2
4. **Configuración Git:** Configurar más tarde

![Crear Data Factory - imagen5](imagen5.png)
![Configuración Data Factory - imagen6](imagen6.png)

### 2.2 Asignación de Permisos (IAM)

Para que ADF pueda acceder al Data Lake sin usar claves de acceso (Access Keys), usaremos la **Identidad Administrada**.

**Pasos:**
1. Ir al recurso **Storage Account** (el nombre que le pusiste)
2. Menú **Control de acceso (IAM)** → **Agregar asignación de roles**
3. Seleccionar el rol: **Storage Blob Data Contributor** (Colaborador de datos de blobs de almacenamiento)
4. **Asignar acceso a:** Managed Identity → Seleccionar tu Data Factory
5. **Nota:** Si estás depurando con tu usuario, asegúrate de agregarte a ti mismo también con este rol

![IAM Storage - imagen7](imagen7.png)
![Asignar rol - imagen8](imagen8.png)
![Seleccionar Data Factory - imagen9](imagen9.png)
![Confirmación rol - imagen10](imagen10.png)

### 2.3 Creación del Servicio Vinculado (Linked Service)

En **Azure Data Factory Studio:**

1. Ir a la pestaña **Manage** (Administrar)
2. Crear **New Linked Service** → **Azure Data Lake Storage Gen2**
3. **Método de autenticación:** Managed Identity (recomendado)
4. Probar conexión

![Linked Service - imagen11](imagen11.png)

---

## Parte 3: Pipeline 1 - Ingesta (Copy Data)

Este pipeline moverá los datos de Bronze a Silver, cambiando el formato de CSV a Parquet (o manteniendo CSV según se requiera).

### 3.1 Datasets

Crear los datasets necesarios:
- **Source:** DelimitedText (CSV) apuntando a `bronze/{carpeta}/{archivo}.csv`
- **Sink:** Parquet (o CSV) apuntando a `silver/{carpeta}/`

![Datasets - imagen12](imagen12.png)
![Dataset Source - imagen13](imagen13.png)
![Dataset Sink - imagen14](imagen14.png)

### 3.2 Actividad de Copia

1. Crear un nuevo **Pipeline**
2. Arrastrar la actividad **Copy Data**
3. **Source:** Seleccionar el dataset de origen (ej. `cust_info`)
4. **Sink:** Seleccionar el dataset de destino en Silver
5. Repetir este proceso para todos los archivos de CRM y ERP

![Pipeline Copy - imagen15](imagen15.png)

### 3.3 Mapeo de Tipos de Datos

Dentro de **Mapping** (Asignación), modificar el tipo de datos a los que consideremos necesarios cambiar.

![Mapping tipos - imagen16](imagen16.png)

**Repetir este proceso con cada CSV** que haya en las carpetas de bronze, desencadenar el pipeline y comprobar que se han creado los datos en Silver.

![Ejecución Pipeline - imagen17](imagen17.png)

---

## Parte 4: Pipeline 2 - Transformación (Data Flows)

Usaremos **Data Flows** para limpiar, unir y transformar los datos hacia la capa Gold (Modelo Estrella).

### 📊 Esquemas de Datos Gold

#### `gold.dim_customers`

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| customer_key | INT | Surrogate key que identifica de forma única cada cliente en la dimensión |
| customer_id | INT | Identificador numérico único asignado a cada cliente |
| customer_number | NVARCHAR(50) | Identificador alfanumérico usado para rastreo y referencia del cliente |
| first_name | NVARCHAR(50) | Nombre del cliente |
| last_name | NVARCHAR(50) | Apellido o nombre de familia del cliente |
| country | NVARCHAR(50) | País de residencia del cliente (ej. 'Australia') |
| marital_status | NVARCHAR(50) | Estado civil del cliente (ej. 'Married', 'Single') |
| gender | NVARCHAR(50) | Género del cliente (ej. 'Male', 'Female', 'n/a') |
| birthdate | DATE | Fecha de nacimiento en formato YYYY-MM-DD |
| create_date | DATE | Fecha en que se creó el registro del cliente en el sistema |

#### `gold.dim_products`

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| product_key | INT | Surrogate key que identifica de forma única cada producto en la dimensión |
| product_id | INT | Identificador único asignado al producto para rastreo interno |
| product_number | NVARCHAR(50) | Código alfanumérico estructurado para categorización o inventario |
| product_name | NVARCHAR(50) | Nombre descriptivo del producto (tipo, color, tamaño) |
| category_id | NVARCHAR(50) | Identificador único de la categoría del producto |
| category | NVARCHAR(50) | Clasificación general del producto (ej. Bikes, Components) |
| subcategory | NVARCHAR(50) | Clasificación más detallada dentro de la categoría |
| maintenance_required | NVARCHAR(50) | Indica si el producto requiere mantenimiento ('Yes', 'No') |
| cost | INT | Precio base del producto en unidades monetarias |
| product_line | NVARCHAR(50) | Línea o serie específica del producto (ej. Road, Mountain) |
| start_date | DATE | Fecha en que el producto estuvo disponible para venta o uso |

#### `gold.fact_sales`

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| order_number | NVARCHAR(50) | Identificador alfanumérico único de cada orden de venta (ej. 'SO54496') |
| product_key | INT | Surrogate key que enlaza la orden con la dimensión de productos |
| customer_key | INT | Surrogate key que enlaza la orden con la dimensión de clientes |
| order_date | DATE | Fecha en que se realizó la orden |
| shipping_date | DATE | Fecha en que se envió el pedido al cliente |
| due_date | DATE | Fecha de vencimiento del pago de la orden |
| sales_amount | INT | Valor monetario total de la venta por línea de pedido |
| quantity | INT | Número de unidades del producto en la orden |
| price | INT | Precio por unidad del producto en la orden |

### 4.1 Dataflow: Fact Sales (Tabla de Hechos)

1. **Source:** `sales_details` (desde Silver)
2. **Derived Column:** Formatear columnas y tipos de datos
3. **Select:** Renombrar columnas (como se muestra en la tabla de `fact_sales`)
4. **Sink:** Guardar en `gold/` como `fact_sales.parquet` (o .csv si se prefiere para Power BI Web)

![Dataflow Fact Sales - imagen18](imagen18.png)

### 4.2 Dataflow: Dim Products

1. **Sources:** `PX_CAT_G1V2` y `prd_info` (desde Silver)
2. **Filter:** Eliminar filas nulas `(!isNull(prd_cost))`
3. **Join:** Unir por ID de producto. Usar expresiones como `replace(substring(...))` si los IDs no coinciden exactamente
4. **Sink:** Guardar en `gold/` como `dim_products.parquet`

![Dataflow Dim Products - imagen19](imagen19.png)
![Join Products - imagen20](imagen20.png)

### 4.3 Dataflow: Dim Customers

1. **Sources:** `cust_info`, `CUST_AZ12`, `LOC_A101`
2. **Join & Union:** Combinar información de clientes del CRM y ERP
3. **Sink:** Guardar en `gold/` como `dim_customers.parquet`

![Dataflow Dim Customers - imagen21](imagen21.png)
![Join Customers - imagen22](imagen22.png)

### 4.4 Ejecución

Crear un **Pipeline maestro** que ejecute estos Data Flows y verificar que en la carpeta `gold` aparezcan los archivos resultantes.

![Pipeline maestro - imagen23](imagen23.png)

---

## Parte 5: Visualización con Power BI

Conectaremos Power BI a los datos procesados en la capa Gold.

### 5.1 Conexión

1. En **Power BI Desktop**, seleccionar **Obtener Datos** → **Azure Data Lake Storage Gen2** (o Web si usas la URL del blob)
2. Ingresar la URL del archivo en Gold
3. Autenticarse con cuenta organizacional

![Power BI conexión - imagen24](imagen24.png)

---

## Parte 6: Azure Machine Learning (Extra)

Configuración de un entorno de ML para acceder a los datos del Warehouse.

### 6.1 Creación del Workspace

1. Crear recurso **Azure Machine Learning**
2. Asignar al mismo grupo de recursos `warehouse`
3. Crear una **instancia de proceso** (Compute Instance) para ejecutar Notebooks

![Azure ML - imagen25](imagen25.png)

### 6.2 Acceso a Datos mediante Python

Para acceder al Data Lake desde un Notebook de ML:

1. Generar un **SAS Token** (Shared Access Signature) en el contenedor `datalake` desde el portal de Azure (permisos de Lectura y Listado)
2. Usar el siguiente código Python en el Notebook:

```python
from azure.storage.blob import BlobServiceClient

account_url = "https://<NOMBRE_CUENTA>.blob.core.windows.net"
sas_token = "<TU_SAS_TOKEN>"
service = BlobServiceClient(account_url=account_url, credential=sas_token)
container_client = service.get_container_client("datalake")

print("Listado de archivos en el Data Lake:")
for blob in container_client.list_blobs():
    print(blob.name)
```

![Notebook Python - imagen26](imagen26.png)

---

## 🎯 Resumen del Proceso

1. **Bronze Layer:** Datos crudos desde sistemas fuente (CRM, ERP)
2. **Silver Layer:** Datos limpios y en formato optimizado (Parquet)
3. **Gold Layer:** Modelo dimensional (Star Schema) listo para análisis
4. **Visualización:** Power BI conectado a la capa Gold
5. **ML (Opcional):** Azure ML para modelos predictivos

---

## 📚 Recursos Adicionales

- [Documentación Azure Data Lake Storage](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-introduction)
- [Documentación Azure Data Factory](https://docs.microsoft.com/azure/data-factory/)
- [Data Flows en ADF](https://docs.microsoft.com/azure/data-factory/concepts-data-flow-overview)
- [Power BI con Azure](https://docs.microsoft.com/power-bi/connect-data/service-azure-and-power-bi)

---

## ⚠️ Notas Importantes

- Siempre usar **Managed Identity** para la autenticación entre servicios Azure (más seguro)
- La arquitectura **Medallion** (Bronze → Silver → Gold) es una best practice en Data Lakes
- Usar **Parquet** en lugar de CSV mejora el rendimiento y reduce costos de almacenamiento
- Configurar correctamente los permisos **IAM** es crucial para evitar errores de acceso

---

## 📧 Soporte

Para dudas sobre la práctica, consultar con el profesor o revisar la documentación oficial de Azure.