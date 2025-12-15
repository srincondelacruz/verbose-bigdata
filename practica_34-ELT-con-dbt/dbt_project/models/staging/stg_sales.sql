with source as (
    select * from {{ source('walmart_source', 'raw_ventas') }}
),

renamed as (
    select
        -- Identificadores (Casteo a entero para evitar errores de join)
        cast("Store" as integer) as tienda_id,
        
        -- FECHAS: Postgres espera YYYY-MM-DD. Tu CSV trae DD-MM-YYYY.
        -- Usamos to_date para arreglarlo de forma segura.
        to_date("Date", 'DD-MM-YYYY') as fecha_venta,
        
        -- MÉTRICAS: Aseguramos que sean numéricas para poder sumar después
        cast("Weekly_Sales" as numeric) as venta_semanal,
        
        -- BANDERAS: Convertimos 1/0 a Booleano (True/False) que es más profesional
        case 
            when "Holiday_Flag" = 1 then true 
            else false 
        end as es_semana_festiva,
        
        -- DIMENSIONES DE ENTORNO
        cast("Temperature" as numeric) as temperatura,
        cast("Fuel_Price" as numeric) as precio_combustible,
        cast("CPI" as numeric) as indice_cpi,
        cast("Unemployment" as numeric) as tasa_desempleo

    from source
)

select * from renamed