# practica_17.py
# Soluciones a los ejercicios de Herencia, Métodos Estáticos y de Clase.

import datetime

# -----------------------------------------------------------------------------
# EJERCICIO 4: Métodos de Instancia (Videojuego)
# -----------------------------------------------------------------------------
print("\n=== EJERCICIO 4: Tienda de Videojuegos ===")

class Videojuego:
    def __init__(self, titulo, plataforma, precio, unidades):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.unidades = unidades

    def mostrar_detalle(self):
        print(f"🎮 {self.titulo} ({self.plataforma}) - {self.precio}€ [Stock: {self.unidades}]")

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Descuento aplicado (-{porcentaje}%). Nuevo precio: {self.precio:.2f}€")

    def vender(self, cantidad):
        if self.unidades >= cantidad:
            self.unidades -= cantidad
            total = self.precio * cantidad
            print(f"Venta exitosa: {cantidad}x {self.titulo}. Total: {total:.2f}€")
        else:
            print(f"Error: No hay suficiente stock de {self.titulo} (Quedan: {self.unidades})")

# --- Pruebas Ex 4 ---
juego1 = Videojuego("Elden Ring", "PS5", 69.99, 10)
juego1.mostrar_detalle()
juego1.aplicar_descuento(10)
juego1.vender(2)
juego1.vender(9) # Falla


# -----------------------------------------------------------------------------
# EJERCICIO 5: Métodos de Instancia, Clase y Estáticos (Academia)
# -----------------------------------------------------------------------------
print("\n=== EJERCICIO 5: Academia de Idiomas ===")

class Estudiante:
    # Atributos de Clase
    total_estudiantes = 0
    cuota_mensual = 120

    def __init__(self, nombre, idioma, nivel):
        if not Estudiante.validar_nivel(nivel):
            raise ValueError(f"Nivel {nivel} no válido.")
        
        self.nombre = nombre
        self.idioma = idioma
        self.nivel = nivel
        Estudiante.total_estudiantes += 1

    # Método de Instancia
    def mostrar_perfil(self):
        print(f"Estudiante: {self.nombre} | Idioma: {self.idioma} ({self.nivel})")

    # Método de Clase (recibe cls)
    @classmethod
    def mostrar_estadisticas(cls):
        print(f"--- Estadísticas Academia ---")
        print(f"Total Estudiantes: {cls.total_estudiantes}")
        print(f"Cuota Actual: {cls.cuota_mensual}€")
        print(f"Ingresos Mensuales Estimados: {cls.total_estudiantes * cls.cuota_mensual}€")

    @classmethod
    def cambiar_cuota(cls, nueva_cuota):
        cls.cuota_mensual = nueva_cuota
        print(f"La cuota ha cambiado a {cls.cuota_mensual}€")

    # Método Estático (no recibe self ni cls)
    @staticmethod
    def validar_nivel(nivel):
        niveles_validos = ["A1", "A2", "B1", "B2", "C1", "C2"]
        return nivel in niveles_validos

# --- Pruebas Ex 5 ---
try:
    e1 = Estudiante("Ana", "Inglés", "B2")
    e2 = Estudiante("Luis", "Francés", "A1")
    e3 = Estudiante("Sara", "Alemán", "C1")
    # e4 = Estudiante("Fail", "Chino", "D3") # Esto lanzaría error

    e1.mostrar_perfil()
    
    Estudiante.mostrar_estadisticas()
    Estudiante.cambiar_cuota(130)
    Estudiante.mostrar_estadisticas()
    
    print(f"¿Es válido el nivel 'C2'? {Estudiante.validar_nivel('C2')}")
    print(f"¿Es válido el nivel 'Z9'? {Estudiante.validar_nivel('Z9')}")

except ValueError as e:
    print(f"Error: {e}")


# -----------------------------------------------------------------------------
# EJERCICIO 6: Herencia Simple (Logística)
# -----------------------------------------------------------------------------
print("\n=== EJERCICIO 6: Empresa de Logística (Herencia) ===")

class Paquete:
    def __init__(self, id_seguimiento, peso_kg, origen, destino):
        self.id_seguimiento = id_seguimiento
        self.peso_kg = peso_kg
        self.origen = origen
        self.destino = destino

    def mostrar_info(self):
        print(f"📦 [{self.id_seguimiento}] {self.origen} -> {self.destino} ({self.peso_kg}kg)")

    def calcular_costo_base(self):
        return self.peso_kg * 2.5

# Clase Hija 1
class PaqueteFragil(Paquete):
    def __init__(self, id_seguimiento, peso_kg, origen, destino, seguro=True):
        # Llamada al constructor del padre
        super().__init__(id_seguimiento, peso_kg, origen, destino)
        self.seguro = seguro

    def mostrar_advertencia(self):
        print("⚠️  FRÁGIL - MANEJAR CON CUIDADO ⚠️")

    # Sobrescritura (Override)
    def calcular_costo_base(self):
        costo = super().calcular_costo_base() # Reutilizamos la lógica del padre
        if self.seguro:
            costo += 10
        return costo

# Clase Hija 2
class PaqueteExpress(Paquete):
    def __init__(self, id_seguimiento, peso_kg, origen, destino, fecha_limite):
        super().__init__(id_seguimiento, peso_kg, origen, destino)
        self.fecha_limite = fecha_limite # String formato "YYYY-MM-DD"

    def tiempo_restante(self, fecha_actual):
        # Simulación simple de días
        return "2 días" # Simplificado para el ejercicio

    # Sobrescritura
    def calcular_costo_base(self):
        return super().calcular_costo_base() * 2

# --- Pruebas Ex 6 ---
p_normal = Paquete("PKG001", 2.0, "Madrid", "Barcelona")
p_fragil = PaqueteFragil("PKG002", 1.5, "Valencia", "Bilbao", seguro=True)
p_express = PaqueteExpress("PKG003", 0.5, "Sevilla", "Madrid", "2025-11-10")

print(f"\n--- Paquete Normal ---")
p_normal.mostrar_info()
print(f"Costo: {p_normal.calcular_costo_base()}€")

print(f"\n--- Paquete Frágil ---")
p_fragil.mostrar_info()
p_fragil.mostrar_advertencia()
print(f"Costo: {p_fragil.calcular_costo_base()}€ (Incluye seguro)")

print(f"\n--- Paquete Express ---")
p_express.mostrar_info()
print(f"Costo: {p_express.calcular_costo_base()}€ (Tarifa doble)")


# -----------------------------------------------------------------------------
# EJERCICIO 7: Polimorfismo (Streaming)
# -----------------------------------------------------------------------------
print("\n=== EJERCICIO 7: Plataforma de Streaming ===")

class PlanSuscripcion:
    def __init__(self, nombre_usuario, meses_contratados):
        self.nombre_usuario = nombre_usuario
        self.meses_contratados = meses_contratados

    def calcular_precio(self):
        return 0.0

    def mostrar_resumen(self):
        print(f"\n👤 Usuario: {self.nombre_usuario}")
        print(f"📅 Duración: {self.meses_contratados} meses")
        print(f"💰 Precio Total: {self.calcular_precio():.2f}€")

class PlanBasico(PlanSuscripcion):
    PRECIO_MES = 7.99
    
    def calcular_precio(self):
        return self.meses_contratados * self.PRECIO_MES
    
    def mostrar_caracteristicas(self):
        print("- Calidad: 720p\n- Pantallas: 1")

    def mostrar_resumen(self):
        super().mostrar_resumen() # Llama al padre primero
        self.mostrar_caracteristicas()

class PlanEstandar(PlanSuscripcion):
    PRECIO_MES = 12.99
    
    def calcular_precio(self):
        total = self.meses_contratados * self.PRECIO_MES
        if self.meses_contratados >= 12:
            total *= 0.85 # 15% descuento
            print("(Descuento anual del 15% aplicado)")
        return total
    
    def mostrar_caracteristicas(self):
        print("- Calidad: 1080p\n- Pantallas: 2")

    def mostrar_resumen(self):
        super().mostrar_resumen()
        self.mostrar_caracteristicas()

class PlanPremium(PlanSuscripcion):
    PRECIO_MES = 17.99
    
    def calcular_precio(self):
        total = self.meses_contratados * self.PRECIO_MES
        if self.meses_contratados >= 12:
            total *= 0.80 # 20% descuento
            print("(Descuento anual del 20% aplicado)")
        return total
    
    def mostrar_caracteristicas(self):
        print("- Calidad: 4K HDR\n- Pantallas: 4\n- Descargas: Ilimitadas")

    def mostrar_resumen(self):
        super().mostrar_resumen()
        self.mostrar_caracteristicas()

# --- Pruebas Ex 7 ---
cliente1 = PlanBasico("Juan", 1)
cliente2 = PlanEstandar("Maria", 12) # Aplica descuento
cliente3 = PlanPremium("Pedro", 6)

cliente1.mostrar_resumen()
cliente2.mostrar_resumen()
cliente3.mostrar_resumen()