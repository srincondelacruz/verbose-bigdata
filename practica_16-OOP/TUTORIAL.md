# Parte 2 - Nivel Intermedio

---

## Ejercicio 1: Sistema de Gestión de Empleados

Crea una clase `EmpleadoEmpresa` con las siguientes características:

* **Variables de clase:**
    * `total_empleados = 0`
    * `salario_minimo = 1000`
    * `empresa = "TechCorp"`
* **Atributos de instancia:**
    * `nombre`
    * `edad`
    * `salario`
    * `departamento`
    * `años_experiencia`
* **Métodos:**
    * `__init__()`: Inicializa atributos. Valida que `salario` sea `>=` a `salario_minimo`, si no, asigna `salario_minimo`. Incrementa `total_empleados`.
    * `aumentar_salario(porcentaje)`: Aumenta el salario.
    * `cambiar_departamento(nuevo_depto)`: Cambia el departamento.
    * `cumplir_años()`: Incrementa `edad` y `años_experiencia`.
    * `calcular_salario_anual()`: Retorna salario * 12.
    * `es_senior()`: Retorna `True` si tiene más de 5 años de experiencia.
    * `get_info_completa()`: Retorna un string con toda la información del empleado.
* **Métodos de clase:**
    * `@classmethod empleados_registrados()`: Retorna `total_empleados`.
    * `@classmethod actualizar_salario_minimo(nuevo_minimo)`: Actualiza `salario_minimo`.

**Prueba:** Crea 5 empleados, realiza operaciones y muestra un resumen.

---

## Ejercicio 2: Sistema de Inventario de Tienda

Crea una clase `Articulo` con:

* **Variables de clase:**
    * `contador_articulos = 0`
    * `iva = 0.21`
* **Atributos de instancia:**
    * `codigo` (generado automáticamente: "ART001", "ART002", etc.)
    * `nombre`
    * `precio`
    * `stock`
    * `categoria`
* **Métodos:**
    * `__init__(nombre, precio, stock_inicial, categoria)`: Inicializa y genera `codigo` automático.
    * `vender(cantidad)`: Reduce `stock` si hay suficiente (retorna `True`/`False`).
    * `reabastecer(cantidad)`: Aumenta `stock`.
    * `calcular_valor_inventario()`: Retorna `precio` × `stock`.
    * `calcular_precio_con_iva()`: Retorna `precio` + IVA.
    * `aplicar_descuento(porcentaje)`: Reduce el `precio`.
    * `necesita_reabastecimiento()`: Retorna `True` si `stock < 5`.
    * `obtener_info()`: Retorna string con toda la información.
* **Métodos de clase:**
    * `@classmethod cambiar_iva(nuevo_iva)`
    * `@classmethod total_articulos()`

**Prueba:** Crea 8 artículos, simula ventas y reabastecimientos, y muestra un reporte final.

---

## Ejercicio 3: Gestión de Cursos Universitarios

Crea una clase `Curso` con:

* **Variables de clase:**
    * `total_cursos = 0`
    * `universidad = "Universidad Nacional"`
* **Atributos de instancia:**
    * `nombre_curso`, `codigo_curso`, `creditos`
    * `estudiantes_inscritos` (lista vacía)
    * `capacidad_maxima`
    * `profesor`
* **Métodos:**
    * `__init__()`: Inicializa atributos.
    * `inscribir_estudiante(nombre_estudiante)`: Agrega estudiante si hay cupo (retorna mensaje).
    * `retirar_estudiante(nombre_estudiante)`: Elimina estudiante.
    * `obtener_cantidad_inscritos()`
    * `esta_lleno()`: Retorna `True`/`False`.
    * `obtener_cupos_disponibles()`
    * `listar_estudiantes()`: Muestra la lista numerada.
    * `calcular_porcentaje_ocupacion()`
    * `cambiar_profesor(nuevo_profesor)`
* **Métodos de clase:**
    * `@classmethod total_cursos_activos()`
    * `@classmethod cambiar_universidad(nueva_uni)`

**Prueba:** Crea 4 cursos, inscribe y retira estudiantes, y genera un reporte de ocupación.

---

## Ejercicio 4: Sistema de Cuentas Bancarias con Historial

Crea una clase `CuentaBancaria` con:

* **Variables de clase:**
    * `contador_cuentas = 1000000000`
    * `tasa_interes_mensual = 0.005`
    * `comision_retiro = 2.50`
* **Atributos de instancia:**
    * `numero_cuenta` (generado automáticamente)
    * `titular`, `saldo`
    * `transacciones` (lista de diccionarios: `{tipo, monto, saldo_resultante}`)
* **Métodos:**
    * `__init__(titular, saldo_inicial)`: Inicializa y registra el depósito inicial.
    * `depositar(monto)`: Aumenta saldo y registra.
    * `retirar(monto)`: Reduce saldo (si hay), aplica comisión y registra (retorna `True`/`False`).
    * `transferir(cuenta_destino, monto)`
    * `aplicar_intereses()`: Aplica interés mensual y registra.
    * `mostrar_historial()`
    * `obtener_saldo()`
    * `contar_transacciones()`
    * `calcular_total_depositado()`: Suma depósitos del historial.
* **Métodos de clase:**
    * `@classmethod obtener_total_cuentas()`

**Prueba:** Crea 3 cuentas, realiza operaciones (depósitos, retiros, transferencias) y muestra historiales.

---

## Ejercicio 5: Sistema de Gestión de Proyectos

Crea una clase `Proyecto` con:

* **Variables de clase:**
    * `total_proyectos = 0`
    * `estados_validos = ["Planificación", "En Progreso", "Completado", "Cancelado"]`
* **Atributos de instancia:**
    * `nombre_proyecto`, `fecha_inicio`, `presupuesto`
    * `gastos` (lista de diccionarios: `{concepto: str, monto: float}`)
    * `estado` (inicialmente "Planificación")
    * `miembros_equipo` (lista de nombres)
* **Métodos:**
    * `__init__()`: Inicializa atributos.
    * `registrar_gasto(concepto, monto)`: Agrega gasto si hay presupuesto (retorna `True`/`False`).
    * `calcular_presupuesto_restante()`
    * `calcular_gastos_totales()`
    * `cambiar_estado(nuevo_estado)`: Cambia estado si es válido.
    * `agregar_miembro(nombre)`
    * `remover_miembro(nombre)`
    * `obtener_porcentaje_gastado()`
    * `esta_sobre_presupuesto()`: Retorna `True`/`False`.
    * `obtener_gasto_mayor()`: Retorna el diccionario del gasto más caro.
    * `generar_reporte()`: Muestra info formateada.
* **Métodos de clase:**
    * `@classmethod proyectos_activos()`

**Prueba:** Crea 3 proyectos, registra gastos, cambia estados y genera reportes.

---

## Ejercicio 6: Sistema de Biblioteca con Control de Préstamos

Crea una clase `Libro` con:

* **Variables de clase:**
    * `biblioteca_nombre = "Biblioteca Municipal"`
    * `dias_prestamo_maximo = 14`
    * `total_libros = 0`
    * `libros_prestados_actualmente = 0`
* **Atributos de instancia:**
    * `titulo`, `autor`, `isbn`
    * `disponible` (booleano)
    * `usuario_actual` (`None` o nombre)
    * `veces_prestado` (contador)
    * `prestamos_historico` (lista de diccionarios: `{usuario, fecha_prestamo, fecha_devolucion}`)
* **Métodos:**
    * `__init__()`: Inicializa.
    * `prestar(nombre_usuario)`: Presta si está disponible, actualiza contadores (retorna `True`/`False`).
    * `devolver()`: Devuelve, actualiza contadores e historial (retorna `True`/`False`).
    * `esta_disponible()`
    * `obtener_info_prestamo()`
    * `es_popular()`: Retorna `True` si `veces_prestado > 5`.
    * `obtener_historial()`
* **Métodos de clase:**
    * `@classmethod libros_en_prestamo()`
    * `@classmethod cambiar_dias_prestamo(nuevos_dias)`
    * `@classmethod porcentaje_prestados()`

**Prueba:** Crea 8 libros, simula préstamos y devoluciones, e identifica libros populares.

---

## Ejercicio 7: Sistema de Calificaciones de Estudiantes

Crea una clase `Estudiante` con:

* **Variables de clase:**
    * `contador_matriculas = 2024000`
    * `calificacion_minima_aprobatoria = 6.0`
    * `total_estudiantes = 0`
* **Atributos de instancia:**
    * `nombre`
    * `matricula` (generada automáticamente: "2024001", "2024002", etc.)
    * `calificaciones` (diccionario: `{materia: [lista de notas]}`)
    * `semestre`
* **Métodos:**
    * `__init__(nombre, semestre)`
    * `agregar_materia(nombre_materia)`
    * `registrar_calificacion(materia, calificacion)`: (0-10)
    * `calcular_promedio_materia(materia)`
    * `calcular_promedio_general()`
    * `obtener_materias_aprobadas()`
    * `obtener_materias_reprobadas()`
    * `obtener_mejor_materia()`
    * `obtener_peor_materia()`
    * `tiene_materias_reprobadas()`: Retorna `True`/`False`.
    * `generar_boleta()`: Muestra reporte completo.
* **Métodos de clase:**
    * `@classmethod total_estudiantes_registrados()`

**Prueba:** Crea 4 estudiantes, agrega 5 materias a c/u, registra calificaciones y genera boletas.

---

## Ejercicio 8: Sistema de Reservas de Hotel

Crea una clase `Habitacion` con:

* **Variables de clase:**
    * `total_habitaciones = 0`
    * `habitaciones_ocupadas = 0`
    * `precios_base = {"Simple": 100, "Doble": 150, "Suite": 300}`
* **Atributos de instancia:**
    * `numero`, `tipo` ("Simple", "Doble", "Suite"), `precio_noche`
    * `ocupada` (booleano), `huesped_actual`
    * `servicios_extras` (lista de diccionarios: `{servicio: str, precio: float}`)
    * `reservas_totales` (contador)
* **Métodos:**
    * `__init__(numero, tipo)`: Asigna precio según `precios_base`.
    * `reservar(nombre_huesped)`
    * `liberar()`
    * `agregar_servicio_extra(servicio, precio)`
    * `calcular_costo_servicios()`
    * `calcular_costo_total(num_noches)`: Retorna `(precio_noche * noches) + servicios_extras`.
    * `obtener_info()`
    * `es_suite()`: Retorna `True`/`False`.
* **Métodos de clase:**
    * `@classmethod calcular_ocupacion()`: Retorna porcentaje.
    * `@classmethod habitaciones_disponibles_por_tipo(tipo)`
    * `@classmethod actualizar_precio_base(tipo, nuevo_precio)`

**Prueba:** Crea 12 habitaciones, realiza reservas, agrega servicios y genera reportes.

---

## Ejercicio 9: Sistema de Pedidos de Restaurante

Crea una clase `Pedido` con:

* **Variables de clase:**
    * `contador_pedidos = 0`
    * `total_pedidos = 0`
    * `pedidos_activos = 0`
    * `propina_sugerida = 0.10`
* **Atributos de instancia:**
    * `numero_pedido` (generado automáticamente)
    * `cliente`, `mesa`
    * `items` (lista de diccionarios: `{platillo, cantidad, precio_unitario}`)
    * `estado` ("Pendiente", "En Preparación", "Listo", "Entregado")
    * `propina` (inicialmente 0)
* **Métodos:**
    * `__init__(cliente, mesa)`: Estado "Pendiente".
    * `agregar_item(platillo, cantidad, precio_unitario)`
    * `eliminar_item(platillo)`
    * `calcular_subtotal()`
    * `agregar_propina(porcentaje)`
    * `calcular_total()`: Retorna `subtotal + propina`.
    * `cambiar_estado(nuevo_estado)`
    * `obtener_cantidad_items()`
    * `obtener_item_mas_caro()`
    * `generar_ticket()`: Muestra ticket formateado.
* **Métodos de clase:**
    * `@classmethod pedidos_pendientes()`
    * `@classmethod cambiar_propina_sugerida(nuevo_porcentaje)`

**Prueba:** Crea 6 pedidos, agrega items, cambia estados y genera tickets.

---

## Ejercicio 10: Sistema de Eventos y Asistentes

Crea una clase `Evento` con:

* **Variables de clase:**
    * `total_eventos = 0`
    * `eventos_agotados = 0`
    * `descuento_estudiante = 0.20`
    * `descuento_grupo = 0.15` (para 4 o más)
* **Atributos de instancia:**
    * `nombre_evento`, `fecha`, `ubicacion`, `capacidad_maxima`, `precio_entrada`
    * `asistentes_registrados` (lista de diccionarios: `{nombre, email, pago_realizado: bool}`)
    * `ingresos_totales`
    * `tipo_evento` ("Concierto", "Conferencia", etc.)
* **Métodos:**
    * `__init__()`: Inicializa.
    * `registrar_asistente(nombre, email, es_estudiante=False)`
    * `registrar_grupo(lista_asistentes, cantidad)`
    * `confirmar_pago(email)`: Marca `pago_realizado=True` y suma a `ingresos` (aplica descuento si es estudiante).
    * `calcular_asistentes_confirmados()`
    * `calcular_asistentes_pendientes()`
    * `obtener_cupos_disponibles()`
    * `esta_agotado()`: Retorna `True`/`False`.
    * `calcular_porcentaje_ocupacion()`
    * `calcular_ingreso_potencial()`
    * `obtener_lista_asistentes()`: Retorna lista de nombres confirmados.
    * `cancelar_registro(email)`
    * `generar_reporte()`
* **Métodos de clase:**
    * `@classmethod total_eventos_creados()`
    * `@classmethod actualizar_descuento_estudiante(nuevo_descuento)`
    * `@classmethod eventos_sold_out()`

**Prueba:** Crea 4 eventos, registra asistentes (individuales y grupos), confirma/cancela pagos, llena un evento y genera reportes.