# reportes.py - Módulo de generación de reportes
# Funciones para generar y mostrar reportes

def imprimir_encabezado(titulo):
    """Imprime un encabezado con formato."""
    separador = "=" * 60
    print(f"\n{separador}")
    print(f"   {titulo}")
    print(separador)


def imprimir_separador_corto():
    """Imprime un separador corto."""
    print("-" * 40)


def mostrar_datos_iniciales(estudiantes, calificaciones):
    """Muestra los datos iniciales de estudiantes y calificaciones."""
    imprimir_separador_corto()
    print("DATOS INICIALES:")
    for i in range(len(estudiantes)):
        print(f"  {estudiantes[i]}: {calificaciones[i]}")


def mostrar_reporte_completo(estadisticas, analisis):
    """
    Muestra el reporte completo con todas las estadísticas.
    
    Args:
        estadisticas: Diccionario con estadísticas calculadas
        analisis: Diccionario con análisis de estudiantes
    """
    print("=== REPORTE COMPLETO ===")
    print(f"Total estudiantes: {analisis['total_estudiantes']}")
    print(f"Suma total: {estadisticas['suma_total']}")
    print(f"Promedio general: {estadisticas['promedio']:.2f}")
    print(f"Aprobados: {analisis['aprobados']} ({analisis['porcentaje_aprobados']:.1f}%)")
    print(f"Reprobados: {analisis['reprobados']}")
    print("")
    print("=== EXTREMOS ===")
    print(f"Mejor estudiante: {analisis['mejor_estudiante']} ({analisis['mejor_nota']})")
    print(f"Peor estudiante: {analisis['peor_estudiante']} ({analisis['peor_nota']})")
    print(f"Nota más alta: {estadisticas['nota_maxima']}")
    print(f"Nota más baja: {estadisticas['nota_minima']}")


def mostrar_reporte_individual(estudiantes, calificaciones, promedio):
    """
    Muestra el análisis individual de cada estudiante.
    
    Args:
        estudiantes: Lista de nombres de estudiantes
        calificaciones: Lista de calificaciones
        promedio: Promedio general de calificaciones
    """
    print("Análisis individual por estudiante:")
    for i in range(len(estudiantes)):
        diferencia_promedio = calificaciones[i] - promedio
        estado = "APROBADO" if calificaciones[i] >= 80 else "REPROBADO"
        
        if diferencia_promedio > 0:
            comparacion = f"(+{diferencia_promedio:.1f} sobre el promedio)"
        elif diferencia_promedio < 0:
            comparacion = f"({diferencia_promedio:.1f} bajo el promedio)"
        else:
            comparacion = "(igual al promedio)"
        
        print(f"  {estudiantes[i]}: {calificaciones[i]} - {estado} {comparacion}")


def mostrar_info_paradigma():
    """Muestra información sobre el paradigma modular utilizado."""
    print("Paradigma modular utilizado:")
    print("  ✓ Código organizado en módulos especializados")
    print("  ✓ Funciones reutilizables y mantenibles")
    print("  ✓ Separación de responsabilidades")
    print("  ✓ Importación de módulos según necesidad")
    print("  ✓ Facilita testing y depuración")
    print("  ✓ Código más legible y escalable")


def mostrar_estadisticas_procesamiento():
    """Muestra estadísticas del procesamiento."""
    print("\nEstadísticas del procesamiento:")
    print(f"  Módulos utilizados: 6")
    print(f"  Funciones definidas: múltiples funciones especializadas")
    print(f"  Arquitectura: Modular y orientada a funciones")
    print(f"  Ventajas: Reutilización, mantenibilidad, escalabilidad")
    print(f"  Paradigma: Modular con programación funcional")

