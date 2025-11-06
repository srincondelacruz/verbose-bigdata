# main.py - Programa principal modular
# Orquesta todos los módulos del sistema de calificaciones

from sistema_calificaciones import datos
from sistema_calificaciones import validacion
from sistema_calificaciones import estadisticas
from sistema_calificaciones import analisis_estudiantes
from sistema_calificaciones import reportes
from sistema_calificaciones import rangos


def main():
    """Función principal que ejecuta el sistema de calificaciones."""
    
    # Encabezado principal
    reportes.imprimir_encabezado("SISTEMA MODULAR DE CALIFICACIONES")
    
    # Obtener datos
    estudiantes = datos.estudiantes
    calificaciones = datos.calificaciones
    
    # Validar datos
    es_valido, mensaje = validacion.validar_datos(estudiantes, calificaciones)
    validacion.mostrar_validacion(es_valido, mensaje)
    
    # Mostrar datos iniciales
    reportes.mostrar_datos_iniciales(estudiantes, calificaciones)
    
    # Realizar análisis estadístico
    reportes.imprimir_encabezado("ANÁLISIS ESTADÍSTICO")
    stats = estadisticas.mostrar_estadisticas(calificaciones)
    
    # Análisis de estudiantes
    reportes.imprimir_encabezado("ANÁLISIS DE ESTUDIANTES")
    analisis = analisis_estudiantes.mostrar_analisis_estudiantes(estudiantes, calificaciones)
    
    # Mostrar reporte completo
    reportes.imprimir_encabezado("REPORTE COMPLETO")
    reportes.mostrar_reporte_completo(stats, analisis)
    
    # Mostrar reporte individual
    reportes.imprimir_encabezado("REPORTE INDIVIDUAL")
    reportes.mostrar_reporte_individual(estudiantes, calificaciones, stats['promedio'])
    
    # Análisis adicional por rangos
    reportes.imprimir_encabezado("ANÁLISIS ADICIONAL")
    rangos.mostrar_estudiantes_por_rangos(estudiantes, calificaciones)
    
    # Información del paradigma
    reportes.imprimir_encabezado("INFORMACIÓN DEL PARADIGMA")
    reportes.mostrar_info_paradigma()
    
    # Finalización
    reportes.imprimir_encabezado("Procesamiento completado exitosamente")
    reportes.mostrar_estadisticas_procesamiento()


if __name__ == "__main__":
    main()

