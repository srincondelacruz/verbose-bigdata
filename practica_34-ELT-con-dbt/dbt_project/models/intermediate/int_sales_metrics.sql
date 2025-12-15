with stg_sales as (
    select * from {{ ref('stg_sales') }}
),

con_logica_negocio as (
    select
        *,
        -- KPI 1: Clasificación de la semana según volumen de venta
        case
            when venta_semanal > 1500000 then 'Rendimiento Alto'
            when venta_semanal > 750000 then 'Rendimiento Medio'
            else 'Rendimiento Bajo'
        end as categoria_rendimiento,

        -- KPI 2: Impacto estimado del combustible (ejemplo de lógica calculada)
        -- Si el combustible es caro (>3.5) y venta es baja, marcamos alerta
        case
            when precio_combustible > 3.5 and venta_semanal < 500000 then true
            else false
        end as alerta_impacto_combustible

    from stg_sales
)

select * from con_logica_negocio