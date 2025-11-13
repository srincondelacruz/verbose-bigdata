# --- Nivel_Intermedio_2.py ---
# Soluciones completas a los 10 ejercicios de la Parte 2 (Encapsulación)

import random # Necesario para Ejercicio 8
import math   # Necesario para Ejercicio 2

# -----------------------------------------------------------------
# Ejercicio 1: Sistema de Biblioteca
# -----------------------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        """Muestra la información del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.isbn}] '{self.titulo}' por {self.autor} - ({estado})"

    def prestar(self):
        """Marca el libro como no disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        """Marca el libro como disponible."""
        if not self.disponible:
            self.disponible = True
            return True
        return False

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__libros = [] # Atributo privado

    def agregar_libro(self, libro):
        """Añade un objeto Libro a la biblioteca."""
        self.__libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca {self.nombre}.")

    def buscar_por_titulo(self, titulo):
        """Busca un libro por título exacto."""
        for libro in self.__libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return f"Error: Libro con título '{titulo}' no encontrado."

    def libros_disponibles(self):
        """Muestra solo los libros disponibles."""
        print(f"\n--- Libros Disponibles en {self.nombre} ---")
        disponibles = False
        for libro in self.__libros:
            if libro.disponible:
                print(f"  - {libro.titulo} por {libro.autor}")
                disponibles = True
        if not disponibles:
            print(" (No hay libros disponibles en este momento)")

    def prestar_libro(self, isbn):
        """Presta un libro usando su ISBN si está disponible."""
        libro_encontrado = None
        for libro in self.__libros:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break
        
        if libro_encontrado:
            if libro_encontrado.prestar():
                print(f"Éxito: '{libro_encontrado.titulo}' ha sido prestado.")
            else:
                print(f"Fallo: '{libro_encontrado.titulo}' ya estaba prestado.")
        else:
            print(f"Error: No se encontró ningún libro con ISBN {isbn}.")

# --- Pruebas Ejercicio 1 ---
print("\n--- Ejercicio 1: Sistema de Biblioteca ---")
biblio = Biblioteca("Biblioteca Municipal")
l1 = Libro("1984", "George Orwell", "111A")
l2 = Libro("Dune", "Frank Herbert", "222B")
l3 = Libro("Fahrenheit 451", "Ray Bradbury", "333C")
l4 = Libro("El Aleph", "J.L. Borges", "444D")
l5 = Libro("Neurodancer", "W. Gibson", "555E")

biblio.agregar_libro(l1)
biblio.agregar_libro(l2)
biblio.agregar_libro(l3)
biblio.agregar_libro(l4)
biblio.agregar_libro(l5)

biblio.libros_disponibles()

print("\n--- Préstamos ---")
biblio.prestar_libro("111A") # Presta 1984
biblio.prestar_libro("222B") # Presta Dune
biblio.prestar_libro("111A") # Falla (ya prestado)
biblio.prestar_libro("999Z") # Falla (no existe)

biblio.libros_disponibles() # Muestra los 3 restantes

print("\n--- Devoluciones ---")
libro_1984 = biblio.buscar_por_titulo("1984")
if isinstance(libro_1984, Libro):
    libro_1984.devolver()
    print(f"'{libro_1984.titulo}' ha sido devuelto.")

biblio.libros_disponibles() # Muestra los 4 disponibles


# -----------------------------------------------------------------
# Ejercicio 2: Sistema de Empleados con Validaciones
# -----------------------------------------------------------------

class Empleado:
    def __init__(self, nombre, salario, departamento, anos_experiencia):
        # Validaciones en el constructor
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre
        
        if salario <= 0:
            raise ValueError("El salario debe ser mayor a 0.")
        self.__salario = salario
        
        self.__departamento = departamento
        
        if anos_experiencia < 0:
            raise ValueError("Los años de experiencia no pueden ser negativos.")
        self.__anos_experiencia = anos_experiencia
        print(f"Empleado '{nombre}' creado con éxito.")

    # --- Getters (Métodos públicos para obtener atributos) ---
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    def get_departamento(self):
        return self.__departamento

    def get_anos_experiencia(self):
        return self.__anos_experiencia

    # --- Métodos de Acción (Setters/Modificadores) ---
    def aumentar_salario(self, porcentaje):
        if 1 <= porcentaje <= 50:
            aumento = 1 + (porcentaje / 100)
            self.__salario = round(self.__salario * aumento, 2)
            print(f"Salario de {self.__nombre} aumentado a {self.__salario}€")
        else:
            print(f"Error: Porcentaje ({porcentaje}%) fuera del rango válido (1-50).")

    def cambiar_departamento(self, nuevo_depto):
        self.__departamento = nuevo_depto
        print(f"{self.__nombre} transferido al departamento de {self.__departamento}.")

    # --- Métodos de Cálculo ---
    def calcular_bono(self):
        # 10% del salario por CADA año de experiencia
        bono_por_anio = self.__salario * 0.10
        bono_total = bono_por_anio * self.__anos_experiencia
        return round(bono_total, 2)

    def __str__(self):
        return (f"--- Empleado: {self.__nombre} ---\n"
                f"  Departamento: {self.__departamento}\n"
                f"  Salario: {self.__salario}€\n"
                f"  Experiencia: {self.__anos_experiencia} años\n"
                f"  Bono Anual: {self.calcular_bono()}€")

# --- Pruebas Ejercicio 2 ---
print("\n--- Ejercicio 2: Empleados con Encapsulación ---")
try:
    emp1 = Empleado("Carlos Ruiz", 50000, "IT", 6)
    emp2 = Empleado("Ana Torres", 60000, "Ventas", 3)
    # emp_error = Empleado("Error", -100, "Test", 0) # Descomentar para probar error de salario
    # emp_error2 = Empleado("", 50000, "Test", 0) # Descomentar para probar error de nombre

    print(emp1)
    emp1.aumentar_salario(10) # Válido
    emp1.aumentar_salario(60) # Falla
    emp1.cambiar_departamento("Innovación")
    print(f"Salario final de {emp1.get_nombre()}: {emp1.get_salario()}")
    print(emp1)

except ValueError as e:
    print(f"Error al crear empleado: {e}")


# -----------------------------------------------------------------
# Ejercicio 3: Sistema de Reservas de Hotel
# -----------------------------------------------------------------

class Habitacion:
    def __init__(self, numero, tipo, precio_noche):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.ocupada = False

    def ocupar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def desocupar(self):
        if self.ocupada:
            self.ocupada = False
            return True
        return False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Hab. {self.numero} ({self.tipo}) - {self.precio_noche}€ - {estado}"

class Cliente:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.dni = dni
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} (DNI: {self.dni})"

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__habitaciones = [] # Lista de objetos Habitacion
        self.__reservas = {}     # Diccionario: dni_cliente -> número_habitación

    def agregar_habitacion(self, habitacion):
        self.__habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} añadida al {self.nombre}.")

    def mostrar_habitaciones_disponibles(self):
        print(f"\n--- Habitaciones Disponibles en {self.nombre} ---")
        disponibles = False
        for h in self.__habitaciones:
            if not h.ocupada:
                print(f"  - {h}")
                disponibles = True
        if not disponibles:
            print(" (No hay habitaciones disponibles)")

    def _buscar_habitacion(self, numero_habitacion):
        for h in self.__habitaciones:
            if h.numero == numero_habitacion:
                return h
        return None

    def hacer_reserva(self, cliente, numero_habitacion):
        if cliente.dni in self.__reservas:
            print(f"Error: {cliente.nombre} ya tiene una reserva activa.")
            return

        habitacion = self._buscar_habitacion(numero_habitacion)
        
        if not habitacion:
            print(f"Error: Habitación {numero_habitacion} no existe.")
            return

        if habitacion.ocupar():
            self.__reservas[cliente.dni] = numero_habitacion
            print(f"Éxito: {cliente.nombre} ha reservado la Habitación {numero_habitacion}.")
        else:
            print(f"Error: Habitación {numero_habitacion} ya está ocupada.")

    def cancelar_reserva(self, dni_cliente):
        if dni_cliente in self.__reservas:
            numero_habitacion = self.__reservas.pop(dni_cliente)
            habitacion = self._buscar_habitacion(numero_habitacion)
            if habitacion:
                habitacion.desocupar()
            print(f"Reserva del cliente {dni_cliente} (Hab. {numero_habitacion}) cancelada.")
        else:
            print(f"Error: Cliente {dni_cliente} no tenía reserva.")

    def calcular_ingreso_total(self):
        total = 0
        for h in self.__habitaciones:
            if h.ocupada:
                total += h.precio_noche
        return total

# --- Pruebas Ejercicio 3 ---
print("\n--- Ejercicio 3: Sistema de Hotel ---")
hotel_plaza = Hotel("Hotel Plaza")
c1 = Cliente("Juan Perez", "111A", "juan@mail.com")
c2 = Cliente("Maria Lopez", "222B", "maria@mail.com")

h101 = Habitacion(101, "Simple", 80)
h102 = Habitacion(102, "Simple", 80)
h201 = Habitacion(201, "Doble", 120)
h301 = Habitacion(301, "Suite", 250)

hotel_plaza.agregar_habitacion(h101)
hotel_plaza.agregar_habitacion(h102)
hotel_plaza.agregar_habitacion(h201)
hotel_plaza.agregar_habitacion(h301)

hotel_plaza.mostrar_habitaciones_disponibles()

print("\n--- Reservas ---")
hotel_plaza.hacer_reserva(c1, 101)
hotel_plaza.hacer_reserva(c2, 301)
hotel_plaza.hacer_reserva(c1, 201) # Falla (cliente ya tiene reserva)

hotel_plaza.mostrar_habitaciones_disponibles()
print(f"Ingreso total por noche: {hotel_plaza.calcular_ingreso_total()}€")

print("\n--- Cancelaciones ---")
hotel_plaza.cancelar_reserva(c1.dni)
hotel_plaza.mostrar_habitaciones_disponibles()
print(f"Ingreso total por noche: {hotel_plaza.calcular_ingreso_total()}€")


# -----------------------------------------------------------------
# Ejercicio 4: Control de Inventario con Alertas
# -----------------------------------------------------------------

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio, stock_minimo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidad = max(0, cantidad) # Validación básica
        self.__precio = max(0, precio)
        self.__stock_minimo = max(0, stock_minimo)

    # --- Getters ---
    def get_codigo(self): return self.__codigo
    def get_nombre(self): return self.__nombre
    def get_cantidad(self): return self.__cantidad
    def get_precio(self): return self.__precio
    def get_stock_minimo(self): return self.__stock_minimo

    # --- Setters (con validación) ---
    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = max(0, nueva_cantidad)

    def set_precio(self, nuevo_precio):
        self.__precio = max(0, nuevo_precio)
        
    def set_stock_minimo(self, nuevo_minimo):
        self.__stock_minimo = max(0, nuevo_minimo)

    # --- Métodos ---
    def necesita_reposicion(self):
        return self.__cantidad < self.__stock_minimo

    def valor_total(self):
        return self.__cantidad * self.__precio

    def __str__(self):
        alerta = " (!) BAJO STOCK" if self.necesita_reposicion() else ""
        return f"[{self.get_codigo()}] {self.get_nombre()} - Stock: {self.get_cantidad()} (Min: {self.get_stock_minimo()}) - Valor: {self.valor_total()}€ {alerta}"

class Almacen:
    def __init__(self):
        self.__productos = [] # Lista de objetos Producto

    def _buscar_producto_obj(self, codigo):
        for p in self.__productos:
            if p.get_codigo() == codigo:
                return p
        return None

    def agregar_producto(self, producto):
        if not self._buscar_producto_obj(producto.get_codigo()):
            self.__productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al almacén.")
        else:
            print(f"Error: Producto con código {producto.get_codigo()} ya existe.")

    def buscar_producto(self, codigo):
        producto = self._buscar_producto_obj(codigo)
        if producto:
            return producto
        else:
            return f"Error: Producto {codigo} no encontrado."

    def vender_producto(self, codigo, cantidad_venta):
        producto = self._buscar_producto_obj(codigo)
        if not producto:
            print(f"Error Venta: Producto {codigo} no existe.")
            return

        if producto.get_cantidad() >= cantidad_venta:
            producto.set_cantidad(producto.get_cantidad() - cantidad_venta)
            print(f"Venta: {cantidad_venta} de '{producto.get_nombre()}'. Stock restante: {producto.get_cantidad()}")
            if producto.necesita_reposicion():
                print(f"  ALERTA: {producto.get_nombre()} ha caído bajo el stock mínimo.")
        else:
            print(f"Error Venta: Stock insuficiente de '{producto.get_nombre()}' (Stock: {producto.get_cantidad()})")

    def reabastecer_producto(self, codigo, cantidad_recarga):
        producto = self._buscar_producto_obj(codigo)
        if producto:
            producto.set_cantidad(producto.get_cantidad() + cantidad_recarga)
            print(f"Reabastecido: {cantidad_recarga} de '{producto.get_nombre()}'. Stock nuevo: {producto.get_cantidad()}")
        else:
            print(f"Error Reabastecer: Producto {codigo} no existe.")

    def productos_bajo_stock(self):
        print("\n--- Reporte: Productos Bajo Stock Mínimo ---")
        bajo_stock = [p for p in self.__productos if p.necesita_reposicion()]
        if not bajo_stock:
            print(" (Ningún producto necesita reposición)")
            return
        for p in bajo_stock:
            print(f"  - {p.get_nombre()} (Stock: {p.get_cantidad()}, Mín: {p.get_stock_minimo()})")

    def valor_inventario_total(self):
        total = sum(p.valor_total() for p in self.__productos)
        return total

# --- Pruebas Ejercicio 4 ---
print("\n--- Ejercicio 4: Control de Inventario ---")
almacen_central = Almacen()
p1 = Producto("P001", "Laptop", 10, 1200, 5)
p2 = Producto("P002", "Teclado", 30, 80, 10)
p3 = Producto("P003", "Monitor", 8, 250, 3) # Bajo stock

almacen_central.agregar_producto(p1)
almacen_central.agregar_producto(p2)
almacen_central.agregar_producto(p3)

print("\n--- Operaciones de Almacén ---")
almacen_central.vender_producto("P001", 3) # Vende 3 Laptops
almacen_central.vender_producto("P002", 25) # Vende 25 Teclados (deja 5, necesita reposición)
almacen_central.vender_producto("P003", 10) # Falla (stock insuficiente)
almacen_central.reabastecer_producto("P002", 50) # Reabastece Teclados

print("\n--- Reporte Final de Almacén ---")
almacen_central.productos_bajo_stock()
print(f"Valor total del inventario: {almacen_central.valor_inventario_total()}€")


# -----------------------------------------------------------------
# Ejercicio 5: Sistema de Calificaciones Estudiantiles
# -----------------------------------------------------------------

class Materia:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

class EstudianteCalificaciones: # Renombrada para evitar conflicto con Ej. Principiante
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.__calificaciones = {} # Diccionario: codigo_materia -> nota

    def agregar_calificacion(self, materia, nota):
        if 0 <= nota <= 10:
            self.__calificaciones[materia.codigo] = nota
            print(f"Calificación {nota} registrada para {self.nombre} en {materia.nombre}.")
        else:
            print(f"Error: Nota {nota} fuera de rango (0-10).")

    def calcular_promedio(self):
        if not self.__calificaciones:
            return 0.0
        return sum(self.__calificaciones.values()) / len(self.__calificaciones)

    def _filtrar_materias(self, aprobadas=True):
        materias_filtradas = []
        for codigo, nota in self.__calificaciones.items():
            if (aprobadas and nota >= 6) or (not aprobadas and nota < 6):
                materias_filtradas.append(codigo) # Simplificado a solo código
        return materias_filtradas

    def materias_aprobadas(self):
        return self._filtrar_materias(aprobadas=True)

    def materias_reprobadas(self):
        return self._filtrar_materias(aprobadas=False)

    def obtener_calificacion(self, codigo_materia):
        return self.__calificaciones.get(codigo_materia, "Materia no cursada")

class SistemaAcademico:
    def __init__(self):
        self.__estudiantes = [] # Lista de objetos Estudiante

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} añadido al sistema.")

    def encontrar_mejor_promedio(self):
        if not self.__estudiantes:
            return None
        # Usamos max con lambda para buscar en la lista de objetos
        return max(self.__estudiantes, key=lambda est: est.calcular_promedio())

    def listar_estudiantes_promedio_menor_a(self, umbral):
        reprobados = [est for est in self.__estudiantes if est.calcular_promedio() < umbral]
        return reprobados

# --- Pruebas Ejercicio 5 ---
print("\n--- Ejercicio 5: Sistema Académico ---")
# 1. Crear Materias
m_fisica = Materia("Física", "FIS101", 4)
m_calc = Materia("Cálculo", "MAT101", 5)
m_prog = Materia("Programación", "PRO101", 5)

# 2. Crear Estudiantes
e1 = EstudianteCalificaciones("Carlos", "A001")
e2 = EstudianteCalificaciones("Sofia", "A002")

# 3. Crear Sistema
sistema = SistemaAcademico()
sistema.agregar_estudiante(e1)
sistema.agregar_estudiante(e2)

# 4. Registrar Calificaciones
e1.agregar_calificacion(m_fisica, 8)
e1.agregar_calificacion(m_calc, 5) # Reprobada
e1.agregar_calificacion(m_prog, 9)

e2.agregar_calificacion(m_fisica, 9)
e2.agregar_calificacion(m_calc, 9)
e2.agregar_calificacion(m_prog, 10)

# 5. Reporte
print("\n--- Reporte Académico ---")
mejor_estudiante = sistema.encontrar_mejor_promedio()
if mejor_estudiante:
    print(f"Mejor Promedio: {mejor_estudiante.nombre} ({mejor_estudiante.calcular_promedio():.2f})")

reprobados = sistema.listar_estudiantes_promedio_menor_a(6.0)
print("\nEstudiantes con promedio general < 6.0:")
if reprobados:
    for e in reprobados:
        print(f"  - {e.nombre} ({e.calcular_promedio():.2f})")
else:
    print(" (Ninguno)")
    
print(f"\nMaterias reprobadas de {e1.nombre}: {e1.materias_reprobadas()}")


# -----------------------------------------------------------------
# Ejercicio 6: Simulador de Cajero Automático (ATM)
# -----------------------------------------------------------------

class Tarjeta:
    def __init__(self, numero, pin, pin_maestro="9999"):
        self.__numero = numero
        self.__pin = pin
        self.__intentos_fallidos = 0
        self.__bloqueada = False
        self.__pin_maestro = pin_maestro

    def is_bloqueada(self):
        return self.__bloqueada

    def validar_pin(self, pin_ingresado):
        if self.__bloqueada:
            print("Tarjeta bloqueada.")
            return False
            
        if pin_ingresado == self.__pin:
            self.__intentos_fallidos = 0
            return True
        else:
            self.__intentos_fallidos += 1
            if self.__intentos_fallidos >= 3:
                self.__bloqueada = True
                print("PIN incorrecto. Tarjeta bloqueada (3 intentos fallidos).")
            else:
                print(f"PIN incorrecto. Intento {self.__intentos_fallidos}/3.")
            return False
            
    def desbloquear(self, pin_maestro):
        if pin_maestro == self.__pin_maestro:
            self.__bloqueada = False
            self.__intentos_fallidos = 0
            print("Tarjeta desbloqueada por administrador.")
        else:
            print("PIN Maestro incorrecto.")

    def get_numero(self):
        return self.__numero

class CuentaBancariaATM: # Renombrada para evitar conflicto
    def __init__(self, numero_cuenta, titular, saldo, tarjeta):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__tarjeta = tarjeta # Objeto Tarjeta

    def get_tarjeta(self):
        return self.__tarjeta
        
    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False

    def retirar(self, monto):
        if monto > 0 and self.__saldo >= monto:
            self.__saldo -= monto
            return True
        return False

class CajeroAutomatico:
    def __init__(self):
        self.__cuentas = {} # Diccionario: numero_tarjeta -> objeto CuentaBancaria
        self.__tarjeta_actual = None
        self.__cuenta_actual = None
        self.transacciones = []
        print("Cajero Automático Iniciado.")

    def agregar_cuenta(self, cuenta):
        numero_tarjeta = cuenta.get_tarjeta().get_numero()
        self.__cuentas[numero_tarjeta] = cuenta

    def insertar_tarjeta(self, numero_tarjeta, pin):
        if numero_tarjeta in self.__cuentas:
            tarjeta = self.__cuentas[numero_tarjeta].get_tarjeta()
            if tarjeta.validar_pin(pin):
                self.__tarjeta_actual = tarjeta
                self.__cuenta_actual = self.__cuentas[numero_tarjeta]
                print(f"Acceso concedido. Bienvenido.")
                return True
        else:
            print("Error: Tarjeta no reconocida.")
        
        self.__tarjeta_actual = None
        self.__cuenta_actual = None
        return False

    def expulsar_tarjeta(self):
        self.__tarjeta_actual = None
        self.__cuenta_actual = None
        print("Tarjeta expulsada. Gracias por operar.")

    def _verificar_sesion(self):
        if not self.__cuenta_actual:
            print("Error: Inserte una tarjeta válida primero.")
            return False
        if self.__tarjeta_actual.is_bloqueada():
            print("Error: La tarjeta está bloqueada.")
            return False
        return True

    def realizar_operacion(self, tipo, monto=0):
        if not self._verificar_sesion():
            return

        if tipo == "consulta":
            saldo = self.__cuenta_actual.consultar_saldo()
            print(f"Saldo actual: {saldo}€")
            self.transacciones.append(f"Consulta: Tarjeta {self.__tarjeta_actual.get_numero()}")
        
        elif tipo == "deposito":
            if self.__cuenta_actual.depositar(monto):
                print(f"Depósito exitoso. Nuevo saldo: {self.__cuenta_actual.consultar_saldo()}€")
                self.transacciones.append(f"Deposito: {monto}€ a Tarjeta {self.__tarjeta_actual.get_numero()}")
            else:
                print("Error: Monto de depósito inválido.")
        
        elif tipo == "retiro":
            if self.__cuenta_actual.retirar(monto):
                print(f"Retiro exitoso. Nuevo saldo: {self.__cuenta_actual.consultar_saldo()}€")
                self.transacciones.append(f"Retiro: {monto}€ de Tarjeta {self.__tarjeta_actual.get_numero()}")
            else:
                print("Error: Monto de retiro inválido o fondos insuficientes.")
        
        else:
            print("Error: Operación no válida.")

# --- Pruebas Ejercicio 6 ---
print("\n--- Ejercicio 6: Simulador de ATM ---")
# 1. Crear Tarjetas y Cuentas
t1 = Tarjeta("1111-2222-3333-4444", "1234")
c1 = CuentaBancariaATM("ES01-1000", "Ana", 1000, t1)

t2 = Tarjeta("5555-6666-7777-8888", "9999")
c2 = CuentaBancariaATM("ES02-2000", "Luis", 50, t2)

# 2. Crear ATM y agregar cuentas
atm = CajeroAutomatico()
atm.agregar_cuenta(c1)
atm.agregar_cuenta(c2)

# 3. Simulación 1 (PIN incorrecto 3 veces)
print("\n--- Simulación 1: Tarjeta Bloqueada ---")
atm.insertar_tarjeta("1111-2222-3333-4444", "0000") # Falla 1
atm.insertar_tarjeta("1111-2222-3333-4444", "1111") # Falla 2
atm.insertar_tarjeta("1111-2222-3333-4444", "2222") # Falla 3 (Bloqueada)
atm.insertar_tarjeta("1111-2222-3333-4444", "1234") # Falla (Bloqueada)

# 4. Simulación 2 (Operaciones exitosas)
print("\n--- Simulación 2: Operaciones Válidas ---")
if atm.insertar_tarjeta("5555-6666-7777-8888", "9999"): # Acceso Luis
    atm.realizar_operacion("consulta")
    atm.realizar_operacion("retiro", 100) # Falla (fondos insuficientes)
    atm.realizar_operacion("retiro", 20)
    atm.realizar_operacion("deposito", 300)
    atm.expulsar_tarjeta()

# 5. Desbloqueo de Tarjeta 1
print("\n--- Desbloqueo Admin ---")
t1.desbloquear("9999") # PIN Maestro
if atm.insertar_tarjeta("1111-2222-3333-4444", "1234"): # Acceso Ana
    atm.realizar_operacion("consulta")
    atm.expulsar_tarjeta()

print(f"\nLog de Transacciones del ATM: {atm.transacciones}")


# -----------------------------------------------------------------
# Ejercicio 7: Sistema de Vehículos (Sin Herencia)
# -----------------------------------------------------------------

class Auto:
    def __init__(self, marca, modelo, anio, kilometraje, tipo_combustible, tanque_max=50):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.tipo_combustible = tipo_combustible
        self.__encendido = False
        self.__velocidad_actual = 0
        self.__combustible_actual = 0
        self.__tanque_max = tanque_max

    def encender(self):
        if self.__combustible_actual > 0:
            self.__encendido = True
            print(f"El {self.marca} {self.modelo} está encendido.")
        else:
            print("No se puede encender: tanque vacío.")

    def apagar(self):
        if self.__velocidad_actual == 0:
            self.__encendido = False
            print(f"El {self.marca} {self.modelo} está apagado.")
        else:
            print(f"No se puede apagar en movimiento (Vel: {self.__velocidad_actual} km/h).")

    def acelerar(self, incremento):
        if self.__encendido and self.__combustible_actual > 0:
            self.__velocidad_actual += incremento
            self.__combustible_actual -= (incremento / 10) # Consumo simple
            print(f"Velocidad: {self.__velocidad_actual} km/h")
        elif not self.__encendido:
            print("Debe encender el auto primero.")
        else:
            print("Sin combustible.")

    def frenar(self, decremento):
        self.__velocidad_actual = max(0, self.__velocidad_actual - decremento)
        print(f"Velocidad: {self.__velocidad_actual} km/h")

    def cargar_combustible(self, litros):
        if self.__encendido:
            print("Apague el auto para cargar combustible.")
            return
        
        espacio_disponible = self.__tanque_max - self.__combustible_actual
        if litros > espacio_disponible:
            carga = espacio_disponible
            print(f"Tanque lleno. Se cargaron solo {carga:.2f} litros.")
        else:
            carga = litros
        
        self.__combustible_actual += carga
        print(f"Carga exitosa. Combustible actual: {self.__combustible_actual:.2f} litros.")
        
    def calcular_consumo(self):
        # Simulación: 10 KM por litro
        if self.kilometraje == 0: return 0
        # Esto es solo un ejemplo, la lógica real de consumo es compleja
        return (self.kilometraje / 10) 

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo} ({self.anio}) - KM: {self.kilometraje}"

class Moto:
    # (Similar a Auto, pero con atributos 'cilindrada' y 'tipo_moto')
    def __init__(self, marca, modelo, anio, cilindrada, tipo_moto):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.cilindrada = cilindrada
        self.tipo_moto = tipo_moto
        self.__encendido = False
        self.__velocidad_actual = 0

    def encender(self):
        self.__encendido = True
        print(f"La Moto {self.marca} está encendida.")
    
    def acelerar(self, incremento):
        if self.__encendido:
            self.__velocidad_actual += incremento
            print(f"Velocidad de la moto: {self.__velocidad_actual} km/h")

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo} ({self.cilindrada}cc)"

class Concesionaria:
    def __init__(self):
        self.__inventario_autos = []
        self.__inventario_motos = []

    def agregar_auto(self, auto):
        self.__inventario_autos.append(auto)
    
    def agregar_moto(self, moto):
        self.__inventario_motos.append(moto)

    def vender(self, vehiculo):
        if isinstance(vehiculo, Auto) and vehiculo in self.__inventario_autos:
            self.__inventario_autos.remove(vehiculo)
            print(f"Auto {vehiculo.marca} {vehiculo.modelo} vendido.")
        elif isinstance(vehiculo, Moto) and vehiculo in self.__inventario_motos:
            self.__inventario_motos.remove(vehiculo)
            print(f"Moto {vehiculo.marca} {vehiculo.modelo} vendida.")
        else:
            print("Error: Vehículo no encontrado en inventario.")

    def mostrar_inventario(self):
        print("\n--- Inventario Concesionaria ---")
        print("--- Autos ---")
        for a in self.__inventario_autos: print(f"  - {a}")
        print("--- Motos ---")
        for m in self.__inventario_motos: print(f"  - {m}")

# --- Pruebas Ejercicio 7 ---
print("\n--- Ejercicio 7: Sistema de Vehículos (Composición) ---")
concesionaria = Concesionaria()
auto1 = Auto("Toyota", "Corolla", 2022, 15000, "Gasolina")
auto2 = Auto("Tesla", "Model 3", 2023, 5000, "Eléctrico")
moto1 = Moto("Honda", "CBR", 2021, 600, "Deportiva")

concesionaria.agregar_auto(auto1)
concesionaria.agregar_auto(auto2)
concesionaria.agregar_moto(moto1)

concesionaria.mostrar_inventario()

print("\n--- Prueba de Auto 1 ---")
auto1.cargar_combustible(60) # Carga 50 (máximo)
auto1.encender()
auto1.acelerar(50)
auto1.frenar(20)
auto1.apagar() # Falla (en movimiento)
auto1.frenar(30)
auto1.apagar()

concesionaria.vender(auto1)
concesionaria.mostrar_inventario()


# -----------------------------------------------------------------
# Ejercicio 8: Juego de Cartas (Batalla)
# -----------------------------------------------------------------

class Carta:
    # Usamos diccionarios para mapear valores y palos
    VALORES = {1: "As", 11: "Jota", 12: "Reina", 13: "Rey"}
    PALOS = {"P": "Picas", "C": "Corazones", "T": "Tréboles", "D": "Diamantes"}

    def __init__(self, valor, palo):
        if valor not in range(1, 14) or palo not in self.PALOS:
            raise ValueError("Carta inválida")
        self.valor = valor # 1 (As) a 13 (Rey)
        self.palo = palo   # P, C, T, D

    def __str__(self):
        # Si el valor está en el dict (1, 11, 12, 13), usa el nombre
        nombre_valor = self.VALORES.get(self.valor, str(self.valor))
        return f"{nombre_valor} de {self.PALOS[self.palo]}"

    def comparar(self, otra_carta):
        # Asignamos 14 al As (1) para que sea el más alto
        val1 = 14 if self.valor == 1 else self.valor
        val2 = 14 if otra_carta.valor == 1 else otra_carta.valor
        
        if val1 > val2: return 1
        if val1 < val2: return -1
        return 0 # Empate

class Mazo:
    def __init__(self):
        self.__cartas = []
        self.__crear_mazo()
        self.barajar()

    def __crear_mazo(self):
        """Genera las 52 cartas."""
        self.__cartas = [Carta(v, p) for p in Carta.PALOS for v in range(1, 14)]

    def barajar(self):
        random.shuffle(self.__cartas)
        print("Mazo barajado.")

    def repartir_carta(self):
        if self.cartas_restantes() > 0:
            return self.__cartas.pop()
        return None

    def cartas_restantes(self):
        return len(self.__cartas)

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__cartas_mano = []

    def recibir_carta(self, carta):
        self.__cartas_mano.append(carta)

    def jugar_carta(self):
        if self.contar_cartas() > 0:
            return self.__cartas_mano.pop(0)
        return None

    def contar_cartas(self):
        return len(self.__cartas_mano)

# --- Pruebas Ejercicio 8 ---
print("\n--- Ejercicio 8: Juego de Cartas (Batalla) ---")
# 1. Crear Mazo y Jugadores
mazo = Mazo()
j1 = Jugador("Ana")
j2 = Jugador("Luis")

# 2. Repartir 5 cartas a cada uno
for _ in range(5):
    j1.recibir_carta(mazo.repartir_carta())
    j2.recibir_carta(mazo.repartir_carta())

print(f"Mazo tiene {mazo.cartas_restantes()} cartas.")
print(f"{j1.nombre} tiene {j1.contar_cartas()} cartas.")

# 3. Jugar una ronda de Batalla
print("\n--- ¡Batalla! (Ronda 1) ---")
carta_j1 = j1.jugar_carta()
carta_j2 = j2.jugar_carta()

print(f"  {j1.nombre} juega: {carta_j1}")
print(f"  {j2.nombre} juega: {carta_j2}")

comparacion = carta_j1.comparar(carta_j2)
if comparacion > 0:
    print(f"  Gana {j1.nombre} esta ronda.")
elif comparacion < 0:
    print(f"  Gana {j2.nombre} esta ronda.")
else:
    print("  ¡Empate en esta ronda!")

print(f"{j1.nombre} tiene {j1.contar_cartas()} cartas.")


# -----------------------------------------------------------------
# Ejercicio 9: Sistema de Citas Médicas
# -----------------------------------------------------------------

class Paciente:
    def __init__(self, nombre, edad, numero_seguro):
        self.nombre = nombre
        self.edad = edad
        self.numero_seguro = numero_seguro
        self.__historial_citas = []

    def agregar_cita_historial(self, cita):
        self.__historial_citas.append(cita)
        
    def __str__(self):
        return f"Paciente: {self.nombre} (Seguro: {self.numero_seguro})"

class Doctor:
    def __init__(self, nombre, especialidad, horario_disponible):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario_disponible = horario_disponible # Ej: ["09:00", "10:00", "11:00"]
        self.__citas_programadas = {} # Ej: {"2025-12-01": ["09:00"]}

    def verificar_disponibilidad(self, fecha, hora):
        if hora not in self.horario_disponible:
            return False # No trabaja a esa hora
        if fecha in self.__citas_programadas:
            if hora in self.__citas_programadas[fecha]:
                return False # Hora ocupada
        return True # Disponible

    def agendar_hora(self, fecha, hora):
        if fecha not in self.__citas_programadas:
            self.__citas_programadas[fecha] = []
        self.__citas_programadas[fecha].append(hora)

    def cancelar_hora(self, fecha, hora):
        if fecha in self.__citas_programadas and hora in self.__citas_programadas[fecha]:
            self.__citas_programadas[fecha].remove(hora)

    def __str__(self):
        return f"Dr. {self.nombre} (Especialidad: {self.especialidad})"

class Cita:
    def __init__(self, paciente, doctor, fecha, hora, motivo):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = "Confirmada" # "Cancelada", "Completada"

    def cancelar(self):
        self.estado = "Cancelada"
        # (Aquí también se liberaría la hora en el doctor)

    def completar(self):
        self.estado = "Completada"

    def __str__(self):
        return f"Cita: {self.fecha} @ {self.hora} - {self.paciente.nombre} con {self.doctor.nombre} ({self.estado})"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__doctores = []
        self.__pacientes = []
        self.__citas = []

    def agregar_doctor(self, doctor):
        self.__doctores.append(doctor)
    
    def agregar_paciente(self, paciente):
        self.__pacientes.append(paciente)

    def agendar_cita(self, paciente, doctor, fecha, hora, motivo):
        print(f"\nIntentando agendar cita para {paciente.nombre} con {doctor.nombre}...")
        if doctor.verificar_disponibilidad(fecha, hora):
            nueva_cita = Cita(paciente, doctor, fecha, hora, motivo)
            doctor.agendar_hora(fecha, hora)
            paciente.agregar_cita_historial(nueva_cita)
            self.__citas.append(nueva_cita)
            print(f"Éxito: {nueva_cita}")
            return nueva_cita
        else:
            print(f"Error: Dr. {doctor.nombre} no disponible el {fecha} a las {hora}.")
            return None

    def cancelar_cita(self, cita):
        cita.cancelar()
        cita.doctor.cancelar_hora(cita.fecha, cita.hora)
        print(f"Cita cancelada: {cita}")

    def citas_del_dia(self, fecha):
        print(f"\n--- Citas para el día {fecha} ---")
        citas_dia = [c for c in self.__citas if c.fecha == fecha and c.estado == "Confirmada"]
        if not citas_dia:
            print(" (No hay citas confirmadas para este día)")
            return
        for c in sorted(citas_dia, key=lambda x: x.hora):
            print(f"  - {c.hora}: {c.paciente.nombre} con {c.doctor.nombre}")
            
    def buscar_doctor_por_especialidad(self, especialidad):
        return [d for d in self.__doctores if d.especialidad.lower() == especialidad.lower()]

# --- Pruebas Ejercicio 9 ---
print("\n--- Ejercicio 9: Sistema de Citas Médicas ---")
# 1. Crear Hospital, Doctores y Pacientes
hospital = Hospital("Hospital Central")
p1 = Paciente("Ana Soto", 30, "SEG123")
p2 = Paciente("Luis Vera", 45, "SEG456")

d_cardio = Doctor("Perez", "Cardiología", ["09:00", "10:00", "11:00"])
d_derma = Doctor("Gomez", "Dermatología", ["10:00", "11:00", "14:00"])
hospital.agregar_doctor(d_cardio)
hospital.agregar_doctor(d_derma)
hospital.agregar_paciente(p1)
hospital.agregar_paciente(p2)

# 2. Agendar Citas
fecha_cita = "2025-12-10"
cita1 = hospital.agendar_cita(p1, d_cardio, fecha_cita, "10:00", "Chequeo Anual")
cita2 = hospital.agendar_cita(p2, d_derma, fecha_cita, "10:00", "Revisión lunar")
cita3 = hospital.agendar_cita(p1, d_derma, fecha_cita, "10:00", "Falla (hora ocupada)")

# 3. Reporte y Cancelación
hospital.citas_del_dia(fecha_cita)
if cita2:
    hospital.cancelar_cita(cita2)
hospital.citas_del_dia(fecha_cita)

# 4. Buscar Doctores
print("\n--- Búsqueda de Doctores ---")
doctores_cardio = hospital.buscar_doctor_por_especialidad("Cardiología")
for d in doctores_cardio:
    print(f"  - {d}")


# -----------------------------------------------------------------
# Ejercicio 10: Sistema de Restaurante Completo
# -----------------------------------------------------------------

class Platillo:
    def __init__(self, nombre, precio, categoria, tiempo_preparacion, disponible=True):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.tiempo_preparacion = tiempo_preparacion # en minutos
        self.disponible = disponible
    
    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - {self.precio}€"

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
        self.__pedido_actual = [] # Lista de (Platillo, cantidad)
        self.total_pagado = 0.0

    def ocupar(self):
        self.ocupada = True
        
    def liberar(self):
        self.ocupada = False
        self.__pedido_actual = []
        # El total_pagado se resetea al asignar mesa

    def agregar_platillo(self, platillo, cantidad):
        if self.ocupada:
            self.__pedido_actual.append((platillo, cantidad))
            print(f"Mesa {self.numero}: Añadido {cantidad}x {platillo.nombre}")
        else:
            print("Error: La mesa no está ocupada.")

    def calcular_total(self):
        return sum(p.precio * cant for p, cant in self.__pedido_actual)

    def generar_ticket(self, propina_pct=0):
        print(f"\n--- TICKET Mesa {self.numero} ---")
        for p, cant in self.__pedido_actual:
            print(f"  {cant}x {p.nombre:<15} {p.precio * cant:>6.2f}€")
        print("-" * 30)
        subtotal = self.calcular_total()
        propina = subtotal * (propina_pct / 100)
        total = subtotal + propina
        print(f"  Subtotal: {subtotal:>19.2f}€")
        if propina > 0:
            print(f"  Propina ({propina_pct}%): {propina:>15.2f}€")
        print(f"  TOTAL: {total:>22.2f}€")
        print("-" * 30)
        self.total_pagado += total
        return total

class Mesero:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.__mesas_asignadas = [] # Lista de objetos Mesa

    def asignar_mesa(self, mesa):
        self.__mesas_asignadas.append(mesa)

    def calcular_total_ventas(self):
        # Calcula el total de ventas de las mesas CERRADAS
        return sum(m.total_pagado for m in self.__mesas_asignadas)

class Restaurante:
    def __init__(self):
        self.__menu = []
        self.__mesas = []
        self.__meseros = []
        self.ventas_del_dia = 0.0

    def agregar_platillo(self, platillo):
        self.__menu.append(platillo)
    
    def agregar_mesa(self, mesa):
        self.__mesas.append(mesa)
        
    def agregar_mesero(self, mesero):
        self.__meseros.append(mesero)

    def mostrar_menu_por_categoria(self, categoria):
        print(f"\n--- Menú (Categoría: {categoria}) ---")
        for p in self.__menu:
            if p.categoria.lower() == categoria.lower() and p.disponible:
                print(f"  - {p}")

    def asignar_mesa(self, numero_personas, mesero):
        for m in self.__mesas:
            if not m.ocupada and m.capacidad >= numero_personas:
                m.ocupar()
                mesero.asignar_mesa(m)
                print(f"Mesa {m.numero} asignada a {mesero.nombre} para {numero_personas} personas.")
                return m
        print("Error: No hay mesas disponibles para esa capacidad.")
        return None

    def tomar_pedido(self, numero_mesa, platillo_nombre, cantidad):
        mesa = next((m for m in self.__mesas if m.numero == numero_mesa), None)
        platillo = next((p for p in self.__menu if p.nombre.lower() == platillo_nombre.lower()), None)

        if not mesa or not mesa.ocupada:
            print(f"Error: Mesa {numero_mesa} no está ocupada.")
            return
        if not platillo or not platillo.disponible:
            print(f"Error: Platillo '{platillo_nombre}' no disponible.")
            return
            
        mesa.agregar_platillo(platillo, cantidad)

    def cerrar_cuenta(self, numero_mesa, propina_pct=10):
        mesa = next((m for m in self.__mesas if m.numero == numero_mesa), None)
        if mesa and mesa.ocupada:
            total_pagado = mesa.generar_ticket(propina_pct)
            self.ventas_del_dia += total_pagado
            mesa.liberar() # Libera la mesa y resetea el pedido
            print(f"Mesa {numero_mesa} cerrada. Total pagado: {total_pagado:.2f}€")
        else:
            print(f"Error: No se puede cerrar la cuenta de la mesa {numero_mesa}.")

    def reporte_ventas_del_dia(self):
        print("\n--- Reporte de Ventas del Día ---")
        print(f"Ingresos Totales (con propina): {self.ventas_del_dia:.2f}€")
        print("\nVentas por Mesero:")
        for m in self.__meseros:
            print(f"  - {m.nombre}: {m.calcular_total_ventas():.2f}€")

# --- Pruebas Ejercicio 10 ---
print("\n--- Ejercicio 10: Sistema de Restaurante ---")
# 1. Crear Restaurante y Staff
rest = Restaurante()
mesero1 = Mesero("Javier", "E01")
rest.agregar_mesero(mesero1)

# 2. Añadir Mesas y Menú
rest.agregar_mesa(Mesa(1, 4))
rest.agregar_mesa(Mesa(2, 2))
rest.agregar_mesa(Mesa(3, 6))

rest.agregar_platillo(Platillo("Solomillo", 25.0, "Principal", 20))
rest.agregar_platillo(Platillo("Ensalada César", 12.0, "Entrante", 10))
rest.agregar_platillo(Platillo("Tarta de Queso", 8.0, "Postre", 5))
rest.agregar_platillo(Platillo("Vino Tinto", 18.0, "Bebida", 2))

# 3. Simulación de servicio
rest.mostrar_menu_por_categoria("entrante")

print("\n--- Servicio ---")
mesa1 = rest.asignar_mesa(3, mesero1) # Asigna Mesa 1
mesa2 = rest.asignar_mesa(2, mesero1) # Asigna Mesa 2

rest.tomar_pedido(1, "Solomillo", 2)
rest.tomar_pedido(1, "Vino Tinto", 1)
rest.tomar_pedido(2, "Ensalada César", 2)

rest.cerrar_cuenta(1, propina_pct=15)
rest.cerrar_cuenta(2, propina_pct=0) # Sin propina

# 4. Reporte Final
rest.reporte_ventas_del_dia()