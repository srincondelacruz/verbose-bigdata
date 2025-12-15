import pandas as pd
from sqlalchemy import create_engine
import sys

# --- CONFIGURACIÓN NUEVA (PUERTO 5434) ---
DB_USER = "admin"
DB_PASS = "admin"
DB_NAME = "ventas_db"
DB_HOST = "localhost"
DB_PORT = "5434"      # <--- ¡IMPORTANTE! 5434

def cargar_datos():
    print(f"🚀 --- INICIANDO CARGA (PUERTO {DB_PORT}) ---")
    
    # 1. LEER CSV
    archivo_csv = 'data/ventas_walmart.csv'
    print(f"1. Leyendo {archivo_csv}...")
    try:
        df = pd.read_csv(archivo_csv)
        print(f"   -> Encontradas {len(df)} filas.")
    except:
        try:
            df = pd.read_csv(f'../{archivo_csv}')
            print(f"   -> Encontradas {len(df)} filas.")
        except:
            print(f"❌ ERROR: No encuentro el archivo CSV.")
            return

    # 2. CONECTAR
    print(f"2. Conectando a Docker (Puerto {DB_PORT}, Usuario '{DB_USER}')...")
    url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    try:
        engine = create_engine(url)
        connection = engine.connect()
        print("   ✅ ¡CONEXIÓN EXITOSA! (La puerta se abrió)")
        
        print("3. Guardando datos...")
        df.to_sql('raw_ventas', engine, if_exists='replace', index=False)
        print("🎉 ¡ÉXITO TOTAL! Datos cargados en 'raw_ventas'.")
        connection.close()
        
    except Exception as e:
        print("\n❌ FALLÓ LA CONEXIÓN.")
        print(f"EL ERROR TÉCNICO ES: {repr(e)}")

if __name__ == "__main__":
    cargar_datos()