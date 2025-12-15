
GUÍA DE INSTALACIÓN Y EJECUCIÓN: PIPELINE ELT WALMART

Esta guía detalla los pasos para desplegar y ejecutar el proyecto desde cero en un entorno local.

================================================================================

PASO 1: REQUISITOS PREVIOS Asegúrate de tener instalado:

Docker Desktop (Debe estar abierto y corriendo).

Python 3.10+

Git

================================================================================

PASO 2: CLONAR EL REPOSITORIO Abre tu terminal y descarga el proyecto:

git clone https://github.com/m0siq/data_engineering_practice.git cd data_engineering_practice

================================================================================

PASO 3: LEVANTAR LA INFRAESTRUCTURA (DOCKER) El proyecto utiliza PostgreSQL en un contenedor. Hemos configurado el puerto 5434 para evitar conflictos.

docker compose up -d

(Verificación: Ejecuta "docker ps". Deberías ver el contenedor activo en el puerto 5434).

================================================================================

PASO 4: CONFIGURAR ENTORNO PYTHON Crea un entorno virtual e instala las dependencias:

En Windows: python -m venv venv 
.\venv\Scripts\activate 
pip install pandas sqlalchemy psycopg2-binary dbt-core dbt-postgres

En Mac/Linux: python3 -m venv venv source venv/bin/activate pip install pandas sqlalchemy psycopg2-binary dbt-core dbt-postgres

================================================================================

PASO 5: CONFIGURAR CONEXIÓN (MÉTODO SIMPLE) Para que dbt sepa conectarse a la base de datos, crearemos el archivo de configuración dentro del proyecto:

Entra en la carpeta "dbt_project".

Crea un archivo nuevo llamado "profiles.yml".

Pega este contenido dentro:

dbt_project: 
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: admin
      password: admin
      port: 5434       
      dbname: ventas_db
      schema: dbt_tunombre
      threads: 1 


================================================================================

PASO 6: FASE 1 - INGESTA (EXTRACT & LOAD) Ejecuta el script para cargar los datos del CSV a PostgreSQL:

python scripts/carga_inicial.py

(Esperado: Mensaje de "ÉXITO TOTAL! Datos cargados en raw_ventas").

================================================================================

PASO 7: FASE 2 - TRANSFORMACIÓN (DBT) Construye los modelos y ejecuta los tests de calidad. IMPORTANTE: Usamos "--profiles-dir ." para decirle que lea el archivo que acabamos de crear.

cd dbt_project
#importante ejecutar con el punto sino no va a ir
dbt build --profiles-dir .

(Esperado: Todos los modelos stg, int, mart en verde).

================================================================================

PASO 8: VISUALIZAR DOCUMENTACIÓN Genera el sitio web con el linaje de datos:
#importante ejecutar con el punto sino no va a ir
dbt docs generate --profiles-dir . 
#importante ejecutar con el punto sino no va a ir
dbt docs serve --port 8001 --profiles-dir .

Abre en tu navegador: http://localhost:8001

================================================================================

PASO 9: VERIFICACIÓN FINAL Si quieres ver los resultados finales (Top 5 Tiendas) en la terminal:

(Abre una nueva terminal si estás ejecutando los docs) python scripts/verificar_final.py

================================================================================

PASO 10: DETENER EL PROYECTO Para apagar la base de datos:

docker compose down
