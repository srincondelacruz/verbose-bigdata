# Práctica 16 (Parte 1): OOP - Nivel Intermedio

Ejercicios avanzados de Programación Orientada a Objetos para simular sistemas de gestión complejos, utilizando variables de clase, métodos de clase y lógica de negocio.

---

## Ejercicio 1: Sistema de Gestión de Empleados

Crea una clase `EmpleadoEmpresa` con las siguientes características:

* **Variables de clase:**
    * `total_empleados = 0`
    * `salario_minimo = 1000`
    * `empresa = "TechCorp"`
* **Atributos de instancia:**
    * `nombre`, `edad`, `salario`, `departamento`, `años_experiencia`
* **Métodos:**
    * `__init__()`: Inicializa atributos. Valida que `salario` sea `>=` a `salario_minimo`, si no, asigna `salario_minimo`. Incrementa `total_empleados`.
    * `aumentar_salario(porcentaje)`: Aumenta el salario.
    * `cambiar_departamento(nuevo_depto)`: Cambia el departamento.
    * `cumplir_años()`: Incrementa `edad` y `años_experiencia`.
    * `calcular_salario_anual()`: Retorna `salario * 12`.
    * `es_senior()`: Retorna `True` si tiene más de 5 años de experiencia.
    * `get_info_completa()`: Retorna un string con toda la información del empleado.
* **Métodos de clase:**
    * `@classmethod empleados_registrados()`: Retorna `total_empleados`.
    * `@classmethod actualizar_salario_minimo(nuevo_minimo)`: Actualiza `salario_minimo`.

**Prueba:** Crea 5 empleados, realiza operaciones (aumentos, cambios de depto) y muestra un resumen.

---

## Ejercicio 2: Sistema de Inventario de Tienda

Crea una clase `Articulo` con:

* **Variables de clase:**
    * `contador_articulos = 0`
    * `iva = 0.21`
* **Atributos de instancia:**
    * `codigo` (generado automáticamente: "ART001", "ART002", etc.)
    * `nombre`, `precio`, `stock`, `categoria`
* **Métodos:**
    * `__init__(nombre, precio, stock_inicial, categoria)`: Inicializa y genera `codigo` automático.
    * `vender(cantidad)`: Reduce `stock` si hay suficiente (retorna `True`/`False`).
    * `reabastecer(cantidad)`: Aumenta `stock`.
    * `calcular_valor_inventario()`: Retorna `precio * stock`.
    * `calcular_precio_con_iva()`: Retorna `precio * (1 + iva)`.
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
    * `capacidad_maxima`, `profesor`
* **Métodos:**
    * `__init__()`: Inicializa atributos e incrementa `total_cursos`.
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
    * `__init__(titular, saldo_inicial)`: Inicializa, genera `numero_cuenta` y registra el depósito inicial.
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
    * `__init__()`: Inicializa atributos e incrementa `total_proyectos`.
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
    * `titulo`, `autor`, `isbn`, `disponible` (bool)
    * `usuario_actual` (`None` o nombre)
    * `veces_prestado` (contador)
    * `prestamos_historico` (lista de diccionarios: `{usuario, fecha_prestamo, fecha_devolucion}`)
* **Métodos:**
    * `__init__()`: Inicializa e incrementa `total_libros`.
    * `prestar(nombre_usuario)`: Presta si está disponible (retorna `True`/`False`).
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
    * `nombre`, `semestre`
    * `matricula` (generada automáticamente: "2024001", "2024002", etc.)
    * `calificaciones` (diccionario: `{materia: [lista de notas]}`)
* **Métodos:**
    * `__init__(nombre, semestre)`: Genera matrícula e incrementa `total_estudiantes`.
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
    * `__init__(numero, tipo)`: Asigna precio según `precios_base` e incrementa `total_habitaciones`.
    * `reservar(nombre_huesped)`: Marca como ocupada y actualiza contador.
    * `liberar()`: Desocupa y limpia datos.
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
    * `total_pedidos = 0` (obsoleto, usar contador)
    * `pedidos_activos = 0`
    * `propina_sugerida = 0.10`
* **Atributos de instancia:**
    * `numero_pedido` (generado automáticamente)
    * `cliente`, `mesa`
    * `items` (lista de diccionarios: `{platillo, cantidad, precio_unitario}`)
    * `estado` ("Pendiente", "En Preparación", "Listo", "Entregado")
    * `propina` (inicialmente 0)
* **Métodos:**
    * `__init__(cliente, mesa)`: Estado "Pendiente", genera `numero_pedido`.
    * `agregar_item(platillo, cantidad, precio_unitario)`
    * `eliminar_item(platillo)`
    * `calcular_subtotal()`
    * `agregar_propina(porcentaje)`
    * `calcular_total()`: Retorna `subtotal + propina`.
    * `cambiar_estado(nuevo_estado)`: Actualiza contadores `pedidos_activos`.
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
    * `__init__()`: Inicializa e incrementa `total_eventos`.
    * `registrar_asistente(nombre, email, es_estudiante=False)`
    * `registrar_grupo(lista_asistentes)`: (*Corrección: debe recibir una lista de asistentes, no `cantidad`*).
    * `confirmar_pago(email)`: Marca `pago_realizado=True` y suma a `ingresos` (aplica descuento).
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

# Parte 2 - Métodos y Encapsulación (Nivel Intermedio)

Ejercicios avanzados de OOP enfocados en la encapsulación (atributos privados `__`), métodos *getter/setter*, validaciones y la interacción entre múltiples clases.

---

## Ejercicio 1: Sistema de Biblioteca (Interacción de Clases)

Crea dos clases: `Libro` y `Biblioteca`.

**Clase `Libro`:**
* Atributos: `titulo`, `autor`, `isbn`, `disponible` (booleano).
* Método `__str__` que muestre la información del libro.
* Método `prestar()` que cambie el estado a no disponible.
* Método `devolver()` que cambie el estado a disponible.

**Clase `Biblioteca`:**
* Atributo privado `__libros` (lista).
* Método `agregar_libro(libro)`.
* Método `buscar_por_titulo(titulo)` que retorne el objeto libro o un mensaje de error.
* Método `libros_disponibles()` que muestre solo los libros disponibles.
* Método `prestar_libro(isbn)` que use los métodos del objeto `Libro`.

**Prueba:** Crea una biblioteca con 5 libros y simula préstamos y devoluciones.

---

## Ejercicio 2: Sistema de Empleados con Validaciones (Encapsulación)

Crea una clase `Empleado` con encapsulación completa:

* **Atributos privados:** `__nombre`, `__salario`, `__departamento`, `__años_experiencia`.
* **Constructor (`__init__`)** que valide:
    * Salario debe ser `> 0`.
    * Años de experiencia no pueden ser negativos.
    * Nombre no puede estar vacío.
* **Métodos Públicos (Getters):** `get_nombre()`, `get_salario()`, etc.
* **Métodos Públicos (Setters/Acciones):**
    * `aumentar_salario(porcentaje)`: Valida que el porcentaje esté entre 1 y 50.
    * `cambiar_departamento(nuevo_depto)`.
* **Métodos de Cálculo:**
    * `calcular_bono()`: Retorna 10% del salario por cada año de experiencia.
* **Método `__str__`** que muestre toda la información.

**Prueba:** Maneja las validaciones con mensajes de error apropiados.

---

## Ejercicio 3: Sistema de Reservas de Hotel (Multi-Clase)

Crea tres clases: `Habitacion`, `Cliente` y `Hotel`.

* **Clase `Habitacion`:**
    * Atributos: `numero`, `tipo` (simple/doble/suite), `precio_noche`, `ocupada` (bool).
    * Métodos: `ocupar()` y `desocupar()`.
* **Clase `Cliente`:**
    * Atributos: `nombre`, `dni`, `email`.
    * Método `__str__`.
* **Clase `Hotel`:**
    * Atributo privado `__habitaciones` (lista de objetos `Habitacion`).
    * Atributo privado `__reservas` (diccionario: `dni_cliente -> numero_habitacion`).
    * Métodos: `agregar_habitacion(habitacion)`, `mostrar_habitaciones_disponibles()`, `hacer_reserva(cliente, numero_habitacion)`, `cancelar_reserva(dni_cliente)`, `calcular_ingreso_total()`.

---

## Ejercicio 4: Control de Inventario con Alertas (Getters/Setters)

Crea dos clases: `Producto` y `Almacen`.

* **Clase `Producto`:**
    * Atributos privados: `__codigo`, `__nombre`, `__cantidad`, `__precio`, `__stock_minimo`.
    * Métodos públicos: Getters y Setters con validaciones (ej. `set_cantidad()` no puede ser negativo).
    * Método `necesita_reposicion()`: Retorna `True` si `cantidad < stock_minimo`.
    * Método `valor_total()`: Retorna `cantidad * precio`.
* **Clase `Almacen`:**
    * Atributo privado `__productos` (lista de objetos `Producto`).
    * Métodos: `agregar_producto(producto)`, `buscar_producto(codigo)`, `vender_producto(codigo, cantidad)`, `reabastecer_producto(codigo, cantidad)`.
    * Métodos de Reporte: `productos_bajo_stock()`, `valor_inventario_total()`.

---

## Ejercicio 5: Sistema de Calificaciones Estudiantiles

Crea tres clases: `Materia`, `Estudiante` y `SistemaAcademico`.

* **Clase `Materia`:**
    * Atributos: `nombre`, `codigo`, `creditos`.
* **Clase `Estudiante`:**
    * Atributos: `nombre`, `matricula`.
    * Atributo privado `__calificaciones` (diccionario: `codigo_materia -> nota`).
    * Métodos: `agregar_calificacion(materia, nota)` (valida 0-10), `calcular_promedio()`, `materias_aprobadas()` (nota >= 6), `materias_reprobadas()`, `obtener_calificacion(codigo_materia)`.
* **Clase `SistemaAcademico`:**
    * Gestión de múltiples estudiantes (lista de objetos `Estudiante`).
    * Método `encontrar_mejor_promedio()`.
    * Método `listar_reprobados()` (promedio < 6).

---

## Ejercicio 6: Simulador de Cajero Automático (ATM)

Crea un sistema bancario con: `Tarjeta`, `CuentaBancaria` y `CajeroAutomatico`.

* **Clase `Tarjeta`:**
    * Atributos privados: `__numero`, `__pin`, `__intentos_fallidos`, `__bloqueada`.
    * Método `validar_pin(pin)`: Incrementa intentos fallidos, bloquea tras 3 intentos.
    * Método `desbloquear(pin_maestro)`.
* **Clase `CuentaBancaria`:**
    * Atributos privados: `__numero_cuenta`, `__titular`, `__saldo`, `__tarjeta` (objeto `Tarjeta`).
    * Métodos: `depositar()`, `retirar()` (valida fondos), `consultar_saldo()`.
* **Clase `CajeroAutomatico`:**
    * Atributo privado `__cuentas` (diccionario: `numero_tarjeta -> objeto CuentaBancaria`).
    * Método `insertar_tarjeta(numero_tarjeta, pin)`.
    * Método `realizar_operacion(tipo, monto)` (solo si la tarjeta está validada).
    * Registro de transacciones.

---

## Ejercicio 7: Sistema de Vehículos (Composición)

Crea clases para vehículos *sin* usar herencia formal (usando composición/atributos).

* **Clase `Auto`:**
    * Atributos: `marca`, `modelo`, `año`, `kilometraje`, `tipo_combustible`.
    * Atributos privados: `__encendido`, `__velocidad_actual`, `__combustible_actual`.
    * Métodos: `encender()`, `apagar()`, `acelerar(incremento)`, `frenar(decremento)`.
    * Métodos: `cargar_combustible(litros)`, `calcular_consumo()`.
* **Clase `Moto`:**
    * Similar a `Auto` pero con atributos propios (`cilindrada`, `tipo_moto`).
* **Clase `Concesionaria`:**
    * Gestión de inventario de autos y motos (dos listas).
    * Métodos: `vender()`, `comprar()`, `buscar_por_caracteristicas()`.

---

## Ejercicio 8: Juego de Cartas (Batalla)

Crea un juego simple de cartas con: `Carta`, `Mazo` y `Jugador`.

* **Clase `Carta`:**
    * Atributos: `valor` (1-13), `palo` (corazones, diamantes, tréboles, picas).
    * Método `__str__` (ej. "As de Picas").
    * Método para comparar cartas.
* **Clase `Mazo`:**
    * Atributo privado `__cartas` (lista de 52 objetos `Carta`).
    * Método privado `__crear_mazo()`: Genera las 52 cartas.
    * Método `barajar()`.
    * Método `repartir_carta()`: Saca la primera carta (`pop`).
    * Método `cartas_restantes()`.
* **Clase `Jugador`:**
    * Atributos: `nombre`, lista privada `__cartas_mano`.
    * Métodos: `recibir_carta()`, `jugar_carta()`, `contar_cartas()`.
* **Lógica:** Implementa el juego básico (dos jugadores reciben cartas y compiten).

---

## Ejercicio 9: Sistema de Citas Médicas

Crea un sistema completo con: `Paciente`, `Doctor`, `Cita` y `Hospital`.

* **Clase `Paciente`:**
    * Atributos: `nombre`, `edad`, `numero_seguro`.
    * Atributo privado `__historial_citas` (lista).
    * Método `agregar_cita_historial()`.
* **Clase `Doctor`:**
    * Atributos: `nombre`, `especialidad`, `horario_disponible` (lista de horas).
    * Atributo privado `__citas_programadas` (diccionario: `fecha -> lista de horas ocupadas`).
    * Método `verificar_disponibilidad(fecha, hora)`.
* **Clase `Cita`:**
    * Atributos: `paciente` (objeto), `doctor` (objeto), `fecha`, `hora`, `motivo`, `estado` (Confirmada, Cancelada, Completada).
    * Métodos: `confirmar()`, `cancelar()`, `completar()`.
* **Clase `Hospital`:**
    * Gestión de listas de doctores, pacientes y citas.
    * Método `agendar_cita()`: Verifica disponibilidad del doctor antes de crear el objeto `Cita`.
    * Método `cancelar_cita()`.
    * Método `citas_del_dia(fecha)`.
    * Método `buscar_doctor_por_especialidad()`.

---

## Ejercicio 10: Sistema de Restaurante Completo

Crea un sistema de gestión de restaurante con múltiples clases interactuando.

* **Clase `Platillo`:**
    * Atributos: `nombre`, `precio`, `categoria`, `tiempo_preparacion`, `disponible`.
* **Clase `Mesa`:**
    * Atributos: `numero`, `capacidad`, `ocupada`.
    * Atributo privado `__pedido_actual` (lista de objetos `Platillo`).
    * Métodos: `agregar_platillo()`, `calcular_total()`, `dividir_cuenta()`.
* **Clase `Mesero`:**
    * Atributos: `nombre`, `id_empleado`.
    * Atributo privado `__mesas_asignadas` (lista de objetos `Mesa`).
    * Método `calcular_total_ventas_mesas()`.
* **Clase `Restaurante`:**
    * Atributos privados: `__menu` (lista de `Platillo`), `__mesas`, `__meseros`.
    * Método `mostrar_menu_por_categoria()`.
    * Método `asignar_mesa(numero_personas)`.
    * Método `tomar_pedido(numero_mesa, platillos)`.
    * Método `cerrar_cuenta(numero_mesa)` (con opción de propina).
    * Método `reporte_ventas_del_dia()`.
    * Método privado `__calcular_tiempo_espera()` (basado en platillos ordenados).