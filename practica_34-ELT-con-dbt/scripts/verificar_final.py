import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURACIÓN---
DB_USER = "admin"
DB_PASS = "admin"
DB_NAME = "ventas_db"
DB_HOST = "localhost"
DB_PORT = "5434"

def verificar_resultados():
    print("🕵️‍♂️ --- VERIFICANDO RESULTADOS FINALES ---")
    
    # 1. Conectar
    url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    try:
        engine = create_engine(url)
        connection = engine.connect()
    except Exception as e:
        print("❌ Error conectando: ", e)
        return

    # 2. Buscar la tabla correcta
    # dbt crea esquemas tipo: "dbt_tu_nombre_marts".
    # Vamos a intentar leer de ahí. Si cambiaste el nombre del esquema en el init,
    # el script podría fallar, pero te mostrará qué tablas existen para ayudarte.
    
    print("📊 Buscando tabla 'mart_analisis_tiendas'...")
    
    # Consulta para obtener el Top 5 Tiendas con mayores ventas
    # NOTA: Ajusta 'dbt_tu_nombre_marts' si pusiste otro nombre de esquema en dbt init
    # Si dejaste el default, probablemente sea algo como 'dbt_postgres_marts' o 'dbt_tu_nombre_marts'
    
    # Truco: Leemos primero todas las tablas para ver dónde cayó
    tablas = pd.read_sql("SELECT table_schema, table_name FROM information_schema.tables WHERE table_name = 'mart_analisis_tiendas'", connection)
    
    if len(tablas) == 0:
        print("⚠️ No encuentro la tabla. ¿Hiciste 'dbt build'?")
        print("Tablas disponibles en tu base de datos:")
        todas = pd.read_sql("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema LIKE 'dbt%%'", connection)
        print(todas)
        return
    
    # Cogemos el esquema correcto automáticamente
    esquema_real = tablas.iloc[0]['table_schema']
    tabla_real = tablas.iloc[0]['table_name']
    
    print(f"✅ Tabla encontrada: {esquema_real}.{tabla_real}")
    print("\n🏆 --- TOP 5 TIENDAS POR INGRESOS ---")
    
    query = f"""
    SELECT 
        tienda_id, 
        ingresos_totales_historicos, 
        venta_promedio_semanal, 
        semanas_rendimiento_alto 
    FROM {esquema_real}.{tabla_real}
    ORDER BY ingresos_totales_historicos DESC
    LIMIT 5
    """
    
    df_top = pd.read_sql(query, connection)
    
    # Formatear dinero para que se vea bonito
    pd.options.display.float_format = '${:,.2f}'.format
    print(df_top.to_string(index=False))
    
    connection.close()

if __name__ == "__main__":
    verificar_resultados()