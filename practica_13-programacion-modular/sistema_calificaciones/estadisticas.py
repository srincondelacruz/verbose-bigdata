# estadisticas.py - Módulo de cálculos estadísticos
# Funciones para realizar cálculos estadísticos sobre las calificaciones

def calcular_suma(calificaciones):
    """Calcula la suma total de las calificaciones."""
    suma_total = 0
    for calificacion in calificaciones:
        suma_total += calificacion
    return suma_total


def calcular_promedio(calificaciones):
    """Calcula el promedio de las calificaciones."""
    suma_total = calcular_suma(calificaciones)
    return suma_total / len(calificaciones)


def ordenar_burbuja(lista):
    """Ordena una lista usando el algoritmo de ordenamiento burbuja."""
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - 1 - i):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                # Intercambiar
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    return lista_ordenada


def calcular_mediana(calificaciones):
    """Calcula la mediana de las calificaciones."""
    calificaciones_ordenadas = ordenar_burbuja(calificaciones)
    n = len(calificaciones_ordenadas)
    
    if n % 2 == 0:
        mediana = (calificaciones_ordenadas[n//2 - 1] + calificaciones_ordenadas[n//2]) / 2
    else:
        mediana = calificaciones_ordenadas[n//2]
    
    return mediana


def calcular_rango(calificaciones):
    """Calcula el rango (diferencia entre máximo y mínimo)."""
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)
    return nota_maxima - nota_minima


def obtener_maxima(calificaciones):
    """Obtiene la calificación máxima."""
    return max(calificaciones)


def obtener_minima(calificaciones):
    """Obtiene la calificación mínima."""
    return min(calificaciones)


def mostrar_estadisticas(calificaciones):
    """
    Muestra todas las estadísticas de las calificaciones.
    
    Args:
        calificaciones: Lista de calificaciones
    
    Returns:
        dict: Diccionario con todas las estadísticas calculadas
    """
    print("\nCalculando suma total...")
    suma_total = calcular_suma(calificaciones)
    for i, cal in enumerate(calificaciones, 1):
        total_parcial = sum(calificaciones[:i])
        print(f"  Sumando {cal}: total parcial = {total_parcial}")
    
    print(f"Suma total de calificaciones: {suma_total}")
    
    promedio = calcular_promedio(calificaciones)
    print(f"Promedio general: {promedio:.2f}")
    
    print("Calculando mediana...")
    calificaciones_ordenadas = ordenar_burbuja(calificaciones)
    print(f"Calificaciones ordenadas: {calificaciones_ordenadas}")
    
    mediana = calcular_mediana(calificaciones)
    print(f"Mediana: {mediana}")
    
    rango = calcular_rango(calificaciones)
    print(f"Rango (max - min): {rango}")
    
    return {
        "suma_total": suma_total,
        "promedio": promedio,
        "mediana": mediana,
        "rango": rango,
        "nota_maxima": obtener_maxima(calificaciones),
        "nota_minima": obtener_minima(calificaciones)
    }

