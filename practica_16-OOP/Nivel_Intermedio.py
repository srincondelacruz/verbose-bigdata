# --- Nivel_Intermedio.py ---
# Soluciones completas a los 10 ejercicios

import math

# -----------------------------------------------------------------
# Ejercicio 1: Sistema de Gestión de Empleados
# -----------------------------------------------------------------

class EmpleadoEmpresa:
    """
    Gestiona empleados de la empresa, validando salarios mínimos
    y rastreando el total de empleados.
    """
    # Variables de clase
    total_empleados = 0
    salario_minimo = 1000
    empresa = "TechCorp"

    def __init__(self, nombre, edad, salario, departamento, anos_experiencia):
        self.nombre = nombre
        self.edad = edad
        
        # 1. Validación de salario (usando max() para limpieza)
        self.salario = max(salario, EmpleadoEmpresa.salario_minimo)
        
        self.departamento = departamento
        self.anos_experiencia = anos_experiencia
        
        # Incrementar el contador de clase
        EmpleadoEmpresa.total_empleados += 1

    def aumentar_salario(self, porcentaje):
        """Aumenta el salario del empleado en un porcentaje dado."""
        aumento = 1 + (porcentaje / 100)
        self.salario = round(self.salario * aumento, 2)

    def cambiar_departamento(self, nuevo_depto):
        """Asigna un nuevo departamento al empleado."""
        self.departamento = nuevo_depto

    def cumplir_anos(self):
        """Incrementa la edad y los años de experiencia en 1."""
        self.edad += 1
        self.anos_experiencia += 1

    def calcular_salario_anual(self):
        """Retorna el salario anual (salario * 12)."""
        return self.salario * 12

    def es_senior(self):
        """Retorna True si tiene más de 5 años de experiencia."""
        return self.anos_experiencia > 5

    def get_info_completa(self):
        """Retorna un string formateado con toda la información."""
        info = (
            f"--- Ficha de Empleado ---\n"
            f"\tNombre: {self.nombre} (Edad: {self.edad})\n"
            f"\tEmpresa: {EmpleadoEmpresa.empresa}\n"
            f"\tDepartamento: {self.departamento}\n"
            f"\tSalario: {self.salario} € (Anual: {self.calcular_salario_anual()} €)\n"
            f"\tAntigüedad: {self.anos_experiencia} años (Senior: {self.es_senior()})\n"
            f"--------------------------"
        )
        return info

    def __str__(self):
        """Representación corta del objeto."""
        return f"Empleado({self.nombre}, Dept: {self.departamento})"

    @classmethod
    def empleados_registrados(cls):
        """Retorna el contador total de empleados."""
        return cls.total_empleados

    @classmethod
    def actualizar_salario_minimo(cls, nuevo_minimo):
        """Actualiza la variable de clase salario_minimo."""
        cls.salario_minimo = nuevo_minimo

# --- Pruebas Ejercicio 1 ---
print("\n--- Ejercicio 1: EmpleadoEmpresa ---")
emp1 = EmpleadoEmpresa("Ana", 30, 900, "Ventas", 2) # Prueba de salario mínimo
emp2 = EmpleadoEmpresa("Luis", 45, 5000, "IT", 8)
emp3 = EmpleadoEmpresa("Sara", 28, 2000, "Marketing", 3)

print(f"Salario inicial de Ana (validado): {emp1.salario}") # Debería ser 1000

emp2.aumentar_salario(10) # Aumento del 10%
print(f"Salario de Luis (con aumento): {emp2.salario}") # Debería ser 5500

emp3.cumplir_anos()
print(f"Edad de Sara (actualizada): {emp3.edad}") # Debería ser 29

print(f"¿Luis es senior? {emp2.es_senior()}") # Debería ser True
print(f"¿Ana es senior? {emp1.es_senior()}") # Debería ser False

print(f"Total de empleados inicial: {EmpleadoEmpresa.empleados_registrados()}") # Debería ser 3

EmpleadoEmpresa.actualizar_salario_minimo(1200)
emp4 = EmpleadoEmpresa("Juan", 22, 1100, "Ventas", 1)
print(f"Salario de Juan (nuevo mínimo): {emp4.salario}") # Debería ser 1200
print(f"Total de empleados final: {EmpleadoEmpresa.empleados_registrados()}") # Debería ser 4
print(emp2.get_info_completa())


# -----------------------------------------------------------------
# Ejercicio 2: Sistema de Inventario de Tienda
# -----------------------------------------------------------------

class Articulo:
    contador_articulos = 0
    iva = 0.21

    def __init__(self, nombre, precio, stock_inicial, categoria):
        Articulo.contador_articulos += 1
        # Genera código automático con ceros a la izquierda (ej. ART001)
        self.codigo = f"ART{Articulo.contador_articulos:03d}"
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} de {self.nombre}.")
            return True
        else:
            print(f"Venta fallida: Stock insuficiente de {self.nombre} (Stock: {self.stock}).")
            return False

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Reabastecido: {cantidad} de {self.nombre}. Nuevo stock: {self.stock}")

    def calcular_valor_inventario(self):
        return self.precio * self.stock

    def calcular_precio_con_iva(self):
        return round(self.precio * (1 + self.iva), 2)

    def aplicar_descuento(self, porcentaje):
        descuento = 1 - (porcentaje / 100)
        self.precio = round(self.precio * descuento, 2)
        print(f"Nuevo precio de {self.nombre}: {self.precio}")

    def necesita_reabastecimiento(self):
        return self.stock < 5

    def obtener_info(self):
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - Precio: {self.precio}€ - Stock: {self.stock}"

    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        cls.iva = nuevo_iva
        print(f"IVA actualizado a: {cls.iva * 100}%")

    @classmethod
    def total_articulos(cls):
        return cls.contador_articulos

# --- Pruebas Ejercicio 2 ---
print("\n--- Ejercicio 2: Inventario de Tienda ---")
# 1. Crear inventario (8 artículos)
inventario = [
    Articulo("Teclado", 80, 10, "Periféricos"),
    Articulo("Ratón", 30, 15, "Periféricos"),
    Articulo("Monitor", 250, 4, "Monitores"), # (Necesita reabastecer)
    Articulo("SSD 1TB", 120, 8, "Almacenamiento"),
    Articulo("Webcam", 50, 0, "Periféricos"), # (Sin stock)
    Articulo("Silla Gamer", 180, 3, "Muebles"), # (Necesita reabastecer)
    Articulo("Laptop", 1200, 2, "Computadoras"), # (Necesita reabastecer)
    Articulo("Cable HDMI", 15, 30, "Accesorios")
]

# 2. Simular ventas
print("\n--- Simulación de Ventas ---")
inventario[0].vender(2)  # Venta Teclado (éxito)
inventario[4].vender(1)  # Venta Webcam (falla)
inventario[2].vender(5)  # Venta Monitor (falla)

# 3. Realizar reabastecimientos
print("\n--- Reabastecimiento ---")
inventario[2].reabastecer(10) # Reabastecer Monitor
inventario[2].vender(5)       # Venta Monitor (éxito)

# 4. Reporte Final
print("\n--- Reporte Final del Inventario ---")
valor_total_inventario = 0

print("Artículos que necesitan reabastecimiento (Stock < 5):")
for item in inventario:
    if item.necesita_reabastecimiento():
        print(f"\t- {item.obtener_info()}")
    valor_total_inventario += item.calcular_valor_inventario()

print(f"\nValor total del inventario: {valor_total_inventario} €")
print(f"Total de artículos (tipos) en el sistema: {Articulo.total_articulos()}")


# -----------------------------------------------------------------
# Ejercicio 3: Gestión de Cursos Universitarios
# -----------------------------------------------------------------

class Curso:
    total_cursos = 0
    universidad = "Universidad Nacional"

    def __init__(self, nombre_curso, codigo_curso, creditos, capacidad_maxima, profesor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.creditos = creditos
        self.estudiantes_inscritos = []
        self.capacidad_maxima = capacidad_maxima
        self.profesor = profesor
        Curso.total_cursos += 1

    def inscribir_estudiante(self, nombre_estudiante):
        if not self.esta_lleno():
            self.estudiantes_inscritos.append(nombre_estudiante)
            return f"Éxito: {nombre_estudiante} inscrito en {self.nombre_curso}."
        else:
            return f"Error: {self.nombre_curso} está lleno (Capacidad: {self.capacidad_maxima})."

    def retirar_estudiante(self, nombre_estudiante):
        if nombre_estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(nombre_estudiante)
            print(f"{nombre_estudiante} retirado de {self.nombre_curso}.")
        else:
            print(f"Error: {nombre_estudiante} no estaba inscrito.")

    def obtener_cantidad_inscritos(self):
        return len(self.estudiantes_inscritos)

    def esta_lleno(self):
        return self.obtener_cantidad_inscritos() >= self.capacidad_maxima

    def obtener_cupos_disponibles(self):
        return self.capacidad_maxima - self.obtener_cantidad_inscritos()

    def listar_estudiantes(self):
        print(f"--- Lista de Estudiantes: {self.nombre_curso} ---")
        if not self.estudiantes_inscritos:
            print(" (No hay estudiantes inscritos)")
            return
        for i, estudiante in enumerate(self.estudiantes_inscritos, 1):
            print(f"  {i}. {estudiante}")

    def calcular_porcentaje_ocupacion(self):
        if self.capacidad_maxima == 0:
            return 0.0
        return (self.obtener_cantidad_inscritos() / self.capacidad_maxima) * 100

    def cambiar_profesor(self, nuevo_profesor):
        self.profesor = nuevo_profesor

    @classmethod
    def total_cursos_activos(cls):
        return cls.total_cursos

    @classmethod
    def cambiar_universidad(cls, nueva_uni):
        cls.universidad = nueva_uni

# --- Pruebas Ejercicio 3 ---
print("\n--- Ejercicio 3: Gestión de Cursos ---")
# 1. Crear 4 cursos
curso_python = Curso("Python Avanzado", "PY101", 4, 3, "Dr. Guido")
curso_ia = Curso("Inteligencia Artificial", "IA201", 5, 20, "Dra. Ng")
curso_bd = Curso("Bases de Datos", "BD301", 3, 25, "Prof. Codd")
curso_web = Curso("Desarrollo Web", "WEB401", 4, 2, "Prof. Berners-Lee")

# 2. Inscribir estudiantes (incluyendo intentos cuando está lleno)
print("\n--- Inscripciones ---")
print(curso_python.inscribir_estudiante("Ana"))
print(curso_python.inscribir_estudiante("Luis"))
print(curso_python.inscribir_estudiante("Sara"))
print(curso_python.inscribir_estudiante("Juan")) # Debe fallar (curso lleno)

print(curso_web.inscribir_estudiante("Maria"))
print(curso_web.inscribir_estudiante("Carlos"))

# 3. Retirar estudiantes
print("\n--- Retiros ---")
curso_python.retirar_estudiante("Luis")
curso_python.retirar_estudiante("Pedro") # Debe fallar (no inscrito)

# 4. Reporte de Ocupación
print("\n--- Reporte Final de Ocupación ---")
print(f"Universidad: {Curso.universidad}")
print(f"Total de Cursos Activos: {Curso.total_cursos_activos()}\n")

cursos = [curso_python, curso_ia, curso_bd, curso_web]
for curso in cursos:
    print(f"Curso: {curso.nombre_curso} ({curso.codigo_curso})")
    print(f"  Profesor: {curso.profesor}")
    print(f"  Ocupación: {curso.calcular_porcentaje_ocupacion():.1f}% ({curso.obtener_cantidad_inscritos()}/{curso.capacidad_maxima})")
    curso.listar_estudiantes()
    print("-" * 20)


# -----------------------------------------------------------------
# Ejercicio 4: Sistema de Cuentas Bancarias con Historial
# -----------------------------------------------------------------

class CuentaBancaria:
    contador_cuentas = 1000000000
    tasa_interes_mensual = 0.005
    comision_retiro = 2.50

    def __init__(self, titular, saldo_inicial):
        CuentaBancaria.contador_cuentas += 1
        self.numero_cuenta = CuentaBancaria.contador_cuentas
        self.titular = titular
        self.saldo = 0 # El saldo se actualiza con el depósito inicial
        self.transacciones = []
        
        # Registra el depósito inicial
        self.depositar(saldo_inicial, es_inicial=True)

    def _registrar_transaccion(self, tipo, monto, saldo_resultante):
        transaccion = {
            "tipo": tipo,
            "monto": monto,
            "saldo_resultante": saldo_resultante
        }
        self.transacciones.append(transaccion)

    def depositar(self, monto, es_inicial=False):
        self.saldo += monto
        tipo_transaccion = "Depósito Inicial" if es_inicial else "Depósito"
        self._registrar_transaccion(tipo_transaccion, monto, self.saldo)
        print(f"[{self.numero_cuenta}] {tipo_transaccion}: {monto}€. Saldo nuevo: {self.saldo}€")

    def retirar(self, monto):
        monto_total_retiro = monto + self.comision_retiro
        if self.saldo >= monto_total_retiro:
            self.saldo -= monto_total_retiro
            self._registrar_transaccion("Retiro", monto, self.saldo)
            print(f"[{self.numero_cuenta}] Retiro: {monto}€ (Comisión: {self.comision_retiro}€). Saldo nuevo: {self.saldo}€")
            return True
        else:
            print(f"[{self.numero_cuenta}] Retiro fallido: Saldo insuficiente (Saldo: {self.saldo}€, Intento: {monto_total_retiro}€)")
            return False

    def transferir(self, cuenta_destino, monto):
        print(f"--- Iniciando Transferencia de {self.numero_cuenta} a {cuenta_destino.numero_cuenta} ---")
        if self.retirar(monto): # El retiro ya incluye la comisión
            cuenta_destino.depositar(monto)
            print(f"Transferencia completada.")
        else:
            print(f"Transferencia fallida.")

    def aplicar_intereses(self):
        intereses = self.saldo * self.tasa_interes_mensual
        if intereses > 0:
            self.saldo += intereses
            self._registrar_transaccion("Intereses", round(intereses, 2), self.saldo)
            print(f"[{self.numero_cuenta}] Intereses aplicados: {intereses:.2f}€. Saldo nuevo: {self.saldo:.2f}€")

    def mostrar_historial(self):
        print(f"\n--- Historial de Cuenta: {self.numero_cuenta} (Titular: {self.titular}) ---")
        for trans in self.transacciones:
            print(f"  Tipo: {trans['tipo']:<18} | Monto: {trans['monto']:>8.2f}€ | Saldo: {trans['saldo_resultante']:>10.2f}€")
        print(f"--- Saldo Final: {self.saldo:.2f}€ ---")

    def obtener_saldo(self):
        return self.saldo

    def contar_transacciones(self):
        return len(self.transacciones)

    def calcular_total_depositado(self):
        total = 0
        for trans in self.transacciones:
            if trans['tipo'] == 'Depósito' or trans['tipo'] == 'Depósito Inicial':
                total += trans['monto']
        return total

    @classmethod
    def obtener_total_cuentas(cls):
        return cls.contador_cuentas - 1000000000

# --- Pruebas Ejercicio 4 ---
print("\n--- Ejercicio 4: Cuentas Bancarias ---")
# 1. Crear cuentas
cuenta_ana = CuentaBancaria("Ana Garcia", 500)
cuenta_luis = CuentaBancaria("Luis Torres", 2000)
cuenta_sara = CuentaBancaria("Sara Mota", 100)

# 2. Realizar operaciones
print("\n--- Operaciones ---")
cuenta_ana.depositar(300)
cuenta_luis.retirar(500)
cuenta_sara.retirar(100) # Debe fallar (saldo insuficiente para comisión)

# 3. Transferencia
cuenta_luis.transferir(cuenta_ana, 300)

# 4. Aplicar intereses
cuenta_ana.aplicar_intereses()
cuenta_luis.aplicar_intereses()
cuenta_sara.aplicar_intereses()

# 5. Mostrar historiales
cuenta_ana.mostrar_historial()
cuenta_luis.mostrar_historial()
cuenta_sara.mostrar_historial()

print(f"\nTotal de cuentas creadas: {CuentaBancaria.obtener_total_cuentas()}")


# -----------------------------------------------------------------
# Ejercicio 5: Sistema de Gestión de Proyectos
# -----------------------------------------------------------------

class Proyecto:
    total_proyectos = 0
    estados_validos = ["Planificación", "En Progreso", "Completado", "Cancelado"]

    def __init__(self, nombre_proyecto, fecha_inicio, presupuesto):
        self.nombre_proyecto = nombre_proyecto
        self.fecha_inicio = fecha_inicio
        self.presupuesto = presupuesto
        self.gastos = []
        self.estado = "Planificación"
        self.miembros_equipo = []
        Proyecto.total_proyectos += 1

    def calcular_gastos_totales(self):
        total = 0
        for gasto in self.gastos:
            total += gasto['monto']
        return total

    def calcular_presupuesto_restante(self):
        return self.presupuesto - self.calcular_gastos_totales()

    def registrar_gasto(self, concepto, monto):
        if monto <= self.calcular_presupuesto_restante():
            self.gastos.append({"concepto": concepto, "monto": monto})
            print(f"[{self.nombre_proyecto}] Gasto registrado: {concepto} - {monto}€")
            return True
        else:
            print(f"[{self.nombre_proyecto}] Error: Gasto '{concepto}' ({monto}€) excede el presupuesto restante ({self.calcular_presupuesto_restante()}€).")
            return False

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_validos:
            self.estado = nuevo_estado
            print(f"[{self.nombre_proyecto}] Estado actualizado a: {nuevo_estado}")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado válido.")

    def agregar_miembro(self, nombre):
        if nombre not in self.miembros_equipo:
            self.miembros_equipo.append(nombre)
        
    def remover_miembro(self, nombre):
        if nombre in self.miembros_equipo:
            self.miembros_equipo.remove(nombre)

    def obtener_porcentaje_gastado(self):
        if self.presupuesto == 0:
            return 0.0
        return (self.calcular_gastos_totales() / self.presupuesto) * 100

    def esta_sobre_presupuesto(self):
        return self.calcular_gastos_totales() > self.presupuesto

    def obtener_gasto_mayor(self):
        if not self.gastos:
            return None
        return max(self.gastos, key=lambda gasto: gasto['monto'])

    def generar_reporte(self):
        print(f"\n--- Reporte del Proyecto: {self.nombre_proyecto} ---")
        print(f"  Estado: {self.estado} (Iniciado: {self.fecha_inicio})")
        print(f"  Equipo: {', '.join(self.miembros_equipo) if self.miembros_equipo else 'Sin asignar'}")
        print(f"  Presupuesto: {self.presupuesto}€")
        print(f"  Gastos Totales: {self.calcular_gastos_totales()}€")
        print(f"  Presupuesto Restante: {self.calcular_presupuesto_restante()}€")
        print(f"  % Gastado: {self.obtener_porcentaje_gastado():.1f}%")
        if self.esta_sobre_presupuesto():
            print("  (!) ALERTA: Proyecto sobre-presupuestado.")
        gasto_mayor = self.obtener_gasto_mayor()
        if gasto_mayor:
            print(f"  Gasto Mayor: {gasto_mayor['concepto']} ({gasto_mayor['monto']}€)")
        print("-" * 30)

    @classmethod
    def proyectos_activos(cls):
        return cls.total_proyectos

# --- Pruebas Ejercicio 5 ---
print("\n--- Ejercicio 5: Gestión de Proyectos ---")
# 1. Crear proyectos
proy_web = Proyecto("App E-commerce", "01-01-2025", 50000)
proy_ia = Proyecto("Modelo IA", "15-02-2025", 120000)
proy_migracion = Proyecto("Migración Cloud", "01-03-2025", 30000)

# 2. Asignar equipos y cambiar estados
proy_web.agregar_miembro("Ana")
proy_web.agregar_miembro("Luis")
proy_web.cambiar_estado("En Progreso")

proy_ia.agregar_miembro("Sara")
proy_ia.cambiar_estado("En Progreso")

# 3. Registrar gastos
proy_web.registrar_gasto("Servidores", 15000)
proy_web.registrar_gasto("Licencias", 5000)
proy_web.registrar_gasto("Marketing", 40000) # Debe fallar (excede)

proy_ia.registrar_gasto("GPUs", 80000)
proy_ia.registrar_gasto("Personal", 50000) # Debe fallar (excede)

proy_migracion.registrar_gasto("Consultoría", 35000) # Falla y sobre-presupuesta
proy_migracion.cambiar_estado("Cancelado")

# 4. Generar reportes
print("\n--- Reportes Finales de Proyectos ---")
proyectos = [proy_web, proy_ia, proy_migracion]
for p in proyectos:
    p.generar_reporte()

print(f"\nTotal de proyectos en el sistema: {Proyecto.proyectos_activos()}")


# -----------------------------------------------------------------
# Ejercicio 6: Sistema de Biblioteca con Control de Préstamos
# -----------------------------------------------------------------

class Libro:
    biblioteca_nombre = "Biblioteca Municipal"
    dias_prestamo_maximo = 14
    total_libros = 0
    libros_prestados_actualmente = 0

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.usuario_actual = None
        self.veces_prestado = 0
        self.prestamos_historico = []
        Libro.total_libros += 1

    def prestar(self, nombre_usuario):
        if self.disponible:
            self.disponible = False
            self.usuario_actual = nombre_usuario
            self.veces_prestado += 1
            Libro.libros_prestados_actualmente += 1
            # Simulación simple de fecha
            self.prestamos_historico.append({"usuario": nombre_usuario, "fecha_prestamo": "HOY", "fecha_devolucion": None})
            print(f"'{self.titulo}' prestado a {nombre_usuario}.")
            return True
        else:
            print(f"Error: '{self.titulo}' ya está prestado a {self.usuario_actual}.")
            return False

    def devolver(self):
        if not self.disponible:
            print(f"'{self.titulo}' devuelto por {self.usuario_actual}.")
            self.disponible = True
            self.usuario_actual = None
            Libro.libros_prestados_actualmente -= 1
            # Actualizar historial
            if self.prestamos_historico:
                self.prestamos_historico[-1]["fecha_devolucion"] = "HOY"
            return True
        else:
            print(f"Error: '{self.titulo}' ya estaba disponible.")
            return False

    def esta_disponible(self):
        return self.disponible

    def obtener_info_prestamo(self):
        if self.disponible:
            return f"'{self.titulo}' está DISPONIBLE."
        else:
            return f"'{self.titulo}' está PRESTADO a {self.usuario_actual}."

    def es_popular(self):
        return self.veces_prestado > 5

    def obtener_historial(self):
        print(f"\n--- Historial de '{self.titulo}' (Prestado {self.veces_prestado} veces) ---")
        for p in self.prestamos_historico:
            print(f"  Usuario: {p['usuario']}, Devolución: {p['fecha_devolucion']}")

    @classmethod
    def libros_en_prestamo(cls):
        return cls.libros_prestados_actualmente

    @classmethod
    def cambiar_dias_prestamo(cls, nuevos_dias):
        cls.dias_prestamo_maximo = nuevos_dias

    @classmethod
    def porcentaje_prestados(cls):
        if cls.total_libros == 0:
            return 0.0
        return (cls.libros_prestados_actualmente / cls.total_libros) * 100

# --- Pruebas Ejercicio 6 ---
print("\n--- Ejercicio 6: Biblioteca ---")
# 1. Crear libros
libros = [
    Libro("Cien Años de Soledad", "García Márquez", "111-111"),
    Libro("El Quijote", "Cervantes", "222-222"),
    Libro("Python para Dummies", "A. Coder", "333-333"),
]
# Simulamos un libro popular
libros[0].veces_prestado = 6 

# 2. Simular préstamos
print("\n--- Préstamos ---")
libros[0].prestar("Ana")
libros[1].prestar("Luis")
libros[1].prestar("Sara") # Falla

# 3. Simular devoluciones
print("\n--- Devoluciones ---")
libros[0].devolver()
libros[0].devolver() # Falla

# 4. Reporte Final
print("\n--- Reporte Final de Biblioteca ---")
print(f"Biblioteca: {Libro.biblioteca_nombre}")
print(f"Libros actualmente prestados: {Libro.libros_en_prestamo()}")
print(f"Porcentaje de ocupación: {Libro.porcentaje_prestados():.1f}%")

print("\nLibros Populares (más de 5 préstamos):")
for libro in libros:
    if libro.es_popular():
        print(f"  - {libro.titulo} ({libro.veces_prestado} préstamos)")

libros[1].obtener_historial()


# -----------------------------------------------------------------
# Ejercicio 7: Sistema de Calificaciones de Estudiantes
# -----------------------------------------------------------------

class Estudiante:
    contador_matriculas = 2024000
    calificacion_minima_aprobatoria = 6.0
    total_estudiantes = 0

    def __init__(self, nombre, semestre):
        Estudiante.contador_matriculas += 1
        Estudiante.total_estudiantes += 1
        self.nombre = nombre
        self.matricula = str(Estudiante.contador_matriculas)
        self.calificaciones = {}
        self.semestre = semestre

    def agregar_materia(self, nombre_materia):
        if nombre_materia not in self.calificaciones:
            self.calificaciones[nombre_materia] = []

    def registrar_calificacion(self, materia, calificacion):
        if materia in self.calificaciones:
            if 0 <= calificacion <= 10:
                self.calificaciones[materia].append(calificacion)
            else:
                print(f"Error: Calificación {calificacion} fuera de rango (0-10).")
        else:
            print(f"Error: Materia {materia} no registrada para {self.nombre}.")

    def _calcular_promedio(self, lista_notas):
        if not lista_notas:
            return 0.0
        return sum(lista_notas) / len(lista_notas)

    def calcular_promedio_materia(self, materia):
        if materia in self.calificaciones:
            return self._calcular_promedio(self.calificaciones[materia])
        return 0.0

    def calcular_promedio_general(self):
        if not self.calificaciones:
            return 0.0
        promedios_materias = [self.calcular_promedio_materia(m) for m in self.calificaciones]
        return self._calcular_promedio(promedios_materias)

    def obtener_materias_por_estado(self, aprobadas=True):
        lista_materias = []
        for materia in self.calificaciones:
            promedio = self.calcular_promedio_materia(materia)
            if (aprobadas and promedio >= self.calificacion_minima_aprobatoria) or \
               (not aprobadas and promedio < self.calificacion_minima_aprobatoria):
                lista_materias.append(materia)
        return lista_materias

    def obtener_materias_aprobadas(self):
        return self.obtener_materias_por_estado(aprobadas=True)

    def obtener_materias_reprobadas(self):
        return self.obtener_materias_por_estado(aprobadas=False)

    def tiene_materias_reprobadas(self):
        return len(self.obtener_materias_reprobadas()) > 0
    
    def _obtener_extremo_materia(self, mejor=True):
        if not self.calificaciones:
            return None, 0.0
        
        promedios = {m: self.calcular_promedio_materia(m) for m in self.calificaciones}
        # Usamos max/min en los items del diccionario, usando lambda para mirar el valor (índice 1)
        if mejor:
            extremo = max(promedios.items(), key=lambda item: item[1])
        else:
            extremo = min(promedios.items(), key=lambda item: item[1])
        return extremo # Retorna (materia, promedio)

    def obtener_mejor_materia(self):
        return self._obtener_extremo_materia(mejor=True)

    def obtener_peor_materia(self):
        return self._obtener_extremo_materia(mejor=False)

    def generar_boleta(self):
        print(f"\n--- Boleta de Calificaciones ---")
        print(f"Estudiante: {self.nombre} (Matrícula: {self.matricula})")
        print(f"Semestre: {self.semestre}")
        print("-" * 30)
        if not self.calificaciones:
            print(" (Sin materias registradas)")
            return
        
        for materia, notas in self.calificaciones.items():
            prom = self.calcular_promedio_materia(materia)
            estado = "Aprobada" if prom >= self.calificacion_minima_aprobatoria else "Reprobada"
            print(f"  Materia: {materia:<15} | Prom: {prom:>4.1f} ({estado})")
            print(f"    Notas: {notas}")
        
        print("-" * 30)
        print(f"PROMEDIO GENERAL: {self.calcular_promedio_general():.2f}")
        if self.tiene_materias_reprobadas():
            print(f"(!) Materias Reprobadas: {self.obtener_materias_reprobadas()}")

    @classmethod
    def total_estudiantes_registrados(cls):
        return cls.total_estudiantes

# --- Pruebas Ejercicio 7 ---
print("\n--- Ejercicio 7: Calificaciones de Estudiantes ---")
# 1. Crear estudiantes
e1 = Estudiante("Carlos", 3)
e2 = Estudiante("Sofia", 5)

# 2. Agregar materias y notas
e1.agregar_materia("Física")
e1.registrar_calificacion("Física", 10)
e1.registrar_calificacion("Física", 8)
e1.agregar_materia("Cálculo")
e1.registrar_calificacion("Cálculo", 5) # Reprobada
e1.registrar_calificacion("Cálculo", 4)
e1.agregar_materia("Programación")
e1.registrar_calificacion("Programación", 9)

e2.agregar_materia("Química")
e2.registrar_calificacion("Química", 9)
e2.registrar_calificacion("Química", 10)
e2.agregar_materia("Historia")
e2.registrar_calificacion("Historia", 8)

# 3. Generar Boletas
e1.generar_boleta()
e2.generar_boleta()

# 4. Reporte Grupal
print("\n--- Reporte Grupal ---")
estudiantes = [e1, e2]
promedio_grupo = sum(e.calcular_promedio_general() for e in estudiantes) / len(estudiantes)

print(f"Total de estudiantes: {Estudiante.total_estudiantes_registrados()}")
print(f"Promedio general del grupo: {promedio_grupo:.2f}")

print("\nEstudiantes con promedio > 8.0:")
for e in estudiantes:
    if e.calcular_promedio_general() > 8.0:
        print(f"  - {e.nombre} ({e.calcular_promedio_general():.2f})")

print("\nEstudiantes con materias reprobadas:")
for e in estudiantes:
    if e.tiene_materias_reprobadas():
        print(f"  - {e.nombre} ({e.obtener_materias_reprobadas()})")


# -----------------------------------------------------------------
# Ejercicio 8: Sistema de Reservas de Hotel
# -----------------------------------------------------------------

class Habitacion:
    total_habitaciones = 0
    habitaciones_ocupadas = 0
    precios_base = {"Simple": 100, "Doble": 150, "Suite": 300}

    def __init__(self, numero, tipo):
        if tipo not in self.precios_base:
            raise ValueError(f"Tipo de habitación '{tipo}' no es válido.")
        
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = self.precios_base[tipo]
        self.ocupada = False
        self.huesped_actual = None
        self.servicios_extras = []
        self.reservas_totales = 0
        Habitacion.total_habitaciones += 1

    def reservar(self, nombre_huesped):
        if not self.ocupada:
            self.ocupada = True
            self.huesped_actual = nombre_huesped
            self.reservas_totales += 1
            Habitacion.habitaciones_ocupadas += 1
            print(f"Habitación {self.numero} ({self.tipo}) reservada por {nombre_huesped}.")
            return True
        else:
            print(f"Error: Habitación {self.numero} ya está ocupada.")
            return False

    def liberar(self):
        if self.ocupada:
            print(f"Habitación {self.numero} liberada. Huésped: {self.huesped_actual}.")
            self.ocupada = False
            self.huesped_actual = None
            self.servicios_extras = []
            Habitacion.habitaciones_ocupadas -= 1
        else:
            print(f"Error: Habitación {self.numero} ya estaba libre.")

    def agregar_servicio_extra(self, servicio, precio):
        if self.ocupada:
            self.servicios_extras.append({"servicio": servicio, "precio": precio})
            print(f"Servicio '{servicio}' ({precio}€) agregado a la Habitación {self.numero}.")
        else:
            print("Error: No se pueden agregar servicios a una habitación desocupada.")

    def calcular_costo_servicios(self):
        return sum(s['precio'] for s in self.servicios_extras)

    def calcular_costo_total(self, num_noches):
        costo_estadia = self.precio_noche * num_noches
        costo_servicios = self.calcular_costo_servicios()
        total = costo_estadia + costo_servicios
        print(f"--- Cálculo de Costo (Hab: {self.numero}) ---")
        print(f"  Estadía ({num_noches} noches): {costo_estadia}€")
        print(f"  Servicios Extras: {costo_servicios}€")
        print(f"  Total: {total}€")
        return total

    def obtener_info(self):
        estado = "OCUPADA" if self.ocupada else "DISPONIBLE"
        info = f"Hab. {self.numero} [{self.tipo}] - {self.precio_noche}€/noche - {estado}"
        if self.ocupada:
            info += f" (Huésped: {self.huesped_actual})"
        return info

    def es_suite(self):
        return self.tipo == "Suite"

    @classmethod
    def calcular_ocupacion(cls):
        if cls.total_habitaciones == 0:
            return 0.0
        return (cls.habitaciones_ocupadas / cls.total_habitaciones) * 100

    @classmethod
    def habitaciones_disponibles_por_tipo(cls, tipo, habitaciones):
        # Necesita la lista de habitaciones para verificar el estado
        count = 0
        for h in habitaciones:
            if h.tipo == tipo and not h.ocupada:
                count += 1
        return count

    @classmethod
    def actualizar_precio_base(cls, tipo, nuevo_precio):
        if tipo in cls.precios_base:
            cls.precios_base[tipo] = nuevo_precio
            print(f"Precio base de '{tipo}' actualizado a {nuevo_precio}€.")
        else:
            print(f"Error: Tipo '{tipo}' no existe.")

# --- Pruebas Ejercicio 8 ---
print("\n--- Ejercicio 8: Reservas de Hotel ---")
# 1. Crear 12 habitaciones
hotel = []
for i in range(1, 5): hotel.append(Habitacion(100 + i, "Simple"))
for i in range(1, 6): hotel.append(Habitacion(200 + i, "Doble"))
for i in range(1, 4): hotel.append(Habitacion(300 + i, "Suite"))

# 2. Realizar reservas
hotel[0].reservar("Juan Perez") # 101 Simple
hotel[5].reservar("Ana Lopez") # 201 Doble
hotel[10].reservar("Leo Messi") # 302 Suite

# 3. Agregar servicios extras
hotel[0].agregar_servicio_extra("Lavandería", 30)
hotel[10].agregar_servicio_extra("Cena VIP", 150)
hotel[1].agregar_servicio_extra("Minibar", 50) # Falla (no ocupada)

# 4. Calcular costos
print("\n--- Cálculo de Costos ---")
hotel[0].calcular_costo_total(3) # 3 noches
hotel[10].calcular_costo_total(2) # 2 noches

# 5. Reporte Final
print("\n--- Reporte Final del Hotel ---")
print(f"Ocupación Actual: {Habitacion.calcular_ocupacion():.1f}% ({Habitacion.habitaciones_ocupadas}/{Habitacion.total_habitaciones})")

ingresos_potenciales = 0
for h in hotel:
    if h.ocupada:
        ingresos_potenciales += h.precio_noche
print(f"Ingresos potenciales por noche (solo estadía): {ingresos_potenciales}€")

print("\nDisponibilidad por tipo:")
tipos = ["Simple", "Doble", "Suite"]
for t in tipos:
    disponibles = Habitacion.habitaciones_disponibles_por_tipo(t, hotel)
    print(f"  {t}: {disponibles} disponibles")

# -----------------------------------------------------------------
# Ejercicio 9: Sistema de Pedidos de Restaurante
# -----------------------------------------------------------------

class Pedido:
    contador_pedidos = 0
    pedidos_activos = 0
    propina_sugerida = 0.10

    def __init__(self, cliente, mesa):
        Pedido.contador_pedidos += 1
        Pedido.pedidos_activos += 1
        self.numero_pedido = Pedido.contador_pedidos
        self.cliente = cliente
        self.items = []
        self.estado = "Pendiente" # "En Preparación", "Listo", "Entregado"
        self.propina = 0
        self.mesa = mesa

    def agregar_item(self, platillo, cantidad, precio_unitario):
        if self.estado == "Pendiente":
            self.items.append({"platillo": platillo, "cantidad": cantidad, "precio_unitario": precio_unitario})
            print(f"Pedido {self.numero_pedido}: Añadido {cantidad}x {platillo}")
        else:
            print(f"Error: No se pueden añadir items a un pedido '{self.estado}'.")

    def eliminar_item(self, platillo):
        item_encontrado = None
        for item in self.items:
            if item['platillo'].lower() == platillo.lower():
                item_encontrado = item
                break
        
        if item_encontrado:
            self.items.remove(item_encontrado)
            print(f"Pedido {self.numero_pedido}: Eliminado {platillo}")
        else:
            print(f"Error: {platillo} no encontrado en el pedido {self.numero_pedido}")

    def calcular_subtotal(self):
        return sum(item['cantidad'] * item['precio_unitario'] for item in self.items)

    def agregar_propina(self, porcentaje=None):
        if porcentaje is None:
            porcentaje = self.propina_sugerida
        else:
            porcentaje = porcentaje / 100.0
            
        self.propina = self.calcular_subtotal() * porcentaje
        print(f"Propina añadida: {self.propina:.2f}€")

    def calcular_total(self):
        return self.calcular_subtotal() + self.propina

    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "En Preparación", "Listo", "Entregado"]
        if nuevo_estado in estados_validos:
            # Actualizar contadores si el pedido deja de estar activo
            if self.estado != "Entregado" and nuevo_estado == "Entregado":
                Pedido.pedidos_activos -= 1
            elif self.estado == "Entregado" and nuevo_estado != "Entregado":
                Pedido.pedidos_activos += 1
                
            self.estado = nuevo_estado
            print(f"Pedido {self.numero_pedido} actualizado a: {self.estado}")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado válido.")

    def obtener_cantidad_items(self):
        return sum(item['cantidad'] for item in self.items)

    def obtener_item_mas_caro(self):
        if not self.items:
            return None
        return max(self.items, key=lambda item: item['precio_unitario'])

    def generar_ticket(self):
        print(f"\n--- TICKET Pedido {self.numero_pedido} (Mesa: {self.mesa}) ---")
        print(f"Cliente: {self.cliente} - Estado: {self.estado}")
        print("-" * 30)
        for item in self.items:
            total_item = item['cantidad'] * item['precio_unitario']
            print(f"  {item['cantidad']}x {item['platillo']:<15} {total_item:>6.2f}€")
        print("-" * 30)
        subtotal = self.calcular_subtotal()
        print(f"  Subtotal: {subtotal:>19.2f}€")
        if self.propina > 0:
            print(f"  Propina: {self.propina:>20.2f}€")
        print(f"  TOTAL: {self.calcular_total():>22.2f}€")
        print("-" * 30)

    @classmethod
    def pedidos_pendientes(cls):
        # Nota: Esto requeriría iterar una lista de instancias
        # Para este ejercicio, solo devolvemos el contador de activos.
        return cls.pedidos_activos

    @classmethod
    def cambiar_propina_sugerida(cls, nuevo_porcentaje):
        cls.propina_sugerida = nuevo_porcentaje / 100.0

# --- Pruebas Ejercicio 9 ---
print("\n--- Ejercicio 9: Pedidos de Restaurante ---")
# 1. Crear pedidos
p1 = Pedido("Familia Garcia", 5)
p2 = Pedido("Pareja Mesa 2", 2)
p3 = Pedido("Juan Solo", 1)

# 2. Agregar items
p1.agregar_item("Pizza", 2, 12.50)
p1.agregar_item("Refresco", 4, 2.00)

p2.agregar_item("Pasta", 1, 15.00)
p2.agregar_item("Vino", 1, 18.00)

p3.agregar_item("Café", 1, 1.50)

# 3. Cambiar estados y agregar propinas
p1.cambiar_estado("En Preparación")
p2.cambiar_estado("En Preparación")

p1.agregar_item("Agua", 1, 1.00) # Falla (ya no está pendiente)

p1.cambiar_estado("Listo")
p1.agregar_propina(10) # 10%
p1.cambiar_estado("Entregado")

p2.cambiar_estado("Entregado") # Sin propina

p3.cambiar_estado("Entregado")
p3.agregar_propina() # Propina sugerida (10%)

# 4. Reporte Final
print("\n--- Reporte Final de Pedidos ---")
pedidos = [p1, p2, p3]
total_ingresos = 0
pedido_mayor_valor = None

for p in pedidos:
    p.generar_ticket()
    total_ingresos += p.calcular_total()
    if pedido_mayor_valor is None or p.calcular_total() > pedido_mayor_valor.calcular_total():
        pedido_mayor_valor = p

print("\n--- Resumen del Día ---")
print(f"Total Ingresos (con propina): {total_ingresos:.2f}€")
print(f"Pedidos activos (no entregados): {Pedido.pedidos_activos}")
if pedido_mayor_valor:
    print(f"Pedido con mayor valor: #{pedido_mayor_valor.numero_pedido} ({pedido_mayor_valor.calcular_total():.2f}€)")


# -----------------------------------------------------------------
# Ejercicio 10: Sistema de Eventos y Asistentes
# -----------------------------------------------------------------

class Evento:
    total_eventos = 0
    eventos_agotados = 0
    descuento_estudiante = 0.20
    descuento_grupo = 0.15 # (para 4 o más)

    def __init__(self, nombre_evento, fecha, ubicacion, capacidad_maxima, precio_entrada, tipo_evento):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.precio_entrada = precio_entrada
        self.asistentes_registrados = [] # Lista de dicts {nombre, email, pago_realizado, es_estudiante}
        self.ingresos_totales = 0
        self.tipo_evento = tipo_evento
        Evento.total_eventos += 1

    def obtener_cupos_disponibles(self):
        return self.capacidad_maxima - len(self.asistentes_registrados)

    def esta_agotado(self):
        return self.obtener_cupos_disponibles() <= 0

    def _registrar_asistente_base(self, nombre, email, es_estudiante=False):
        if self.esta_agotado():
            print(f"Error [{self.nombre_evento}]: Evento agotado. No se pudo registrar a {nombre}.")
            return False
        
        self.asistentes_registrados.append({
            "nombre": nombre,
            "email": email,
            "pago_realizado": False,
            "es_estudiante": es_estudiante
        })
        return True

    def registrar_asistente(self, nombre, email, es_estudiante=False):
        if self._registrar_asistente_base(nombre, email, es_estudiante):
            print(f"Asistente '{nombre}' registrado para {self.nombre_evento}.")

    def registrar_grupo(self, lista_asistentes_grupo):
        # lista_asistentes_grupo es una lista de dicts {nombre, email, es_estudiante}
        if len(lista_asistentes_grupo) > self.obtener_cupos_disponibles():
            print(f"Error [{self.nombre_evento}]: Cupo insuficiente para registrar al grupo.")
            return

        print(f"Registrando grupo de {len(lista_asistentes_grupo)} personas...")
        for asistente in lista_asistentes_grupo:
            self._registrar_asistente_base(
                asistente['nombre'], 
                asistente['email'], 
                asistente.get('es_estudiante', False)
            )
        
    def _buscar_asistente(self, email):
        for asistente in self.asistentes_registrados:
            if asistente['email'] == email:
                return asistente
        return None

    def confirmar_pago(self, email):
        asistente = self._buscar_asistente(email)
        if not asistente:
            print(f"Error: Email {email} no encontrado en los registros.")
            return

        if asistente['pago_realizado']:
            print(f"Info: {asistente['nombre']} ya había pagado.")
            return

        precio_final = self.precio_entrada
        if asistente['es_estudiante']:
            precio_final *= (1 - self.descuento_estudiante)
            print(f"Aplicando descuento de estudiante a {asistente['nombre']}...")
        
        # (Nota: Lógica de descuento de grupo se aplicaría aquí si el pago es grupal)
        
        asistente['pago_realizado'] = True
        self.ingresos_totales += precio_final
        print(f"Pago confirmado para {asistente['nombre']}. Monto: {precio_final:.2f}€")

    def _contar_asistentes_por_pago(self, pagado=True):
        return sum(1 for a in self.asistentes_registrados if a['pago_realizado'] == pagado)

    def calcular_asistentes_confirmados(self):
        return self._contar_asistentes_por_pago(pagado=True)

    def calcular_asistentes_pendientes(self):
        return self._contar_asistentes_por_pago(pagado=False)

    def calcular_porcentaje_ocupacion(self):
        if self.capacidad_maxima == 0: return 0.0
        return (len(self.asistentes_registrados) / self.capacidad_maxima) * 100

    def calcular_ingreso_potencial(self):
        # Calcula cuánto faltaría si todos los pendientes pagan
        ingreso_pendiente = 0
        for a in self.asistentes_registrados:
            if not a['pago_realizado']:
                precio_final = self.precio_entrada
                if a['es_estudiante']:
                    precio_final *= (1 - self.descuento_estudiante)
                ingreso_pendiente += precio_final
        return self.ingresos_totales + ingreso_pendiente

    def obtener_lista_asistentes(self, confirmados=True):
        return [a['nombre'] for a in self.asistentes_registrados if a['pago_realizado'] == confirmados]

    def cancelar_registro(self, email):
        asistente = self._buscar_asistente(email)
        if asistente:
            if asistente['pago_realizado']:
                # (Lógica de reembolso omitida, solo ajusta ingresos)
                precio_reembolso = self.precio_entrada
                if asistente['es_estudiante']:
                    precio_reembolso *= (1 - self.descuento_estudiante)
                self.ingresos_totales -= precio_reembolso
            
            self.asistentes_registrados.remove(asistente)
            print(f"Registro de {asistente['nombre']} ({email}) cancelado.")
            if self.esta_agotado(): # Si estaba lleno, actualiza contador
                Evento.eventos_agotados -= 1
        else:
            print(f"Error: Email {email} no encontrado.")

    def generar_reporte(self):
        print(f"\n--- Reporte de Evento: {self.nombre_evento} ({self.tipo_evento}) ---")
        print(f"  Fecha: {self.fecha} | Ubicación: {self.ubicacion}")
        print(f"  Precio Entrada: {self.precio_entrada}€")
        if self.esta_agotado():
            print("  ESTADO: ¡AGOTADO! (SOLD OUT)")
            if not any(e == self for e in getattr(Evento, '_eventos_agotados_lista', [])):
                 Evento.eventos_agotados += 1
                 if not hasattr(Evento, '_eventos_agotados_lista'):
                     Evento._eventos_agotados_lista = []
                 Evento._eventos_agotados_lista.append(self)
        
        print(f"  Ocupación: {self.calcular_porcentaje_ocupacion():.1f}% ({len(self.asistentes_registrados)}/{self.capacidad_maxima})")
        print(f"  Asistentes Confirmados (Pagados): {self.calcular_asistentes_confirmados()}")
        print(f"  Asistentes Pendientes de Pago: {self.calcular_asistentes_pendientes()}")
        print(f"  Ingresos Actuales: {self.ingresos_totales:.2f}€")
        print(f"  Ingreso Potencial (si todos pagan): {self.calcular_ingreso_potencial():.2f}€")

    @classmethod
    def total_eventos_creados(cls):
        return cls.total_eventos

    @classmethod
    def actualizar_descuento_estudiante(cls, nuevo_descuento):
        cls.descuento_estudiante = nuevo_descuento / 100.0

    @classmethod
    def eventos_sold_out(cls):
        # Esta es una implementación simple; idealmente, se manejaría
        # en el método 'reservar' cuando se agota.
        return cls.eventos_agotados


# --- Pruebas Ejercicio 10 ---
print("\n--- Ejercicio 10: Sistema de Eventos ---")
# 1. Crear 4 eventos
concierto = Evento("Concierto Rock", "01-12-2025", "Estadio", 100, 80, "Concierto")
conferencia = Evento("Tech Summit", "15-11-2025", "Centro de Convenciones", 50, 200, "Conferencia")
teatro = Evento("Obra Clásica", "20-11-2025", "Teatro Nacional", 3, 40, "Teatro")
deportivo = Evento("Final Fútbol", "05-12-2025", "Estadio", 200, 60, "Deportivo")

# 2. Registrar asistentes (individuales y grupos)
print("\n--- Registros y Pagos ---")
concierto.registrar_asistente("Carlos", "carlos@mail.com", es_estudiante=True)
concierto.registrar_asistente("Ana", "ana@mail.com")

grupo_tech = [
    {"nombre": "Empresa A1", "email": "e1@mail.com"},
    {"nombre": "Empresa A2", "email": "e2@mail.com"},
    {"nombre": "Empresa A3", "email": "e3@mail.com"},
    {"nombre": "Empresa A4", "email": "e4@mail.com"} # Grupo de 4
]
conferencia.registrar_grupo(grupo_tech) # (Descuento de grupo se aplica al pagar)

# 3. Llenar un evento
teatro.registrar_asistente("Luis", "luis@mail.com")
teatro.registrar_asistente("Maria", "maria@mail.com")
teatro.registrar_asistente("Pedro", "pedro@mail.com")
teatro.registrar_asistente("Julia", "julia@mail.com") # Falla (agotado)

# 4. Confirmar pagos
concierto.confirmar_pago("carlos@mail.com") # Pago con descuento estudiante
concierto.confirmar_pago("ana@mail.com") # Pago normal
conferencia.confirmar_pago("e1@mail.com") # Pago normal (descuento grupo no implementado en pago individual)

# 5. Cancelar registro
concierto.cancelar_registro("ana@mail.com") # Cancela un pago ya hecho

# 6. Reporte Final
print("\n--- Reporte Final del Sistema ---")
eventos = [concierto, conferencia, teatro, deportivo]
ingresos_totales_sistema = 0
asistentes_totales_confirmados = 0
evento_mayor_ocupacion = None

for e in eventos:
    e.generar_reporte()
    ingresos_totales_sistema += e.ingresos_totales
    asistentes_totales_confirmados += e.calcular_asistentes_confirmados()
    if evento_mayor_ocupacion is None or e.calcular_porcentaje_ocupacion() > evento_mayor_ocupacion.calcular_porcentaje_ocupacion():
        evento_mayor_ocupacion = e

print("\n--- Resumen General del Sistema ---")
print(f"Total de Eventos Creados: {Evento.total_eventos_creados()}")
print(f"Total Eventos Agotados: {Evento.eventos_sold_out()}")
print(f"Ingresos Totales del Sistema: {ingresos_totales_sistema:.2f}€")
print(f"Total Asistentes Confirmados: {asistentes_totales_confirmados}")
if evento_mayor_ocupacion:
    print(f"Evento con Mayor Ocupación: {evento_mayor_ocupacion.nombre_evento} ({evento_mayor_ocupacion.calcular_porcentaje_ocupacion():.1f}%)")