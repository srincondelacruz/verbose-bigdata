# Pipeline de Datos con MongoDB, Azure Cosmos DB, Databricks y Azure AI Foundry

Este documento describe el proceso completo para configurar un pipeline de datos desde MongoDB local hasta Azure AI Foundry, pasando por Cosmos DB y Databricks.

## 1. Preparar MongoDB Local

### Instalación de MongoDB

1. Descargar e instalar MongoDB desde [este enlace](https://www.mongodb.com/try/download/community)

![Descarga MongoDB](foto1.png)

2. Ejecutar el instalador con las siguientes configuraciones:
   - Elegir la opción "Complete"
   - **NO** marcar la casilla de "Install Mongo as a service"
   - Dejar marcada la casilla para instalar Compass automáticamente

![Opciones instalación 1](foto2.png)
![Opciones instalación 2](foto3.png)
![Opciones instalación 3](foto4.png)

### Configuración de Variables de Entorno

3. Verificar la instalación ejecutando en CMD:
```bash
mongod.exe --version
```

![Error comando no reconocido](foto5.png)

4. Añadir MongoDB al PATH de Windows:
   - Copiar la ruta de instalación (por defecto en C:) hasta la carpeta "bin"

![Ruta MongoDB](foto6.png)

5. Añadir la ruta al PATH del sistema:

![Configurar PATH](foto7.png)

6. Verificar que ahora funciona el comando:

![Comando funcionando](foto8.png)

### Preparación de Directorios

7. Crear estructura de carpetas para los datos:
   - Crear carpeta `C:\data`
   - Crear subcarpeta `C:\data\db`

![Estructura carpetas](foto9.png)

### Instalación de MongoDB Shell

8. Descargar [MongoDB Shell](https://www.mongodb.com/try/download/shell)

![Descarga Shell](foto10.png)

9. Extraer y guardar en la misma ruta que MongoDB Server

![Ubicación Shell](foto11.png)

10. Añadir la carpeta bin del Shell al PATH

### Instalación de Database Tools

11. Descargar [Database Tools](https://www.mongodb.com/try/download/database-tools)

![Descarga Database Tools](foto12.png)

12. Extraer y añadir al PATH

![Ruta Database Tools](foto13.png)

### Iniciar MongoDB

13. Abrir CMD y ejecutar:
```bash
mongod
```

14. En otra ventana de CMD, ejecutar:
```bash
mongosh
```

![MongoDB Shell conectado](foto14.png)

15. Verificar bases de datos con:
```bash
show dbs
```

![Bases de datos por defecto](foto15.png)

### Usar MongoDB Compass

16. Abrir Compass y conectar usando la URL por defecto

![Compass conexión](foto16.png)
![Compass conectado](foto17.png)

### Importar Datos

17. Crear nueva base de datos y colección desde Compass

![Crear base de datos](foto18.png)

18. Importar CSV o JSON

![Colección vacía](foto19.png)
![Importar datos](foto20.png)
![Datos importados](foto21.png)

**Nota:** Revisar los tipos de datos detectados automáticamente para evitar problemas posteriores.

## 2. Migrar a Azure Cosmos DB (API MongoDB)

### Crear Recurso en Azure

1. En el portal de Azure, crear un recurso de Cosmos DB para MongoDB

![Crear Cosmos DB](foto22.png)

2. Seleccionar la opción recomendada y activar el **free tier**

### Exportar Datos de MongoDB Local

3. Ejecutar en CMD para crear backup:
```bash
mongodump
```

![Mongodump](foto23.png)

### Importar a Cosmos DB

4. Obtener la cadena de conexión Self desde el portal de Azure (sección "Connection Strings")

5. Ejecutar el comando de restauración (todo en una línea):
```bash
mongorestore --uri "mongodb+srv://usuario:contraseña@clusteragg.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000" ./dump
```

![Mongorestore](foto24.png)

### Verificar Migración

6. En el portal de Azure, ir a Quick Start y seleccionar Mongo Shell

![Quick Start](foto25.png)

7. Ejecutar comandos de verificación:
```bash
show dbs
use db_prueba
db.collection_prueba.find().pretty()
```

![Verificación datos](foto26.png)

## 3. ETL con Azure Databricks

### Crear Servicio Databricks

1. Crear Azure Databricks en el portal (seleccionar Trial para prueba gratuita)

### Conectar con Cosmos DB

2. En un notebook de Databricks, configurar la conexión:

![Configuración conexión](foto27.png)

3. Verificar que los datos están accesibles:

![Datos accesibles](foto28.png)

### Limpieza de Datos

4. Identificar y corregir errores en los datos:

![Errores en datos](foto29.png)

5. Convertir tipos de datos problemáticos (ej: columna edad)

6. Resultado después de la limpieza:

![Datos limpios](foto30.png)

## 4. Vector DB

### Conversión a Formato Delta

1. Convertir los datos limpios a formato Delta para mejor rendimiento:

![Conversión Delta 1](foto31.png)
![Conversión Delta 2](foto32.png)

2. Verificar que la tabla se guardó correctamente:

![Tabla Delta guardada](foto33.png)

### Generar Embeddings

3. Crear representaciones vectoriales para búsquedas semánticas:

![Configuración embeddings 1](foto34.png)
![Configuración embeddings 2](foto35.png)

### Crear Azure AI Search

4. Crear recurso de AI Search en Azure:

![Crear AI Search](foto36.png)

**Nota:** La integración con AI Search mediante librería de Databricks presenta problemas pendientes de resolver:

![Error librería](foto37.png)

## 5. Integración con Azure AI Foundry

### Crear Recurso AI Foundry

1. Crear un recurso de Azure AI Foundry en el portal

2. Asignar automáticamente los recursos ya creados:
   - Cosmos DB
   - Azure AI Search

![Configuración AI Foundry](foto38.png)

---

## Requisitos Previos

- Windows con permisos de administrador
- Cuenta de Azure con suscripción activa
- Conocimientos básicos de:
  - MongoDB
  - Azure Portal
  - Python/PySpark
  - ETL

## Recursos Adicionales

- [Documentación MongoDB](https://docs.mongodb.com/)
- [Azure Cosmos DB Documentation](https://docs.microsoft.com/azure/cosmos-db/)
- [Azure Databricks Documentation](https://docs.databricks.com/)
- [Azure AI Search Documentation](https://docs.microsoft.com/azure/search/)

## Problemas Conocidos

- La librería para integrar Databricks con Azure AI Search presenta errores de importación
- Algunas funcionalidades requieren verificación adicional de permisos en Azure

## Próximos Pasos

1. Resolver el problema de integración Databricks-AI Search
2. Completar la configuración de embeddings vectoriales
3. Configurar flujos de trabajo en AI Foundry
4. Implementar modelos de IA sobre los datos procesados