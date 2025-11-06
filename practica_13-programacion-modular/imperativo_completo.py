# imperativo_completo.py - Paradigma Imperativo
# Programa completo que procesa calificaciones usando programación imperativa

# Variables globales para almacenar todos los datos
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofia"]
calificaciones = [85, 92, 78, 96, 88]

# Variables para cálculos estadísticos
suma_total = 0
promedio = 0
mediana = 0
rango = 0

# Variables para conteo de estudiantes
aprobados = 0
reprobados = 0
total_estudiantes = 0

# Variables para mejores y peores estudiantes
mejor_estudiante = ""
mejor_nota = 0
peor_estudiante = ""
peor_nota = 0
nota_maxima = 0
nota_minima = 0

# Variables para formateo y presentación
separador_largo = "=" * 60
separador_corto = "-" * 40
porcentaje_aprobados = 0

print(separador_largo)
print("   SISTEMA IMPERATIVO DE CALIFICACIONES")
print(separador_largo)

# Validación manual de datos
print("Validando datos de entrada...")
datos_validos = True
mensaje_error = ""

if len(estudiantes) == 0:
    datos_validos = False
    mensaje_error = "La lista de estudiantes está vacía"
elif len(calificaciones) == 0:
    datos_validos = False
    mensaje_error = "La lista de calificaciones está vacía"
elif len(estudiantes) != len(calificaciones):
    datos_validos = False
    mensaje_error = "Las listas deben tener la misma longitud"
else:
    # Validar cada calificación
    for i in range(len(calificaciones)):
        if calificaciones[i] < 0 or calificaciones[i] > 100:
            datos_validos = False
            mensaje_error = f"La calificación {calificaciones[i]} está fuera del rango válido (0-100)"
            break

if datos_validos:
    print("Resultado: Datos válidos")
else:
    print(f"ERROR: {mensaje_error}")
    print("No se pueden procesar datos inválidos")
    exit()

print(separador_corto)

# Mostrar datos iniciales
print("DATOS INICIALES:")
for i in range(len(estudiantes)):
    print(f"  {estudiantes[i]}: {calificaciones[i]}")

# === CÁLCULOS ESTADÍSTICOS ===
print(f"\n{separador_largo}")
print("   ANÁLISIS ESTADÍSTICO")
print(separador_largo)

# Calcular suma total paso a paso
print("Calculando suma total...")
suma_total = 0
for i in range(len(calificaciones)):
    suma_total = suma_total + calificaciones[i]
    print(f"  Sumando {calificaciones[i]}: total parcial = {suma_total}")

print(f"Suma total de calificaciones: {suma_total}")

# Calcular promedio
total_estudiantes = len(calificaciones)
promedio = suma_total / total_estudiantes
print(f"Promedio general: {promedio:.2f}")

# Calcular mediana (ordenamiento manual)
print("Calculando mediana...")
calificaciones_ordenadas = []
for nota in calificaciones:
    calificaciones_ordenadas.append(nota)

# Ordenamiento burbuja manual
for i in range(len(calificaciones_ordenadas)):
    for j in range(0, len(calificaciones_ordenadas) - 1 - i):
        if calificaciones_ordenadas[j] > calificaciones_ordenadas[j + 1]:
            # Intercambiar
            temp = calificaciones_ordenadas[j]
            calificaciones_ordenadas[j] = calificaciones_ordenadas[j + 1]
            calificaciones_ordenadas[j + 1] = temp

print(f"Calificaciones ordenadas: {calificaciones_ordenadas}")

# Calcular mediana según si es par o impar
n = len(calificaciones_ordenadas)
if n % 2 == 0:
    mediana = (calificaciones_ordenadas[n//2 - 1] + calificaciones_ordenadas[n//2]) / 2
else:
    mediana = calificaciones_ordenadas[n//2]

print(f"Mediana: {mediana}")

# Calcular rango (diferencia entre máximo y mínimo)
nota_maxima = calificaciones[0]
nota_minima = calificaciones[0]

for i in range(1, len(calificaciones)):
    if calificaciones[i] > nota_maxima:
        nota_maxima = calificaciones[i]
    if calificaciones[i] < nota_minima:
        nota_minima = calificaciones[i]

rango = nota_maxima - nota_minima
print(f"Rango (max - min): {rango}")

# === ANÁLISIS DE ESTUDIANTES ===
print(f"\n{separador_largo}")
print("   ANÁLISIS DE ESTUDIANTES")
print(separador_largo)

# Contar aprobados y reprobados paso a paso
print("Contando aprobados y reprobados...")
aprobados = 0
reprobados = 0

for i in range(len(calificaciones)):
    if calificaciones[i] >= 80:
        aprobados = aprobados + 1
        print(f"  {estudiantes[i]} APROBÓ con {calificaciones[i]}")
    else:
        reprobados = reprobados + 1
        print(f"  {estudiantes[i]} REPROBÓ con {calificaciones[i]}")

print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")

# Encontrar mejor y peor estudiante paso a paso
print("\nBuscando mejor y peor estudiante...")
mejor_nota = calificaciones[0]
peor_nota = calificaciones[0]
mejor_estudiante = estudiantes[0]
peor_estudiante = estudiantes[0]

for i in range(1, len(calificaciones)):
    if calificaciones[i] > mejor_nota:
        mejor_nota = calificaciones[i]
        mejor_estudiante = estudiantes[i]
        print(f"  Nuevo mejor: {mejor_estudiante} ({mejor_nota})")
    
    if calificaciones[i] < peor_nota:
        peor_nota = calificaciones[i]
        peor_estudiante = estudiantes[i]
        print(f"  Nuevo peor: {peor_estudiante} ({peor_nota})")

print(f"Mejor rendimiento: {mejor_estudiante} ({mejor_nota})")
print(f"Menor rendimiento: {peor_estudiante} ({peor_nota})")

# Calcular porcentaje de aprobados
porcentaje_aprobados = (aprobados / total_estudiantes) * 100

# Crear resumen del estado
resumen = ""
if aprobados > reprobados:
    resumen = f"Buen rendimiento general: {porcentaje_aprobados:.1f}% de aprobación"
elif reprobados > aprobados:
    resumen = f"Rendimiento preocupante: solo {porcentaje_aprobados:.1f}% de aprobación"
else:
    resumen = f"Rendimiento equilibrado: {porcentaje_aprobados:.1f}% de aprobación"

print(f"\nResumen: {resumen}")

# === REPORTE COMPLETO ===
print(f"\n{separador_largo}")
print("   REPORTE COMPLETO")
print(separador_largo)

print("=== REPORTE COMPLETO ===")
print(f"Total estudiantes: {total_estudiantes}")
print(f"Suma total: {suma_total}")
print(f"Promedio general: {promedio:.2f}")
print(f"Aprobados: {aprobados} ({porcentaje_aprobados:.1f}%)")
print(f"Reprobados: {reprobados}")
print("")
print("=== EXTREMOS ===")
print(f"Mejor estudiante: {mejor_estudiante} ({mejor_nota})")
print(f"Peor estudiante: {peor_estudiante} ({peor_nota})")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

# === REPORTE INDIVIDUAL POR ESTUDIANTE ===
print(f"\n{separador_largo}")
print("   REPORTE INDIVIDUAL")
print(separador_largo)

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

# === INFORMACIÓN ADICIONAL ===
print(f"\n{separador_largo}")
print("   ANÁLISIS ADICIONAL")
print(separador_largo)

# Buscar estudiantes en rangos específicos
print("Estudiantes por rangos de calificación:")

# Rango excelente (90-100)
excelentes = 0
print("Excelente (90-100):")
for i in range(len(estudiantes)):
    if 90 <= calificaciones[i] <= 100:
        excelentes = excelentes + 1
        print(f"  {estudiantes[i]}: {calificaciones[i]}")
if excelentes == 0:
    print("  Ninguno")

# Rango bueno (80-89)
buenos = 0
print("Bueno (80-89):")
for i in range(len(estudiantes)):
    if 80 <= calificaciones[i] <= 89:
        buenos = buenos + 1
        print(f"  {estudiantes[i]}: {calificaciones[i]}")
if buenos == 0:
    print("  Ninguno")

# Rango regular (70-79)
regulares = 0
print("Regular (70-79):")
for i in range(len(estudiantes)):
    if 70 <= calificaciones[i] <= 79:
        regulares = regulares + 1
        print(f"  {estudiantes[i]}: {calificaciones[i]}")
if regulares == 0:
    print("  Ninguno")

# Rango deficiente (0-69)
deficientes = 0
print("Deficiente (0-69):")
for i in range(len(estudiantes)):
    if 0 <= calificaciones[i] <= 69:
        deficientes = deficientes + 1
        print(f"  {estudiantes[i]}: {calificaciones[i]}")
if deficientes == 0:
    print("  Ninguno")

# === INFORMACIÓN DEL PARADIGMA ===
print(f"\n{separador_largo}")
print("   INFORMACIÓN DEL PARADIGMA")
print(separador_largo)

print("Paradigma imperativo utilizado:")
print("  ✓ Código secuencial paso a paso")
print("  ✓ Variables globales para almacenar estado")
print("  ✓ Bucles explícitos para procesamiento")
print("  ✓ Lógica procedural sin funciones")
print("  ✓ Modificación directa de variables")
print("  ✓ Todo el código en un solo archivo")

print(f"\n{separador_largo}")
print("   Procesamiento completado exitosamente")
print(separador_largo)

# Mostrar estadísticas finales del procesamiento
print("\nEstadísticas del procesamiento:")
print(f"  Variables utilizadas: aproximadamente 20")
print(f"  Líneas de código ejecutadas: todas secuencialmente")
print(f"  Bucles realizados: múltiples for loops")
print(f"  Operaciones matemáticas: suma, división, comparaciones")
print(f"  Paradigma: Imperativo puro")

