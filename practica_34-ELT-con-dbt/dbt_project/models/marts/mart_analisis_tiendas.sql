with ventas_enriquecidas as (
    select * from {{ ref('int_sales_metrics') }}
)

select
    tienda_id,
    
    -- Métricas Transaccionales (Lo que le importa al negocio)
    sum(venta_semanal) as ingresos_totales_historicos,
    avg(venta_semanal) as venta_promedio_semanal,
    max(venta_semanal) as record_venta_semanal,
    
    -- Análisis de Contexto (Promedios de indicadores económicos)
    round(avg(temperatura), 2) as temperatura_promedio,
    round(avg(indice_cpi), 2) as cpi_promedio,
    round(avg(tasa_desempleo), 2) as desempleo_promedio,
    
    -- Segmentación (Conteo de semanas buenas vs malas)
    count(case when categoria_rendimiento = 'Rendimiento Alto' then 1 end) as semanas_rendimiento_alto

from ventas_enriquecidas
group by tienda_id
order by ingresos_totales_historicos desc