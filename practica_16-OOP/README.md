# Práctica 16: Programación Orientada a Objetos (OOP)

Este directorio contiene los ejercicios prácticos sobre Programación Orientada a Objetos en Python. La práctica está dividida en dos niveles de dificultad.

## 🗂️ Índice de Archivos

* **[TUTORIAL.md](./TUTORIAL.md)**: El guion completo con todos los enunciados (Nivel Principiante, Nivel Intermedio/Encapsulación).

* **[Nivel_Intermedio.py](./Nivel_Intermedio.py)**: Soluciones a la Parte 1 (Ejercicios 1-10: Clases `Libro`, `Estudiante`, `Coche`, etc.).

* **[Nivel_Intermedio_2.py](./Nivel_Intermedio_2.py)**: Soluciones a la Parte 2 (Ejercicios 1-10: `EmpleadoEmpresa`, `Inventario`, `CuentaBancaria`, etc.).

## 🧠 Enfoque y Lógica

* **Nivel Intermedio:** Se centra en la creación de clases simples, la definición de atributos en el `__init__` y la implementación de métodos de instancia y métodos de clase (`@classmethod`).

* **Nivel Intermedio_2:** Avanza hacia conceptos más complejos como la **encapsulación** (atributos privados `__`), la creación de *getters/setters* con validación, y la **interacción entre múltiples clases** (ej. `Hotel` gestionando `Habitacion`).

---

# Práctica 16: Programación Orientada a Objetos (OOP)

Este directorio contiene los ejercicios prácticos sobre Programación Orientada a Objetos en Python, desde conceptos básicos hasta sistemas de gestión intermedios.

## 🎯 Objetivo

Dominar los pilares de la OOP: clases, objetos, atributos (de instancia y de clase), métodos (de instancia y de clase), y el constructor `__init__`.

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